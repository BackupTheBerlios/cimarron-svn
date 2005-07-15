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
from fvl.cimarron import skin

__all__ = ('TestHelloWorld',)

class TestHelloWorld(unittest.TestCase):
    def setUp(self):
        self.app = skin.Application()
    def testSkinArgv(self):
        self.assertEqual(skin.__name__, 'fvl.cimarron.skins.gtk2')
    def testWindow(self):
        self.win = skin.Window()
    def testWindowParent(self):
        self.win = skin.Window(parent=self.app)
        self.assertEqual(self.app, self.win.parent)
        self.assertEqual(list(self.app.children), [self.win])
    def testWindowTitle(self):
        self.win = skin.Window(parent=self.app, title='hello')
        self.assertEqual(self.win.title, 'hello')
    def testLabel(self):
        self.testWindowTitle()
        self.label = skin.Label(text='Hello, World!', parent=self.win)
        self.assertEqual(self.label.text, 'Hello, World!')
        self.assertEqual(self.win, self.label.parent)

if __name__ == '__main__':
    unittest.main()
