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

from testCommon import abstractTestControl
from model.country import Country

__all__ = ('TestEntrySomeMore',
           )

class TestEntry(abstractTestControl):
    def setUp(self):
        super(TestEntry, self).setUp()
        self.win = cimarron.skin.Window(title='Test', parent=self.app)
        self.parent = cimarron.skin.VBox (parent= self.win)
        self.widget = self.entry = cimarron.skin.Entry(parent=self.parent)
        self.setUpControl()

    def testSetValue (self):
        raise NotImplementedError, 'you should subclass testEntry'

    def testEntryNotDirtyJustBecauseEmpty(self):
        self.widget.commitValue(None)
        self.assert_(not self.widget.dirty())

#    def testValueFromNone(self):
#        self.assertRaises(TypeError, self.widget.newTarget, None)

class TestEntrySomeMore(unittest.TestCase):
    def setUp(self):
        self.target = Country(name='Gergovia')
        self.app = cimarron.skin.Application()
        self.win = cimarron.skin.Window(title='Test', parent=self.app)
        self.widget = self.entry = cimarron.skin.Entry(parent=self.win,
                                                       target=self.target,
                                                       attribute='name')
    def testNewTargetCalledUponInit(self):
        self.assertEqual(self.widget.value, self.target.name)
        
    def testValueReachesModelOnActivate(self):
        self.widget.value = 'Paysandu'
        self.widget._activate()
        self.assertEqual(self.widget.value, self.target.name)
