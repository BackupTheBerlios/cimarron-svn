# -*- coding: utf-8 -*-
#
# Copyright 2003, 2004, 2005 Fundación Via Libre
#
# This file is part of PAPO.
#
# PAPO is free software; you can redistribute it and/or modify it under the
# terms of the GNU General Public License as published by the Free Software
# Foundation; either version 2 of the License, or (at your option) any later
# version.
#
# PAPO is distributed in the hope that it will be useful, but WITHOUT ANY
# WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
# FOR A PARTICULAR PURPOSE.  See the GNU General Public License for more
# details.
#
# You should have received a copy of the GNU General Public License along with
# PAPO; if not, write to the Free Software Foundation, Inc., 59 Temple Place,
# Suite 330, Boston, MA 02111-1307 USA

from itertools import izip, repeat
import logging
logger = logging.getLogger('fvl.cimarron.skins.gtk2.grid')

from zope import interface
import gtk

from fvl.cimarron.controllers.column import ColumnAwareXmlMixin
from fvl.cimarron.controllers.base import Controller

class Grid(ColumnAwareXmlMixin, Controller):
    """
    Grids are used for editing a list of objects.
    """

    def __init__(self, columns=None, klass=None, **kw):
        """
        @param columns: a list of B{Column}s that describe
            what to show in the grid, how obtain it from the
            objects, and eventually how to save data back to.
        """
        self._widget = self._tv = gtk.TreeView()
        # self.mainWidget = self
        self.columns = columns

        self.klass = klass

        # put the TreeView in a scrolled window
        self._widget = gtk.ScrolledWindow()
        self._widget.set_policy(gtk.POLICY_NEVER, gtk.POLICY_ALWAYS)
        self._widget.add(self._tv)

        self._tv.connect('key-release-event', self._keyreleased)

        super (Grid, self).__init__(**kw)
        # this was not done because it was initializing
        # is this still true?
        self.refresh()

    def attributesToConnect(klass):
        return ['klass']+super (Grid, klass).attributesToConnect()
    attributesToConnect = classmethod(attributesToConnect)

    def _set_columns(self, columns):
        self._columns = columns or []
        if columns:
            # build the tv columns and the data types tuple
            (self._tvcolumns, self._dataspec) = izip(*izip(
                [ gtk.TreeViewColumn(c.name) for c in columns ],
                repeat(str)
                ))

            # add the columns and attrs
            for i in xrange (len(columns)):
                c = self._tvcolumns[i]
                crt = gtk.CellRendererText()
                # editable
                crt.set_property('editable', True)
                crt.connect('edited', self._cell_edited, i)
                c.pack_start(crt, True)
                c.add_attribute(crt, 'text', i)
                self._tv.append_column(c)
    def _get_columns(self):
        return self._columns
    columns = property(_get_columns, _set_columns)
        
    def _set_index(self, index):
        if index is not None:
            self._tv.set_cursor((index, ))
    def _get_index(self):
        cursor = self._tv.get_cursor()
        if cursor:
            return int(cursor[0][0])
        else:
            # the cursor is not set
            return None
    index = property(_get_index, _set_index, None,
                     """The index of the object currently selected.
                     If no object is selected, it is None.""")

    def _cell_edited(self, cell, path, text, colNo, *ignore):
        write = self.columns[colNo].write
        # modify the ListStore model...
        self._tvdata[path][colNo] = text
        # ... and our model
        try:
            write (self.value[int(path)], text)
        except(TypeError, IndexError):
            # we're editing the new value
            write(self.new, text)
            
        # coming soon: our models will (should) suport the generic TreeModel protocol
        # also: if write() returns false, the entry flashes and
        # a) rollbacks the value or
        # b) leaves it with wrong value, so the user can edit it (preferred)
        return False
    def _keyreleased(self, widget, key_event, *ignore):
        last = self.value is None or len (self.value)==0 or self.index==len(self.value)-1
        # print `self.value`, `self._tv.get_cursor ()`, last

        if key_event.keyval==gtk.keysyms.Down and last:
            try:
                if self.new.isDirty:
                    if self.value is None:
                        self.value = [self.new]
                    else:
                        self.value.append(self.new)
                    self.new = self.klass()
                    self._tvdata.append ([j.read(self.new) for j in self.columns])
            except AttributeError:
                # print 'self.new does not exist. so, go create it'
                self.new = self.klass()
                self._tvdata.append ([j.read(self.new) for j in self.columns])
            
        return False

    def refresh(self):
        super(Grid, self).refresh()
        if len(self.columns)>0:
            self._tvdata = gtk.ListStore(*self._dataspec)
        else:
            self._tvdata = gtk.ListStore(str)
        # print 'Grid.refresh:', `self.value`, self.columns
        if self.value is not None:
            for i in self.value:
                # add all the values
                # NOTE: this forces the data to be read.
                data = [j.read(i) for j in self.columns]
                # print 'Grid: adding', data
                self._tvdata.append(data)
            self.index = 0
        else:
            self.index = None
        self._tv.set_model(self._tvdata)


