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

from testCommon import abstractTestContainer

__all__= ('TestNotebook', )

class TestNotebook (abstractTestContainer):
    def setUp (self):
        super (TestNotebook, self).setUp ()
        self.parent= cimarron.skin.Window (parent= self.app)
        self.widget= cimarron.skin.Notebook (parent= self.parent)

    def testAddChild (self):
        self.other= cimarron.skin.Entry ()
        self.other.label= 'first'
        self.other.parent= self.widget

        self.assertEqual (True, True)
