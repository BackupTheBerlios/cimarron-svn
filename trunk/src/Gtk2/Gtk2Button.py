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
import types
from Generic.Button import Button
from Gtk2Control import Gtk2Control

class Gtk2Button (Button, Gtk2Control):
    _stocks = dict([(k[6:].lower(), v) for k, v in gtk.__dict__.items()
                  if k.startswith("STOCK_")])
    _rstocks = dict([(v, k) for k, v in _stocks.items()])

    def __init__ (self, **kw):
        if not hasattr(self,'_obj'):
            self._obj= gtk.Button()
            self._obj.set_property('can_default', True)
            self._label = None
            self._image = None
            self._stock = None
            
        super (Gtk2Button, self).__init__ (**kw)
       
        self._obj.connect ('clicked', self.__activate)

    def _doSetLabel (self, label):
        self._stock = None
        self._label = label
        self._balance()

    def _balance(self):
        for i in self._obj.get_children():
            self._obj.remove(i)
        if self._stock is None:
            self._obj.set_property('use_stock', False)
            if isinstance(self._label, types.StringTypes):
                self._label = gtk.Label(self._label)
                self._label.set_use_underline(True)
                self._label.set_use_markup(True)
                self._label.set_mnemonic_widget(self._obj)
            if isinstance(self._image, types.StringTypes):
                img = self._image
                self._image = gtk.Image()
                self._image.set_from_file(img)
            if self._label and self._image:
                hbox = gtk.HBox()
                hbox.add(self._image)
                hbox.add(self._label)
                self._obj.add(hbox)
            elif self._label:
                self._obj.add(self._label)
            elif self._image:
                self._obj.add(self._image)
            self._obj.show_all()
        else:
            self._obj.set_label(self._stock)
            self._obj.set_property('use_stock', True)
        
    def _doSetStockImage(self, image):
        self._stock = None
        self._image = gtk.Image()
        self._image.set_from_stock(self._stocks.get(image, None),
                                   gtk.ICON_SIZE_BUTTON)
        self._balance()
    def _doSetImage (self, image):
        self._stock = None
        self._image = image
        self._balance()
        
    def _doSetStock (self, type):
        self._stock = self._stocks.get(type, None)
        self._balance()
    def _doGetStock (self):
        return self._rstocks.get(self._obj.get_label(), None)

    def __activate(self, widget, *a):
        self.submit()

    def __focus_out(self, widget, *a):
        pass
