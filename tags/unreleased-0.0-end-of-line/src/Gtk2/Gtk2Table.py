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
from Generic.Table import Table
from Gtk2CompositeView import Gtk2CompositeView

class Gtk2Table(Table,Gtk2CompositeView):
    def __init__(self, **kw):
        if not hasattr(self, '_obj'):
            self._obj = gtk.Table()
        super(Gtk2Table, self).__init__(**kw)
      
    def _doAttach(self, widget, left, right, top, bottom):
        self._obj.attach(widget._obj, left, right, top, bottom)
   
    def _doSetColSpacings(self, spacing):
        self._obj.set_col_spacings(spacing)
    def _doGetColSpacings(self):
        return self._obj.get_col_spacings()
    def _doSetColSpacing(self, col, spacing):
        self._obj.set_col_spacing(col, spacing)
    def _doGetColSpacing(self, col):
        return self._obj.get_col_spacing(col)
    def _doGetDefaultColSpacing(self):
        return self._obj.get_default_col_spacing()
   
    def _doSetRowSpacings(self, spacing):
        self._obj.set_row_spacings(spacing)
    def _doGetRowSpacings(self):
        return self._obj.get_row_spacings()
    def _doSetRowSpacing(self, row, spacing):
        self._obj.set_row_spacing(row, spacing)
    def _doGetRowSpacing(self, row):
        return self._obj.get_row_spacing(row)
    def _doGetDefaultRowSpacing(self):
        return self._obj.get_default_row_spacing()
        
    def _doSetHomogeneous(self, homogeneous):
        self._obj.set_homogeneous(homogeneous)
    def _doGetHomogeneous(self):
        return self._obj.get_homogeneous()
        
    def _doResize(self, rows, columns):
        self._obj.resize(rows, columns)
