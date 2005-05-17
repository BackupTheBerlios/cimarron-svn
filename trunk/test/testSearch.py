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

from testCommon import abstractTestControl
from testGrid import Person

__all__=('TestSearch',)

class PersonSearch (cimarron.controllers.SearchEntry):
    def search (self, values):
        name, surname= values[:2]
        ans= []

        for i in self.data:
            found= False
            if name is not None:
                found= name in i.name
            if surname is not None:
                found= found and surname in i.surname

            if found:
                ans.append (i)

        return ans

class TestSearch (abstractTestControl):
    def setUp (self):
        super (TestSearch, self).setUp ()
        self.parent = self.win = cimarron.skin.Window(title='Test', parent=self.app)
        columns= (
            cimarron.skin.Column (name='Nombre', read=Person.getName, write=Person.setName),
            cimarron.skin.Column (name='Apellido', read=Person.getSurname, write=Person.setSurname),
            )
        self.widget= PersonSearch (
            parent= self.parent,
            columns= columns,
            )
        self.data= [
            Person ('jose', 'perez'),
            Person ('marcos', 'dione'),
            Person ('john', 'lenton'),
            Person ('pedro', 'dargenio'),
            ]
        self.value= self.widget.value= self.data[0]

    def testNoneInEmptyFound (self):
        # here we 'plant' the data, but real Search's will fetch its own data
        self.widget.data= []
        self.widget.doSearch ()
        self.assertEqual (self.widget.value, None)

    def testNoneMatchesFound (self):
        # here we 'plant' the data, but real Search's will fetch its own data
        self.widget.data= self.data
        searchingValues= (
            ('martin', ''),
            ('', 'rezk'),
            )

        for i in xrange (len (searchingValues)):
            for j in xrange (len (searchingValues[i])):
                self.widget.entries[j].value= searchingValues[i][j]
            self.widget.doSearch ()
            self.assertEqual (self.widget.value, None)

    def testOneFound (self):
        self.widget.data= self.data
        searchingValues= (
            ('jos', ''),
            ('', 'pe'),
            ('m', ''),
            ('', 'dio'),
            ('john', ''),
            ('', 'lenton'),
            ('p', ''),
            ('', 'da'),
            )
        for i in xrange (len (searchingValues)):
            for j in xrange (len (searchingValues[i])):
                self.widget.entries[j].value= searchingValues[i][j]
            self.widget.doSearch ()
            self.assertEqual (self.widget.value, self.data[i/2])

    def testOnAction (self):
        self.widget.data= self.data
        super (TestSearch, self).testOnAction ()
