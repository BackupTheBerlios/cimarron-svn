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
# Debug.sections.append ('Gtk2Notebook')

from Generic.Notebook import Notebook
from Gtk2CompositeView import Gtk2CompositeView
import gtk
import types
from Gtk2View import deferredmethod

class Gtk2Notebook(Notebook, Gtk2CompositeView):
    def __init__(self, **kw):
        if not hasattr(self, '_obj'):
            self._obj = gtk.Notebook()
            self._obj.popup_enable()
            self._obj.set_scrollable(True)
        super(Gtk2Notebook, self).__init__(**kw)

    def _doInsertPage(self, pos, child, label, menu):
        if isinstance(label, types.StringTypes):
            label = gtk.Label(label)
        if isinstance(menu, types.StringTypes):
            menu = gtk.Label(menu)

        self._obj.insert_page_menu(child._obj, label, menu, pos)

    def _doNextPage(self):
        self._obj.next_page()
    _doNextPage= deferredmethod (_doNextPage)
    def _doPrevPage(self):
        self._obj.prev_page()
    _doPrevPage= deferredmethod (_doPrevPage)
    def _doChangePage(self, n):
        self._obj.set_current_page(n)
    _doChangePage= deferredmethod (_doChangePage)

    # _doInsertPage() already took care of it
    # if not, you shouldn't be calling addChild()/setParent()
    def _doAddChild (self, child):
        self.debug ('dummy add child')
        pass
    def _doRemoveChild (self, child):
        self.debug ('dummy remove child')
        pass
