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

from Generic.Image import Image
from Gtk2Misc import Gtk2Misc
import gtk

class Gtk2Image(Image, Gtk2Misc):
    _stocks = dict([(k[6:].lower(), v) for k, v in gtk.__dict__.items()
                  if k.startswith("STOCK_")])
    _sizes = dict([(k[10:].lower(), v) for k, v in gtk.__dict__.items()
                  if k.startswith("ICON_SIZE_")])
    def __init__(self, **kw):
        if not hasattr(self, '_obj'):
            self._obj = gtk.Image()
        super(Gtk2Image, self).__init__(**kw)
    def _doSetFromFile(self, file):
        self._obj.set_from_file(file)
    def _doSetFromStock(self, stock, size):
        stock = self._stocks[stock]
        size = self._sizes[size]
        self._obj.set_from_stock(stock, size)
    
