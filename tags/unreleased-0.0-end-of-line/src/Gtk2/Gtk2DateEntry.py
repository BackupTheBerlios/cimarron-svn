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

from Utils import Debug
# Debug.sections.append ('Gtk2DateEntry')

import mx.DateTime
import gtk

from Gtk2TextEntry import Gtk2TextEntry
from Generic.DateEntry import DateEntry, _

class Gtk2DateEntry(DateEntry, Gtk2TextEntry):
    _known_types = { 65362: mx.DateTime.RelativeDate(days=1),
                     65364: mx.DateTime.RelativeDate(days=-1),
                     65365: mx.DateTime.RelativeDate(months=1),
                     65366: mx.DateTime.RelativeDate(months=-1),
                     '65365': mx.DateTime.RelativeDate(years=1),
                     '65366': mx.DateTime.RelativeDate(years=-1),
                     }
    _calendar_img = None
    def __init__(self, **kw):
        if self._calendar_img is None:
            f = self.getConfigAsString('calendar_image')
            self.__class__._calendar_img = gtk.gdk.pixbuf_new_from_file(f)

        if not hasattr(self, '_entry'):
            entry = self._entry = gtk.Entry()
            entry.set_width_chars(13)

        if not hasattr(self, '_label'):
            self._label = gtk.Label('')

        if not hasattr(self, '_obj'):
            self._obj = gtk.EventBox()
            if not hasattr(self, '_vbox'):
                button = gtk.Button()
                i = gtk.Image()
                i.set_from_pixbuf(self._calendar_img)
                button.add(i)
                button.connect('clicked', self._popup_dialog)
                vbox = gtk.VBox()
                vbox.pack_start(entry, False, True)
                vbox.pack_start(self._label, False, True)
                hbox = gtk.HBox()
                hbox.pack_start(vbox, True, True)
                hbox.pack_start(button, False, False)
                self._vbox = gtk.VBox()
                self._vbox.pack_start(hbox, False, False)
            self._obj.add(self._vbox)

        if not hasattr(self, '_ctrl'):
            self._ctrl = False

        if not hasattr(self.__class__, '_dia'):
            dia = gtk.Dialog(_("Select a date"),
                             None, 0,
                             (gtk.STOCK_CANCEL, gtk.RESPONSE_CANCEL,
                              gtk.STOCK_OK, gtk.RESPONSE_OK))
            dia.set_position(gtk.WIN_POS_MOUSE)
            dia.set_default_response(gtk.RESPONSE_OK)
            cal = gtk.Calendar()
            cal.connect('day_selected_double_click',
                        lambda *a: dia.response(gtk.RESPONSE_OK))
            dia.vbox.add(cal)
            self.__class__._dia = dia
            self.__class__._cal = cal
        
        # super(Gtk2DateEntry, self).__init__(**kw)
        self._processArgs(Gtk2DateEntry, kw)

        self._entry.connect('key_press_event', self._change_value)
        self._entry.connect('key_release_event', self._release)

    def _change_value(self, widget, event):
        self.debug ('')
        kv = event.keyval
        if kv == 65507:
            self.debug ('_ctrl True')
            self._ctrl = True
        else:
            if self._ctrl is True:
                kv = str(kv)
                self.debug ('kv: %s' % kv)
            if kv in self._known_types.keys():
                self.debug ('setting value %s' % (self._value + self._known_types[kv]))
                self.setValue(self._value + self._known_types[kv])
                return True
        
        self.debug ('')
        return False

    def _release(self, widget, event):
        if event.keyval == 65507:
            self.debug ('_ctrl False')
            self._ctrl = False

    def _popup_dialog(self, *a):
        dia = self._dia
        cal = self._cal
        win = self.getWindow()
        win.disable()
        win.busy()
        win.pushStatus(_('Waiting for input in calendar'))
        value = self.getValue()
        dia.set_parent_window(self.getWindow()._obj.window)
        dia.show_all()
        cal.select_month(value.month-1, value.year)
        cal.select_day(value.day)
        cal.grab_focus()
        dia.action_area.get_children()[0].grab_default()
        response = dia.run()
        if response == gtk.RESPONSE_OK:
            (Y, M, D) = cal.get_date()
            M += 1
            self.setValue(mx.DateTime.Date(Y, M, D))
        else:
            self.rejectInput()
        dia.hide_all()
        win.enable()
        win.idle()
        win.popStatus()
        self._entry.grab_focus()

    def _doSetValue(self, value):
        self.debug ('setting value %s' % value, parents=5)
        super(Gtk2DateEntry, self)._doSetValue(value)
        if self._entry.is_focus():
            self._entry.select_region(0, -1)
        self._label.set_markup('<span size="x-small">%s</span>' % (self.getValue().strftime(_('%a %b %e, %Y')),))

