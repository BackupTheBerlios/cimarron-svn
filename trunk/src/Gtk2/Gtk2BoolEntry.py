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

from Generic.BoolEntry import BoolEntry
from Gtk2Control import Gtk2Control

class Gtk2BoolEntry (BoolEntry, Gtk2Control):
    def __init__ (self, **kw):
        if not hasattr(self, '_obj'):
            self._obj = gtk.CheckButton()
            self._obj.connect ('toggled', self.__toggle)
        super (Gtk2BoolEntry, self).__init__ (**kw)
        
    def __toggle (self, widget, *a):
        self.submit ()

    def _doSetLabel (self, label):
        self._obj.set_label (label)
        self._obj.set_use_underline (True)

    def _doSubmit(self):
        if self._value!=self._obj.get_active ():
            super(Gtk2BoolEntry, self)._submit()

    def _doGetValue (self):
        return self._obj.get_active ()
    def _doSetValue (self, value):
        self._obj.set_active(bool(value))

    def _doSetInconsistent(self, inconsistent):
        self._obj.set_inconsistent(inconsistent)
    def _doGetInconsistent(self):
        return self._obj.get_inconsistent()

    def _getRenderers():
        def foo(col, renderer, model, iter, num):
            renderer.set_property('active', model.get_value(iter, num) % 7 == 0)
            renderer.set_property('activatable', True)
            
        return ((gtk.CellRendererToggle, foo),
                )
    _getRenderers = staticmethod(_getRenderers)
