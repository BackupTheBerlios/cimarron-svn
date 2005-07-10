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
from fvl.cimarron.model import Model

class testModel(unittest.TestCase):
    def setUp(self):
        self.m = Model()
    def testGetattr(self):
        self.m.foo = 3
        self.assertEqual(self.m.getattr('foo'), 3)
    def testSetattr(self):
        self.m.setattr('bar', Ellipsis)
        self.assertEqual(self.m.bar, Ellipsis)
    def testError(self):
        self.assertRaises(AttributeError, self.m.getattr, 'NO.SUCH.ATTRIBUTE')

class testTraversal(testModel):
    def setUp(self):
        testModel.setUp(self)
        self.m.c = type('C', (), {})()
    def testGet(self):
        self.m.c.foo = 15
        self.assertEqual(self.m.getattr('c.foo'), 15)
    def testSet(self):
        self.m.setattr('c.foo', Ellipsis)
        self.assertEqual(self.m.c.foo, Ellipsis)
    def testGetWithAttrs(self):
        self.m.callable = lambda x: x+x
        self.assertEqual(self.m.getattr('callable.X'), 'XX')
