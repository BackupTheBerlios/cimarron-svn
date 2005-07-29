# -*- coding: utf-8 -*-
#
# Copyright 2005 Fundación Via Libre
#
# This file is part of PAPO.
#
# PAPO is free software; you can redistribute it and/or modify it under the
# terms of the GNU General Public License as published by the Free Software
# Foundation; either version 2 of the License, or (at your option) any later
# version.
#
# PAPO is distributed in the hope that it will be useful, but WITHOUT ANY
# WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
# FOR A PARTICULAR PURPOSE.  See the GNU General Public License for more
# details.
#
# You should have received a copy of the GNU General Public License along with
# PAPO; if not, write to the Free Software Foundation, Inc., 59 Temple Place,
# Suite 330, Boston, MA 02111-1307 USA
"""
CRUD controllers and related junk.
"""
__revision__ = int('$Rev$'[5:-1])

import logging

from fvl.cimarron.controllers.base import Controller, WindowController

logger = logging.getLogger('fvl.cimarron.controllers.crud')

class CRUDController (WindowController):
    """
    CRUD ('ABM' in spanish) Controller .
    see: http://c2.com/cgi/wiki?CrudScreen
    """
    def attributesToConnect (cls):
        """
        See L{XmlMixin.attributesToConnect
        <fvl.cimarron.skins.common.XmlMixin.attributesToConnect>}
        """
        attrs = super(CRUDController, cls).attributesToConnect()
        return attrs+['cls']
    attributesToConnect = classmethod(attributesToConnect)
    
    def __init__ (self, cls=None, searchColumns=None, editorClass=None,
                  filename=None, store=None, **kwargs):
        from fvl.cimarron.skin import Notebook, VBox, Button

        self.editors = []
        super(CRUDController, self).__init__(**kwargs)
        self.note = Notebook(parent=self.window)

        # first tab
        self.firstTab = VBox(label='Search')
        self.firstTab.parent = self.note

        self.new = Button(parent=self.firstTab, label='New', expand=False)
        self.cls = cls
        self.store = store

        if searchColumns:
            # add the Search thing
            self.search = Search(parent=self.firstTab, columns=searchColumns,
                                 onAction=self.changeModel)

        # second tab
        if editorClass is not None:
            if filename is not None:
                modelEditor = editorClass.fromXmlFile(filename)
            else:
                # let's hope the editorClass knows what to do
                modelEditor = editorClass()
            modelEditor.parent = self.note
            self.editors.append(modelEditor)
            self.mainWidget = modelEditor

        # more tabs?
        # FIXME: complete!

    def _set_value(self, value):
        self.__value = value
        for editor in self.editors:
            editor.newTarget(self.__value)
    def _get_value(self):
        return self.__value
    value = property(_get_value, _set_value)

    def _set_cls (self, cls):
        if cls is not None:
            def onAction(control, *ignore):
                return self.newModel(control, cls, *ignore)
            self.new.onAction = onAction
        self._cls = cls
    def _get_cls (self):
        return self._cls
    cls = property(_get_cls, _set_cls, None, """
        The CRUD's 'class'. This is, the callable used to create
        a new object of the type the CRUD is editing.""")

    def _set_store(self, store):
        self.__store = store
        for editor in self.editors:
            editor.store = store
    def _get_store(self):
        return self.__store
    store = property(_get_store, _set_store, None, """""")
        
    def newModel(self, control, cls, *ignore):
        """
        Create a new object and point the CRUD at it.
        """
        self.changeModel(control, cls())

    def changeModel(self, control, model=None):
        """
        Updates the CRUD's currently-in-edition object.
        """
        if model is None:
            value = self.search.value
        else:
            value = model
        self.commitValue(value)

        if value is not None:
            self.note.activate(1)
            # and this?
            # self.editor.focus ()

    def save (self, *ignore):
        self.store.save()
        # FIXME: really?
        self.onAction()

    def discard(self):
        self.store.discard()

    def fromXmlObj (cls, xmlObj):
        """
        See L{XmlMixin.fromXmlObj
        <fvl.cimarron.skins.common.XmlMixin.fromXmlObj>}
        """
        self = cls()
        root = xmlObj
        attrs = {self: cls.attributesToConnect()}
        idDict = {}

        xmlObj = xmlObj.children
        first = True
        second = False
        while xmlObj:
            (obj, attrsInChild, idDictInChild) = \
                  self.childFromXmlObj(xmlObj)
            if obj is not None:
                if first:
                    obj.parent = self.firstTab
                    self.search = obj
                    first = False
                    second = True
                else:
                    obj.parent = self.note
                    self.editors.append(obj)
                    if second:
                        self.mainWidget = obj
                        obj.onAction = self.save
                        second = False

                attrs.update(attrsInChild)
            idDict.update(idDictInChild)
            xmlObj = xmlObj.next

        # at this time, so it has time to do the <import>s
        self.fromXmlObjProps(root.properties)
        try:
            idDict[self.id] = self
        except AttributeError:
            # have no id, ignore
            pass
        
        return (self, attrs, idDict)
    fromXmlObj = classmethod(fromXmlObj)
        
