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

from Gtk2StatefulControl import Gtk2StatefulControl
from Generic.TextEntry import TextEntry
import gtk,sys

class Gtk2TextEntry(TextEntry, Gtk2StatefulControl):
    _bar = gtk.gdk.Cursor (gtk.gdk.XTERM)
    __obligs = {'_obj': gtk.Entry}
    def __init__(self, **kw):
        self._processArgs(Gtk2TextEntry, kw)
        if not hasattr(self, '_entry'):
            self._entry = self._obj
        entry = self._entry
        
        entry.connect('activate', self._activate)
        entry.connect('focus_out_event', self._focusOut)
        entry.connect('key_press_event', self._keyPress)

    def _activate(self, widget, *a):
        return self.submit()
    def _focusOut(self, widget, *a):
        return self.submit()

    def _keyPress(self, widget, event, *a):
        if event.string == '\x1b':
            self.rejectInput()

    def _doSubmit(self):
        if self._value != self._entry.get_text():
            super(Gtk2TextEntry, self)._submit()

    def _doSetValue(self, value):
        self._entry.set_text(unicode(value))

    def _doGetValue(self):
        return self._entry.get_text()

    def _doSetMaxLength(self, max_len):
        self._entry.set_max_length(max_len)
    def _doGetMaxLength(self):
        return self._entry.get_max_length()

    def _doSetEditable(self, editable):
        self._entry.set_editable(editable)
    def _doGetEditable(self):
        return self._entry.get_editable()

    def _doFrame(self):
        self._entry.set_has_frame(True)
    def _doUnframe(self):
        self._entry.set_has_frame(False)
    def _doHasFrame(self):
        return self._entry.get_has_frame()

    def _doBusy(self):
        self._entry.window.get_children()[0].set_cursor(self._watch)
        super(Gtk2TextEntry, self)._doBusy()

    def _doIdle(self):
        self._entry.window.get_children()[0].set_cursor(self._bar)
        super(Gtk2TextEntry, self)._doIdle()

    def _doFocus(self):
        super(Gtk2TextEntry, self)._doFocus()
        self._entry.select_region(0, -1)

    def _getRenderers():
        def bar(col, renderer, model, iter, num):
            renderer.set_property('text', model.get_value(iter, num).upper())
            renderer.set_property('editable', True)
        def foo(col, renderer, model, iter, num):
            renderer.set_property('text', model.get_value(iter, num))
            renderer.set_property('editable', True)
            
        return ((gtk.CellRendererText, foo),
                (gtk.CellRendererText, bar),
                )
    _getRenderers = staticmethod(_getRenderers)
