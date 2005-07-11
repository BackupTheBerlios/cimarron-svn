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

__all__=('TestSearch',)

class TestSearch(abstractTestControl):
    def setUp(self):
        super (TestSearch, self).setUp()
        self.parent = self.win = cimarron.skin.Window(title='Test', parent=self.app)
        columns = (
            cimarron.skin.Column(name='Nombre', attribute='name'),
            cimarron.skin.Column(name='Apellido', attribute='surname'),
            )
        self.widget = cimarron.skin.SearchEntry(
            parent = self.parent,
            columns = columns,
            searcher = Person,
            )
        Person.__values__ = self.data = [
            Person('jose', 'perez'),
            Person('marcos', 'dione'),
            Person('john', 'lenton'),
            Person('pedro', 'dargenio'),
            ]
        
        self.setUpControl(target=self.data[0], attr=None)

    def testNoneInEmptyFound(self):
        # here we 'plant' the data, but real Search's will fetch its own data
        # self.widget.data = []
        Person.__values__ = []
        self.widget.search()
        self.assertEqual(self.widget.value, None)

    def testNoneMatchesFound(self):
        # here we 'plant' the data, but real Search's will fetch its own data
        # self.widget.data = self.data
        Person.__values__ = self.data
        searchingValues = (
            {'name':'martin', 'surname':''},
            {'name':'', 'surname':'rezk'},
            )

        for i in xrange (len(searchingValues)):
            j = 0
            for k in searchingValues[i].keys():
                self.widget.entries[j].value = searchingValues[i][k]
                j =+ 1
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
        for i in xrange (len(searchingValues)):
            j = 0
            for k in searchingValues[i].keys():
                self.widget.entries[j].value = searchingValues[i][k]
                j += 1
            self.widget.search()
            self.assertEqual(self.widget.value, self.data[i/2])

    def testOnAction(self):
        self.widget.data = self.data
        super (TestSearch, self).testOnAction()
