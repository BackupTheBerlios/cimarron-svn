# -*- python -*- coding: ISO-8859-1 -*-
# Copyright 2004 Fundacion Via Libre
#
# This file is part of PAPO.
# 
# PAPO is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
# 
# PAPO is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with PAPO; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA

from Generic.CompositeView import CompositeView
from Gtk2View import Gtk2View

class Gtk2CompositeView(CompositeView, Gtk2View):
    def _doAddChild(self, child):
        self._obj.add(child._obj)

    def _doRemoveChild(self, child):
        self._obj.remove(child._obj)

    def _doSetBorderWidth(self, width):
        self._obj.set_border_width(width)
    def _doGetBorderWidth(self):
        return self._obj.get_border_width()
    
