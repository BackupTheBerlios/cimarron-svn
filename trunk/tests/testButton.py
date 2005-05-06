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

__all__ = ('TestButton',
           'TestCheckbox',
           )

class TestButton(abstractTestControl):
    def setUp(self):
        super(TestButton, self).setUp()
        self.win = cimarron.skin.Window(title='Test', parent=self.app)
        self.parent = cimarron.skin.VBox (parent= self.win)
        self.widget = cimarron.skin.Button(label='Click me', parent=self.parent)
        self.setUpControl()

    def testLabel(self):
        self.assertEqual(self.widget.label, 'Click me')

    def testSetLabel (self):
        raise NotImplementedError

class TestCheckbox(TestButton):
    def setUp(self):
        super(TestCheckbox, self).setUp()
        self.widget = cimarron.skin.Checkbox(label='Click me', parent=self.parent)
        self.setUpControl()

    def testChecked(self):
        self.widget.checked = True
        self.assertEqual(self.widget.checked, True)
        self.widget.checked = False
        self.assertEqual(self.widget.checked, False)
