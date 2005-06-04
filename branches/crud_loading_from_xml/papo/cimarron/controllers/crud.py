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
    C(reate)R(ead)U(pdate)D(elete) Controller ('ABM' in spanish).
    see: http://c2.com/cgi/wiki?CrudScreen
    """
    def toConnect (klass):
        toConnect= super (CRUDController, klass).toConnect ()
        return toConnect+['klass']
    toConnect= classmethod (toConnect)
    
    def __init__ (self, klass=None, searchColumns=[], editorKlass=None, filename=None, **kw):
        super (CRUDController, self).__init__ (**kw)
        self.note= cimarron.skin.Notebook (parent=self.win)
        self.editors= {}

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
            self.editors[modelEditor]= lambda x: x

        # more tabs?

    def _set_klass (self, klass):
        if klass is not None:
            self.new.onAction= lambda control, *ignore: self.newModel (control, klass, *ignore)
        self._klass= klass
    def _get_klass (self):
        return self._klass
    klass= property (_get_klass, _set_klass)
        
    def newModel (self, control, klass, *ignore):
        print 'newModel'
        self.changeModel (control, klass ())

    def changeModel (self, control, model=None):
        if model is None:
            self.value= self.search.value
        else:
            self.value= model
        for editor, f in self.editors.items ():
            editor.value= f (self.value)
        self.note.activate (1)
        # and this?
        # self.editor.focus ()

    def save (self, *ignore):
        pass

    def refresh (self):
        # update all the `children'
        for child in self.note.children:
            try:
                child.refresh ()
            except AttributeError:
                pass

    def fromXmlObj (klass, xmlObj, skin):
        self = klass()
        root= xmlObj
        toConnect= {self: klass.toConnect ()}

        xmlObj = xmlObj.children
        first= True
        while xmlObj:
            (obj, toConnectInChild)= self.childFromXmlObj (xmlObj, skin)
            if obj is not None:
                if first:
                    obj.parent= self.firstTab
                    self.search= obj
                    first= False
                else:
                    obj.parent= self.note
                    self.editors[obj]= lambda x: x
                toConnect.update (toConnectInChild)
            xmlObj= xmlObj.next

        # at this time, so it has time to do the <import>s
        self.fromXmlObjProps(root.properties)
        toConnect= self._connect (toConnect)
        
        return (self, toConnect)
    fromXmlObj = classmethod(fromXmlObj)
        
class Editor (Controller):
    def refresh (self, *ignore):
        # the _attributes_ must be in the same order
        # than the entries :(
        if self.value is not None:
            for entry in self.entries.children:
                entry.value= entry.read (self.value)

    def modifyModel (self, control, *ignore):
        control.write (self.value, control.value)

    def save (self, *ignore):
        # how will thi be finally done is a mistery (yet)
        print 'save', str (self.value)
        pass
    def discard (self, *ignore):
        # how will thi be finally done is a mistery (yet)
        print 'discard', self.value
        pass

    def will_focus_out (self, control, *ignore):
        self.modifyModel (control)

    def fromXmlObj (klass, xmlObj, skin):
        self = klass()
        self.fromXmlObjProps(xmlObj.properties)

        # main containers
        vbox= cimarron.skin.VBox (parent=self, label=self.label)
        hbox= cimarron.skin.HBox (parent=vbox)
        labels= cimarron.skin.VBox (parent=hbox)
        self.entries= cimarron.skin.VBox (parent=hbox)

        # load children
        toConnect= {self: klass.toConnect ()}
        xmlObj = xmlObj.children
        while xmlObj:
            (obj, toConnectInChild)= self.childFromXmlObj (xmlObj, skin)
            if obj!=None:
                if xmlObj.name=="Label":
                    obj.parent= labels
                else:
                    obj.parent= self.entries
                    obj.onAction= self.modifyModel
                    obj.delegates.append (self)
                    toConnectInChild[obj]+= ['read', 'write']
                toConnect.update (toConnectInChild)
            
            xmlObj= xmlObj.next

        # save/discard buttons
        hbox= cimarron.skin.HBox (parent=vbox)
        save= cimarron.skin.Button (
            parent= hbox,
            label= 'Save',
            onAction= self.save,
            )
        discard= cimarron.skin.Button (
            parent= hbox,
            label= 'Discard',
            onAction= self.discard,
            )

        # we do (connect) what we can
        toConnect= self._connect (toConnect)
        
        return (self, toConnect)
    fromXmlObj = classmethod(fromXmlObj)
