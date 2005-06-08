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

from papo import cimarron
from base import Controller, WindowController

class CRUDController (WindowController):
    """
    CRUD ('ABM' in spanish) Controller .
    see: http://c2.com/cgi/wiki?CrudScreen
    """
    def attributesToConnect (klass):
        attrs = super (CRUDController, klass).attributesToConnect ()
        return attrs+['klass']
    attributesToConnect= classmethod (attributesToConnect)
    
    def __init__ (self, klass=None, searchColumns=[], editorKlass=None, filename=None, **kw):
        self.editors= []
        super (CRUDController, self).__init__ (**kw)
        self.note= cimarron.skin.Notebook (parent=self.win)

        # first tab
        self.firstTab= cimarron.skin.VBox (label='Search')
        self.firstTab.parent= self.note

        self.new= cimarron.skin.Button (
            parent= self.firstTab,
            label= 'New',
            )

        self.klass= klass

        if searchColumns:
            # add the Search thing
            self.search= cimarron.skin.Search (
                parent= self.firstTab,
                columns= searchColumns,
                onAction= self.changeModel,
                )

        # second tab
        if editorKlass is not None:
            if filename is not None:
                modelEditor= editorKlass.fromXmlFile (filename)
            else:
                # let's hope the editorKlass knows what to do
                modelEditor= editorKlass ()
            modelEditor.parent= self.note
            self.editors.append (modelEditor)
            self.mainWidget= modelEditor

        # more tabs?

    def _set_klass (self, klass):
        if klass is not None:
            self.new.onAction= lambda control, *ignore: self.newModel (control, klass, *ignore)
        self._klass= klass
    def _get_klass (self):
        return self._klass
    klass= property (_get_klass, _set_klass)
        
    def newModel (self, control, klass, *ignore):
        self.changeModel (control, klass ())

    def changeModel (self, control, model=None):
        if model is None:
            self.value= self.search.value
        else:
            self.value= model

        # print 'CRUD.changeModel', `model`, model is None, self.search.value, self.value
        if self.value is not None:
            self.note.activate (1)
            # and this?
            # self.editor.focus ()

    def save (self, *ignore):
        self.onAction ()

    def refresh (self):
        for editor in self.editors:
            try:
                editor.value= editor.read ()
                # print 'CRUD:', editor, `editor.read`, `editor.value`
            except (AttributeError, TypeError):
                editor.value= self.value
                # print 'CRUD:', editor, `editor.value`

    def fromXmlObj (klass, xmlObj, skin):
        self = klass()
        root= xmlObj
        attrs= {self: klass.attributesToConnect ()}
        idDict= {}

        xmlObj = xmlObj.children
        first= True
        second= False
        while xmlObj:
            (obj, attrsInChild, idDictInChild)= self.childFromXmlObj (xmlObj, skin)
            if obj is not None:
                if first:
                    obj.parent= self.firstTab
                    self.search= obj
                    first= False
                    second= True
                else:
                    obj.parent= self.note
                    self.editors.append (obj)
                    if second:
                        self.mainWidget= obj
                        obj.onAction= self.save
                        second= False

                attrsInChild[obj]+= ['read', 'write']
                attrs.update (attrsInChild)
            idDict.update (idDictInChild)
            xmlObj= xmlObj.next

        # at this time, so it has time to do the <import>s
        self.fromXmlObjProps(root.properties)
        try:
            idDict[self.id]= self
        except AttributeError:
            # have no id, ignore
            pass
        
        return (self, attrs, idDict)
    fromXmlObj = classmethod(fromXmlObj)
        

class Editor (Controller):
    def refresh (self, *ignore):
        try:
            for entry in self.entries.children:
                try:
                    entry.value= entry.read ()
                    # print 'editor:', entry, `entry.read.other`, entry.read.path, `entry.value`
                except TypeError:
                    # print 'editor:', entry, `entry.read.other`, entry.read.path, `self.value`
                    entry.value= self.value
                except AttributeError:
                    entry.value= self.value
                    # print 'editor:', entry, `entry.value`
        except AttributeError:
            # the entries are not there yet
            pass

    def modifyModel (self, control, *ignore):
        try:
            control.write (control.value)
        except AttributeError:
            # no saving needed?
            # yes, it's possible, like a grid editing addresses
            # it modifies the addresses directly.
            pass

    def save (self, *ignore):
        # how will this be finally done is a mistery (yet)
        # print 'save', str (self.value)
        self.onAction ()
    def discard (self, *ignore):
        # how will this be finally done is a mistery (yet)
        # print 'discard', self.value
        pass

    def will_focus_out (self, control, *ignore):
        self.modifyModel (control)

    def fromXmlObj (klass, xmlObj, skin):
        self = klass()
        self.fromXmlObjProps(xmlObj.properties)
        try:
            idDict= {self.id: self}
        except AttributeError:
            idDict= {}

        # main containers
        vbox= cimarron.skin.VBox (parent=self, label=self.label)
        hbox= cimarron.skin.HBox (parent=vbox)
        labels= cimarron.skin.VBox (parent=hbox)
        self.entries= cimarron.skin.VBox (parent=hbox)

        # load children
        attrs= {self: klass.attributesToConnect ()}
        xmlObj = xmlObj.children
        while xmlObj:
            (obj, attrsInChild, idDictInChild)= self.childFromXmlObj (xmlObj, skin)
            if obj!=None:
                if xmlObj.name=="Label":
                    obj.parent= labels
                else:
                    obj.parent= self.entries
                    obj.onAction= self.modifyModel
                    obj.delegates.append (self)
                    attrsInChild[obj]+= ['read', 'write']
                attrs.update (attrsInChild)
            idDict.update (idDictInChild)
            
            xmlObj= xmlObj.next

        # save/discard buttons
        hbox= cimarron.skin.HBox (parent=vbox)
        save= cimarron.skin.Button (
            parent= hbox,
            label= 'Save',
            onAction= self.save,
            )
        # so tests passes
        self.mainWidget= save
        discard= cimarron.skin.Button (
            parent= hbox,
            label= 'Discard',
            onAction= self.discard,
            )

        return (self, attrs, idDict)
    fromXmlObj = classmethod(fromXmlObj)