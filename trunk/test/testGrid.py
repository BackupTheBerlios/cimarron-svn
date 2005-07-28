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

import unittest

from fvl import cimarron
from fvl.cimarron.skin import Column, Window, Grid, SelectionGrid

from model.person import Person
from fvl.cimarron.model import Model

from testCommon import abstractTestControl

__all__ = ('TestSelectionGrid', 'TestGrid', 'TestGridInit')

class DummyTarget(Model):
    def __init__(self, dummy):
        self.dummy = dummy

class TestGridInit(unittest.TestCase):
    """
    Test we can create empty Grids
    """
    def testGrid(self):
        grid = Grid()
        self.assertEqual(list(grid.columns), [])
    def testSelectionGrid(self):
        grid = SelectionGrid()
        self.assertEqual(list(grid.data), [])

class TestGrid(abstractTestControl):
    def setUp(self):
        super (TestGrid, self).setUp()
        self.list = [Person('jose', 'perez'),
                     Person('marcos', 'dione'),
                     Person('john', 'lenton'),
                     ]
        columns = (Column(name='Nombre', attribute='name'),
                   Column(name='Apellido', attribute='surname'),
                   )

        self.parent = self.window = Window(title='Test', parent=self.app)
        self.widget = self.grid = Grid(parent = self.parent,
                                       columns = columns,
                                       cls = Person,
                                       )

        target = DummyTarget(self.list)
        self.setUpControl(target=target, attr='dummy')

    def testIndex(self):
        for i in xrange (len(self.widget.value)):
            self.widget.index = i
            self.assertEqual(self.widget.index, i)
            self.assertEqual(self.value[i], self.widget.value[i])

    def testWrite(self):
        self.widget._cell_edited(None, 0, 'juan', 0)
        self.widget.index = 0
        try:
            self.assertEqual(self.widget.value[0].name, 'juan')
        except(TypeError, IndexError):
            self.assertEqual(self.widget.new.name, 'juan')

    def testValueIsTargetWhenNoAttr(self):
        self.target = self.list
        super (TestGrid, self).testValueIsTargetWhenNoAttr()


class TestSelectionGrid(abstractTestControl):
    def setUp(self):
        super (TestSelectionGrid, self).setUp()
        self.list = [Person('jose', 'perez'),
                     Person('marcos', 'dione'),
                     Person('john', 'lenton'),
                     ]
        columns = (Column(name='Nombre', attribute='name'),
                   Column(name='Apellido', attribute='surname'),
                   )

        self.parent = self.window = Window(title='Test', parent=self.app)
        self.widget = self.grid = SelectionGrid(parent = self.parent,
                                                columns = columns,
                                                data = self.list,
                                                onAction=self.dummyAction,
                                                )

        target = DummyTarget(self.list[0])
        self.setUpControl(target=target, attr='dummy')

    def testIndex(self):
        for i in xrange (len(self.list)):
            self.widget.index = i
            self.assertEqual(self.list[i], self.widget.value)

    def testValue(self):
        for i in xrange (len(self.list)):
            self.widget.value = self.list[i]
            self.assertEqual(self.list[i], self.widget.value)

    def testNoValue(self):
        self.widget.data = []
        self.widget.value = None
        self.assert_(self.widget.value is None)

    def testValueIsTargetWhenNoAttr(self):
        self.setUpControl(target=self.list[0], attr=None)
        self.widget.index = 0
        super (TestSelectionGrid, self).testValueIsTargetWhenNoAttr()

    def testNoTarget(self):
        self.setUpControl(target=None, attr=None)
        self.testIndex()
        self.testValue()

    def testDoubleClickSelection(self):
        self.widget.index=1
        self.widget._double_click(widget=self.widget._concreteWidget)
        self.assertEquals(self.dummyDCValue,self.widget.data[self.widget.index],
                                    """Double click did not sent the values""") 

    def dummyAction(self,sender): #action to test double click functioning
        self.dummyDCValue = sender.data[sender.index]
