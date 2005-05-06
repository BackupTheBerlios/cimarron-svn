# -*- coding: utf-8 -*-
#
# Copyright 2003 Fundación Via Libre
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

import unittest
from papo import cimarron
from testCommon import abstractTestControl

__all__= ('TestGrid', 'Person')


class Person (object):
    def __init__ (self, name, surname):
        self.setName (name)
        self.setSurname (surname)

    def getName (self):
        return self.__name
    def setName (self, name):
        self.__name= name
    name= property (getName, setName)

    def getSurname (self):
        return self.__surname
    def setSurname (self, sn):
        self.__surname= sn
    surname= property (getSurname, setSurname)

class TestGrid (abstractTestControl):
    def setUp (self):
        super (TestGrid, self).setUp ()
        self.model= [
            Person ('jose', 'perez'),
            Person ('marcos', 'dione'),
            Person ('john', 'lenton'),
            ]
        columns= (
            cimarron.skin.Column (name='Nombre', read=Person.getName, write=Person.setName),
            cimarron.skin.Column (name='Apellido', read=Person.getSurname, write=Person.setSurname),
            )

        self.parent = self.win = cimarron.skin.Window(title='Test', parent=self.app)
        self.widget= self.grid= cimarron.skin.Grid (
            parent= self.parent,
            columns= columns,
            rows= 5,
            )

        # so testValue passes
        self.value= None
        self.widget.data= self.model

    def testIndex (self):
        for i in xrange (len (self.model)):
            self.widget.index= i
            self.assertEqual (self.model[i], self.widget.value)

    def testValue (self):
        for i in xrange (len (self.model)):
            self.widget.value= self.model[i]
            self.assertEqual (self.model[i], self.widget.value)

    def testNoValue (self):
        self.widget.data = []
        self.widget.value= None
        self.assertEqual (self.widget.value, None)

    def testWrite (self):
        # self.widget.entries[0, 0]._widget.set_text ('juan')
        self.widget.entries[0, 0].value= 'juan'
        self.widget.entries[0, 0].onAction ()
        self.widget.index= 0
        self.assertEqual (self.widget.value.name, 'juan')