class Editor(Controller):
    def __init__(self, attributes=None, label='', store=None, **kwargs):
        from fvl.cimarron.skin import VBox, HBox, Button, Label, Entry

        super(Editor, self).__init__(**kwargs)
        if attributes is None:
            attributes = []
        self.store = store

        # main containers
        self._outerWidget = self.vbox = VBox(parent=self)

        hbox = HBox(parent=self.vbox)
        self.labels = VBox(parent=hbox)
        self.entries = VBox(parent=hbox)

        self.label = label
        for attr in attributes:
            Label(parent=self.labels, text=attr)
            # FIX: make if more flexible
            Entry(parent=self.entries, attribute=attr)
    
        # save/discard buttons
        hbox = HBox(parent=self.vbox, expand=False)
        save = Button(parent=hbox, label='Save', onAction=self.save)
        self.mainWidget = save
        discard = Button (parent=hbox, label='Discard', onAction=self.discard)

    def _set_value(self, value):
        self.__value = value
        try:
            entries = self.entries.children
        except AttributeError, e:
            # the entries are not there yet
            pass
        else:
            value = self.__value
            for entry in entries:
                entry.newTarget (value)
    def _get_value(self):
        return self.__value
    value = property(_get_value, _set_value)

    def _set_label(self, label):
        self.vbox.label = label
    def _get_label(self):
        return self.vbox.label
    label = property(_get_label, _set_label)

    def modifyModel (self, control, *ignore):
        try:
            control.write (control.value)
        except AttributeError:
            # no saving needed?
            # yes, it's possible, like a grid editing addresses
            # it modifies the addresses directly.
            pass

    def save (self, *ignore):
        # print 'save', str (self.value)
        self.store.save()
        self.onAction ()
    def discard (self, *ignore):
        # print 'discard', self.value
        self.store.discard()

    def will_focus_out (self, control, *ignore):
        self.modifyModel (control)

    def fromXmlObj (cls, xmlObj):
        from fvl.cimarron.skin import HBox, VBox, Button
        
        self = cls()
        self.fromXmlObjProps(xmlObj.properties)
        try:
            idDict = {self.id: self}
        except AttributeError:
            idDict = {}

        # load children
        attrs = {self: cls.attributesToConnect()}
        xmlObj = xmlObj.children
        while xmlObj:
            (obj, attrsInChild, idDictInChild) = \
                  self.childFromXmlObj(xmlObj)
            if obj is not None:
                if xmlObj.name == "Label":
                    obj.parent = self.labels
                else:
                    obj.parent = self.entries
                    obj.onAction = self.modifyModel
                    obj.delegates.append(self)
                attrs.update(attrsInChild)
            idDict.update(idDictInChild)
            
            xmlObj = xmlObj.next

        return (self, attrs, idDict)
    fromXmlObj = classmethod(fromXmlObj)