class SelectionGrid(ColumnAwareXmlMixin, Controller):
    """
    SelectionGrids are used for showing a list of objects,
    and for selecting one among those.
    """

    def __init__(self, data=None, columns=None, **kw):
        """
        @param data: the list of objects to be shown.

        @param columns: a list of B{Column}s that describe
            what to show in the grid, how obtain it from the
            objects, and eventually how to save data back to.
        """
        self._tv = gtk.TreeView()

        if columns is None:
            columns = []
        if data is None:
            data = []

        self._columns = columns
        # build the tv columns and the data types tuple
        (self._tvcolumns, self._dataspec) = izip(*izip(
            [ gtk.TreeViewColumn(c.name) for c in columns ],
            repeat(str)
            ))
        self.data = data

        # put the TreeView in a scrolled window
        self._widget = gtk.ScrolledWindow()
        self._widget.set_policy(gtk.POLICY_NEVER, gtk.POLICY_ALWAYS)
        self._widget.add(self._tv)

        # add the columns and attrs
        for i in xrange (len(columns)):
            c = self._tvcolumns[i]
            crt = gtk.CellRendererText()
            c.pack_start(crt, True)
            c.add_attribute(crt, 'text', i)
            self._tv.append_column(c)

        self._tv.connect('key-release-event', self._keyreleased)
        self._tv.connect('cursor_changed', self._cursor_changed)

        super (SelectionGrid, self).__init__(**kw)

    def _keyreleased(self, widget, key_event, *ignore):
        if key_event.keyval==gtk.keysyms.Return:
            self.onAction()
            return True
        return False

    def _set_data(self, data):
        # the model data
        self._data = data
        self.refreshFromData()
	
    def refreshFromData(self):
        if len(self._columns)>0:
            self._tvdata = gtk.ListStore(*self._dataspec)
        if self.data is not None:
            for i in self.data:
                # build a ListStore w/ al the values
                # NOTE: this forces the data to be read.
                self._tvdata.append ([j.read(i) for j in self._columns])
        self._tv.set_model(self._tvdata)
    def _get_data(self):
        return self._data
    data = property(_get_data, _set_data, None,
                    """The list of objects to be shown.""")

    def _cursor_changed(self, *ignore):
        self.__index = int (self._tv.get_cursor()[0][0])
    def _set_index(self, index):
        if index is not None:
            self._tv.set_cursor(index)
        self.__index = index
    def _get_index(self):
        return self.__index
    index = property(_get_index, _set_index, None,
                     """The index of the object currently selected.
                     If no object is selected, it is None.""")

    def _set_value(self, value):
        try:
            index = self.data.index(value)
        except(ValueError, AttributeError):
            #   the value is not present
            #               data might be None?
            index = None
            # what about building a new item?
        self.index = index
        # super (SelectionGrid, self)._set_value (value)
        # print '-> value:', value, 'index:', index
        
    def _get_value(self):
        ans = None
        if self.index is not None:
            ans = self.data[self.index]
        # print '<- value:', ans, 'index:', self.index
        return ans
    value = property(_get_value, _set_value, None,
                     """The selected object. If no object is selected, it is None.""")

