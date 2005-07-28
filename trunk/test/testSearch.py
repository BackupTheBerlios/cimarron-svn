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

from testCommon import abstractTestControl
from model.person import Person

__all__=('TestSearchEntry',)

class TestSearchEntry(abstractTestControl):
    def setUp(self):
        super (TestSearchEntry, self).setUp()
        self.parent = self.window = cimarron.skin.Window(title='Test', parent=self.app)
        self.columns = (
            cimarron.skin.Column(name='Nombre', attribute='name'),
            cimarron.skin.Column(name='Apellido', attribute='surname'),
            )
        self.widget = cimarron.skin.SearchEntry(
            parent = self.parent,
            columns = self.columns,
            searcher = Person,
            cls = Person,
            )
        Person.__values__ = self.data = [
            Person('jose', 'perez'),
            Person('marcos', 'dione'),
            Person('john', 'lenton'),
            Person('pedro', 'dargenio'),
            ]
        
        self.setUpControl(target=self.data[0], attr=None)

    def testNoneInEmptyFound(self):
        Person.__values__ = []
        self.widget.search()
        self.assertEqual(self.widget.value, None)

    def testNoneMatchesFound(self):
        Person.__values__ = self.data
        searchingValues = (
            {'name':'martin', 'surname':''},
            {'name':'', 'surname':'rezk'},
            )

        for index, value in enumerate(searchingValues):
            for j, key in enumerate(['name', 'surname']):
                self.widget.entries[j].value = searchingValues[index][key]
            self.widget.search()
            self.assertEqual(self.widget.value, None)

    def testOneFound(self):
        self.widget.data = self.data
        searchingValues = (
            {'name':'jos', 'surname':''},
            {'name':'', 'surname':'pe'},
            {'name':'m', 'surname':''},
            {'name':'', 'surname':'dio'},
            {'name':'john', 'surname':''},
            {'name':'', 'surname':'lenton'},
            {'name':'p', 'surname':''},
            {'name':'', 'surname':'da'},
            )
        for index, value in enumerate(searchingValues):
            for j, key in enumerate(['name', 'surname']):
                self.widget.entries[j].value = value[key]
                
            self.widget.search()
            
            # correct value
            self.assertEqual(self.widget.value, self.data[index/2])
            for j, column in enumerate(self.columns):
                # correct displayed values
                self.assertEqual(self.widget.entries[j].value, self.widget.value.getattr(column.attribute))

    def testOnAction(self):
        self.widget.data = self.data
        super (TestSearchEntry, self).testOnAction()
        

