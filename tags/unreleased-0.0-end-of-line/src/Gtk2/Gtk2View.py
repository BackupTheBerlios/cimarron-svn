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

from Generic.View import View
from Generic.Window import Window
import gtk

def deferredmethod(do_this):
    def dm(self, *a, **kw):
        if not self._defer ():
            do_this(self, *a, **kw)
        else:
            self._queuedMethods.append((do_this, a, kw))
    return dm

class Gtk2View(View):
    _tooltips = gtk.Tooltips()
    _watch = gtk.gdk.Cursor (gtk.gdk.WATCH)
    def __init__ (self, **kw):
        self._queuedMethods = []
        super(Gtk2View, self).__init__(**kw)
        self._defer= self.isHidden
        
    def _doFocus(self):
        self._obj.grab_focus()
    def _doHide(self):
        self._obj.hide()
    def _doShow(self):
        self._obj.show()
        for (function, args, kwargs) in self._queuedMethods:
            function (self, *args, **kwargs)
    def _doDisable(self):
        self._obj.set_sensitive(False)
    def _doEnable(self):
        self._obj.set_sensitive(True)
    def _doBusy(self):
        if self._obj.window:
            self._obj.window.set_cursor(self._watch)
    def _doIdle(self):
        if self._obj.window:
            self._obj.window.set_cursor(None)
    def _doSetTip(self, tip):
        Gtk2View._tooltips.set_tip(self._obj, tip)

    def _doSetSizeRequest(self, x, y):
        self._obj.set_size_request(x, y)
    def _doGetSizeRequest(self):
        size = self._obj.get_size_request()
        if size == (-1, -1):
            return None
        return size
