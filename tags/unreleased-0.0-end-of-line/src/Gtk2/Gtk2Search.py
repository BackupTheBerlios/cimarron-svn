# -*- python -*- coding ISO-8859-1 -*-
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
from Gtk2Label import Gtk2Label
from Gtk2SearchEntry import Gtk2SearchTextEntry
from Gtk2HBox import Gtk2HBox
from Gtk2VBox import Gtk2VBox
from Generic.Search import Search, BoxedSearch, HSearch, VSearch
import gtk, gobject

class Gtk2Search(Search, Gtk2StatefulControl):
    _watch_ptr = None
    def __init__(self, **kw):
        self._processArgs(Gtk2Search, kw)

        self._response = None
        self._row = None
        self._sortcol = None

        self._treeview = gtk.TreeView()
        self._treeview.set_rules_hint(True)
        self._treeview.set_enable_search(True)
        def cursor_changed(tv):
            tv.get_selection().set_mode(gtk.SELECTION_BROWSE)
            self._dia_ok_button.set_sensitive(True)
        def row_activated(tv, path, col):
            self._dia.response(gtk.RESPONSE_OK)
        def col_clicked(tvcol, n):
            self._treeview.set_search_column(n)
        self._treeview.connect('cursor-changed', cursor_changed)
        self._treeview.connect('row-activated', row_activated)
        
        self._buildDialog ()
        self._index= 0 
        
        super(Gtk2Search, self).__init__()

    def _buildDialog (self):
        self._dia = gtk.Dialog(_('Multiple objects found; please select one'),
                               None, 0,
                               (gtk.STOCK_CANCEL, gtk.RESPONSE_CANCEL,
                                gtk.STOCK_OK, gtk.RESPONSE_OK))
        self._dia.set_position(gtk.WIN_POS_MOUSE)
        self._dia.set_modal(True)
        self._dia.set_size_request(400,300)
        self._dia.set_default_response(gtk.RESPONSE_OK)
        self._dia.set_destroy_with_parent(True)

        self._dia_ok_button = self._dia.action_area.get_children()[0]

        sw = gtk.ScrolledWindow()
        sw.set_policy(gtk.POLICY_AUTOMATIC, gtk.POLICY_AUTOMATIC)
        sw.add(self._treeview)

        self._dia.vbox.pack_start(sw, True, True)
        self._progress = gtk.ProgressBar()
        self._progress.set_size_request(-1, 10)
        self._dia.vbox.pack_start(self._progress, False, False)

        def response(dia, rid):
            self._response = rid
        self._dia.connect('response', response)

    def _doAddChild (self, child):
        self._obj.add (child._obj)
        col = gtk.TreeViewColumn(child.getFinder ().label, child._renderer, text=(self._index+1))
        col.set_sort_column_id(self._index+1)
        col.set_resizable(True)
        col.set_reorderable(True)
        def col_clicked(tvcol, n):
            self._treeview.set_search_column(n)
        col.connect('clicked', col_clicked, self._index+1)
        self._treeview.append_column(col)
        self._index+= 1
            
    def _doChoose(self, found, entry):
        # arma un liststore
        self._store = gtk.ListStore(gobject.TYPE_PYOBJECT,
                                    *[gobject.TYPE_STRING for i in self._entries])
        # set sort if needed
        if self._sortcol is not None:
            self._store.set_sort_column_id(*self._sortcol)
        # set model
        self._treeview.set_model(self._store)
        # build ui
        self._dia.set_parent_window(self.getWindow()._obj.window)
        self._response = None
        self._dia_ok_button.set_sensitive(False)
        self._dia.show_all()
        gtk.gdk.set_xcursor(self._dia.window, "left_ptr_watch")

        finder= entry.getFinder ()
        entries= self._entries
        tot = found[0]
        got = 0
        n = 0
        self._progress.set_fraction(0)
        self._treeview.set_enable_search(False)
        self._treeview.set_headers_clickable(False)
        # fill the grid
        while tot > got and self._response is None:
            gtk.mainiteration()
            chunk = finder.fetchSlice(found, n)
            n += 1
            got += len(chunk)
            if not self._response:
                for i in chunk:
                    self._store.append([i]+[f.getFinder().getter(i) for f in entries])
                    gtk.mainiteration()
            self._progress.set_fraction(1.0*got/tot)
        self._treeview.set_headers_clickable(True)
        self._treeview.set_enable_search(True)
        self._dia.window.set_cursor(None)

        rv = self._response or self._dia.run()
        self._dia.hide_all()
        sortcol = self._store.get_sort_column_id()
        if sortcol[0] >= 0:
            self._sortcol = sortcol
        else:
            self._sortcol = None
        self._store = None
        if rv == gtk.RESPONSE_OK:
            m, i = self._treeview.get_selection().get_selected()
            self.foundOne(m.get_value(i, 0))

    def _doSetValue(self, value):
        self._row = value
        for i in self._entries:
            i.setValue(i.getGetter()(value))
    def _doGetValue(self):
        return self._row


class Gtk2BoxedSearch(BoxedSearch, Gtk2Search):
    def __init__(self, **kw): 
        self._processArgs(Gtk2BoxedSearch, kw)

class Gtk2VSearch(VSearch, Gtk2BoxedSearch, Gtk2VBox):
    __obligs = {'_obj': gtk.VBox,}
    def __init__(self, **kw):
        kw.setdefault('innerContainerClass', Gtk2HBox)
        self._processArgs(Gtk2HSearch, kw)

class Gtk2HSearch(HSearch, Gtk2BoxedSearch, Gtk2HBox):
    __obligs = {'_obj': gtk.HBox,}
    def __init__(self, **kw):
        kw.setdefault('innerContainerClass', Gtk2VBox)
        self._processArgs(Gtk2HSearch, kw)
