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
from testCommon import abstractTestWidget, abstractTestContainer

__all__ = ('TestWindow',
           )

class TestWindow(abstractTestContainer, abstractTestWidget):
    def setUp(self):
        super(TestWindow, self).setUp()
        self.widget = self.win = cimarron.skin.Window(title='Test',
                                                      parent=self.app)
        self.otherwin = cimarron.skin.Window(parent=self.app)
        self.parent = self.app

    def testWindowTitle(self):
        self.assertEqual(self.win.title, 'Test')
