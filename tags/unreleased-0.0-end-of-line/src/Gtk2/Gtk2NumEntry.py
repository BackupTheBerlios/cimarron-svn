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

from Gtk2TextEntry import Gtk2TextEntry
from Generic.NumEntry import NumEntry
import gtk

class Gtk2NumEntry(NumEntry, Gtk2TextEntry):
    def __init__(self, **kw):
        if not hasattr(self, '_entry'):
            self._entry = gtk.SpinButton()
            self._obj = self._entry
        super(Gtk2NumEntry, self).__init__(**kw)

    def _doSetRange(self, min_num, max_num):
        self._entry.set_range(min_num, max_num)
    def _doGetRange(self):
        return self._entry.get_range()

    def _doSetIncrements(self, pri, sec):
        self._entry.set_increments(pri, sec)
    def _doGetIncrements(self):
        return self._entry.get_increments()

    def _doSetDigits(self, digits):
        self._entry.set_digits(digits)
    def _doGetDigits(self):
        return self._entry.get_digits()
