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
import sys
from cStringIO import StringIO

from fvl import cimarron
from testCommon import abstractTestContainer

__all__ = ('TestBoxes',
           )

class TestBoxes (abstractTestContainer):
    def setUp (self):
        super (TestBoxes, self).setUp ()
        self.parent= self.window= cimarron.skin.Window (parent=self.app)
        self.widget= self.vbox= cimarron.skin.VBox (parent=self.parent)

    def testVisual (self):
        d= cimarron.skin.Button (parent=self.widget, label='Looking good')
        self.assertEqual (d.parent, self.widget)
        self.other= cimarron.skin.HBox (parent= self.widget)

        b= cimarron.skin.Button (label='Looking so-so')
        b.parent= self.other
        # self.app.Button (parent= self.other, label='Looking so-so')
        cimarron.skin.Button (parent= self.other, label='Looking bad')

        # self.app.show ()
        # self.app.run ()

    def testReparenting1 (self):
        b= cimarron.skin.Button (parent= self.widget, label='reparented 1')
        def test():
            b.parent= self.widget

        self.assertRaises(ValueError, test)

    def testReparenting2 (self):
        b= cimarron.skin.Button (label='reparented 2')
        b.parent= None

    def testReparenting3 (self):
        b= cimarron.skin.Button (parent= self.widget, label='reparented 3')

        def test():
            b.parent = None
        self.assertRaises (NotImplementedError, test)


    def testReparenting4 (self):
        b= cimarron.skin.Button (label='reparented 4')
        b.parent= self.widget
        self.assertEqual (b.parent, self.widget)

    def testReparenting5 (self):
        b= cimarron.skin.Button (parent= self.widget, label='reparented 5')

        def test ():
            b.parent= self.window

        self.assertRaises (NotImplementedError, test)
