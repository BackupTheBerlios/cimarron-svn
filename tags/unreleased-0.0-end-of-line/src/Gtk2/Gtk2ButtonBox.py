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

import gtk
from Generic.ButtonBox import ButtonBox
from Gtk2Box import Gtk2Box

class Gtk2ButtonBox(ButtonBox, Gtk2Box):
    __layout_dict = { 'default': gtk.BUTTONBOX_DEFAULT_STYLE,
                      'edge': gtk.BUTTONBOX_EDGE,
                      'end': gtk.BUTTONBOX_END,
                      'spread': gtk.BUTTONBOX_SPREAD,
                      'start': gtk.BUTTONBOX_START }
    __layouts = ('default', 'edge', 'end', 'spread', 'start')

    def _doSetLayout(self, layout_style):
        layout = self.__layout_dict.get(layout_style, None)
        self._obj.set_layout(layout)

    def _doGetLayout(self):
        return self.__layouts[self._obj.get_layout()]

    def _doSetMinChildSize(self, min_width, min_height):
        sp=self._obj.set_property
        sp('child-min-width', min_width)
        sp('child-min-height', min_height)

    def _doGetMinChildSize(self):
        gp = self._obj.get_property
        return (gp('child-min-width', 'child-min-height'))
    
    def _doSetChildSecondary(self, child, is_secondary):
        self._obj.set_child_secondary(self, child._obj, is_secondary)
    def _doGetChildSecondary(self, child):
        return child._obj.get_property('secondary')

    def _doSetInternalPadding(self, xpad, ypad):
        sp = self._obj.set_property
        sp('child-internal-pad-x', xpad)
        sp('child-internal-pad-y', ypad)
    def _doGetInternalPadding(self):
        gp = self._obj.get_property
        return (gp('child-internal-pad-x'), gp('child-internal-pad-y'))
