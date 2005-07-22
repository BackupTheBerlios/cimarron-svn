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

from fvl import cimarron
from fvl.cimarron.controllers import CRUDController, Editor

from testCommon import abstractTestControl
from testController import TestController
from model.person import Person
from model import Store

__all__ = ('TestCRUDController',
           'TestEditor',
           )

class TestCRUDController (TestController):
    def setUp (self):
        super (TestCRUDController, self).setUp ()
        self.store = Store()
        self.widget= CRUDController.fromXmlFile ('test/testCrud.xml')
        self.widget.parent= self.parent= self.app
        self.widget.store = self.store
        person= Person.__values__[0]
        self.setUpControl (target= person, attr=None)
        
    def testRefresh (self):
        # self.widget.target= self.target
        self.assertEqual (self.widget.editors[0].target, self.target)
        self.assertEqual (self.widget.editors[0].value, self.target)
        self.assertEqual (self.widget.editors[1].target, self.target)
        self.assertEqual (self.widget.editors[1].value, self.target.addresses)

    def testSearch (self):
        # too specific stuff! fix if ui changes!
        vbox= self.widget.note.children[0]
        search= vbox.children[1]
        nameEntry= search.entries[0]
        surnameEntry= search.entries[1]
        searchButton= search.h.children[-1]
        personEditor= self.widget.editors[0]
        addrEditor= self.widget.editors[1]

        # test them, just in case
        self.assert_ (isinstance (vbox, cimarron.skin.VBox))
        self.assert_ (isinstance (search, cimarron.skin.SearchEntry))
        self.assert_ (isinstance (nameEntry, cimarron.skin.Entry))
        self.assert_ (isinstance (surnameEntry, cimarron.skin.Entry))
        self.assert_ (isinstance (searchButton, cimarron.skin.Button))
        self.assert_ (isinstance (personEditor, cimarron.skin.Editor))
        self.assert_ (isinstance (addrEditor, cimarron.skin.Editor))

        # back to `normality'
        nameEntry.commitValue ('Freeman')
        searchButton.onAction ()

        # tests
        # print surnameEntry
        # self.assertEqual (surnameEntry.value, 'Newman')
        self.assertEqual (personEditor.target, self.target)
        self.assertEqual (personEditor.value, self.target)
        self.assertEqual (addrEditor.target, self.target)
        self.assertEqual (addrEditor.value, getattr (self.target, addrEditor.attribute))


class TestEditor(TestController):
    def setUp(self):
        super (TestEditor, self).setUp()
        self.store = Store()
        self.parent= cimarron.skin.Window ()
        # self.widget = cimarron.skin.Editor(store=self.store,
        #                                    attributes=['name', 'surname'])
        self.widget= Editor.fromXmlFile ('test/editor.xml')
        self.widget.parent= self.parent
        self.widget.store = self.store
        self.entry= self.widget.entries.children[0]

        self.setUpControl(target=Person('Marcos', 'Dione'), attr=None)

    def testLabel(self):
        # assign a label attribute
        # and check it ends up in the outer container
        # (for putting it in a Notebook)
        pass

    def testRefresh (self):
        # self.widget.target= self.target
        self.assertEqual (self.entry.target, self.target)
        self.assertEqual (self.entry.value,
                          getattr (self.value, self.entry.attribute))

    def testNothing(self):
        pass
