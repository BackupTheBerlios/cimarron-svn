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

"""
In this module you will find two different kinds of grid: A writeable L{Grid}
whose value is a list of objects, and a read-only L{SelectionGrid} whose value
is the selected item from a list of possibilities.
"""

__revision__ = int('$Rev$'[5:-1])

import logging
logger = logging.getLogger('fvl.cimarron.skins.gtk2.grid')
# logger.setLevel(logging.DEBUG)

from zope import interface
import gtk

from fvl.cimarron.controllers.column import ColumnAwareXmlMixin
from fvl.cimarron.controllers.base import Controller

class Grid(ColumnAwareXmlMixin, Controller):
    """
    Grids are used for editing a list of objects.
    """
    def __init__(self, columns=None, cls=None, **kwargs):
        """
        @param columns: a list of B{Column}s that describe
            what to show in the grid, how obtain it from the
            objects, and eventually how to save data back to.

        @param cls: a class for building new objects. if this is None,
            the grid won't be able to create more objects, but still
            will be able to edit the existing ones.
        """
        if '_concreteWidget' not in self.__dict__:
            self._concreteWidget = gtk.TreeView()
        self._tv = self._concreteWidget
        self._tv.set_rules_hint(True)
        self.columns = columns
        self.cls = cls

        # put the TreeView in a scrolled window
        if '_outerWidget' not in self.__dict__:
            self._outerWidget = gtk.ScrolledWindow()
            self._outerWidget.set_policy(gtk.POLICY_NEVER, gtk.POLICY_ALWAYS)
            self._outerWidget.add(self._tv)

        self._tv.connect('key-release-event', self._keyreleased)

        # make pylint (more like crud puppy now) happy
        self._tvdata = None
        self._tvdatalen = 0
        # pylint must be ignored on these.
        # they're set to the proper values elsewhere.
        # self._columns = []
        # self._dataspec = None
        # self._tvcolumns = None
        self.index = None

        super(Grid, self).__init__(**kwargs)

    def _get_value(self):
        return self._value
    def _set_value(self, value):
        if self.window is not None:
            self.window.disable()
        try:
            self._value = value
            if len(self.columns)>0:
                self._tvdata = gtk.ListStore(*self._dataspec)
            else:
                self._tvdata = gtk.ListStore(str)

            if value is not None:
                for i in value:
                    self._tvdata.append([i.getattr(j.attribute)
                                         for j in self.columns])
                self._tvdatalen = len(value)
                self.index = 0
            else:
                self._tvdatalen = 0
                self.index = None
            self._tv.set_model(self._tvdata)
        finally:
            if self.window is not None:
                self.window.enable()
    value = property(_get_value, _set_value)

    def attributesToConnect(cls):
        """
        See L{XmlMixin.attributesToConnect}
        """
        return ['cls'] + super(Grid, cls).attributesToConnect()
    attributesToConnect = classmethod(attributesToConnect)

    def _set_columns(self, columns):
        """
        Set the grid's columns. C{columns} should be a list of L{Column}-like
        objects.
        """
        self._columns = columns or []
        if columns:
            # build the tv columns and the data types tuple
            # i don't find a socking way to tell the focusing to skip
            # readOnly columns.
            (self._tvcolumns, self._dataspec) = \
                zip(*[ (gtk.TreeViewColumn(column.name),
                        column.entry._cellDataType)
                       for column in columns ])

            # add the columns and attrs
            for i, dataColumn in enumerate(columns):
                viewColumn = self._tvcolumns[i]
                dataColumn.entry._setupCell(self, dataColumn, viewColumn, i)
                self._tv.append_column(viewColumn)

    def _get_columns(self):
        return self._columns
    columns = property(_get_columns, _set_columns)
        
    def _set_index(self, index):
        """
        If index is not None, select the grid's row #C{index}.
        """
        if index is not None:
            # focus the right column
            # or the first if there's no column focused yet
            # which is the case when tehre were no rows.
            column = self._tv.get_cursor()[1]
            if column is None:
                column = self._tvcolumns[0]
            self._tv.set_cursor((index, ), column)
    def _get_index(self):
        """
        Return the index of the selected row, or None if nothing is currently
        selected.
        """
        cursor = self._tv.get_cursor()
        if cursor and cursor[0]:
            return int(cursor[0][0])
        else:
            # the cursor is not set
            return None
    index = property(_get_index, _set_index, None,
                     """The index of the object currently selected.
                     If no object is selected, it is None.""")

    def _cell_toggled(self, cell, path, colNo, *ignore):
        newVal = not self._tvdata[path][colNo]
        return self._cell_edited(cell, path, newVal, colNo)

    def _cell_edited(self, cell, path, newVal, colNo, *ignore):
        """
        A cell has been edited: keep the models in sync.
        """
        attribute = self.columns[colNo].attribute
        # modify the ListStore model...
        self._tvdata[path][colNo] = newVal
        # ... and our model
        value = self.value
        # print `value`, `path`
        if value is not None and int(path)<len(value):
            value = value[int(path)]
        else:
            # we're editing the empty row, so go build an object
            # to give back up that row.
            value = self.cls()
            if self.value is not None:
                self.value.append(value)
            else:
                self.value = [value]
        value.setattr(attribute, newVal)
            
        return False
    def _keyreleased(self, widget, key_event, *ignore):
        """
        A key has been released: the user might be wanting to insert a row...
        """
        if self.value is None:
            valueLen = 0
        else:
            valueLen = len(self.value)
        # conditions that assert we're in the last row of data.
        last = self.value is None \
               or valueLen == 0 \
               or self.index == valueLen-1
               
        logger.debug("%r %r %r", self.index, self.value, last)
        if key_event.keyval == gtk.keysyms.Down and last and \
               self.cls is not None and self._tvdatalen == valueLen:
            # right conditions; insert a new row in the TreeView
            # without changing the value yet.
            self._tvdata.append(['' for j in self.columns])
            self._tvdatalen += 1
            self.index = valueLen
            logger.debug('making new %r', self.index)
            
        logger.debug(`self._tv.get_cursor()`)
        return False

class SelectionGrid(ColumnAwareXmlMixin, Controller):
    """
    SelectionGrids are used for showing a list of objects,
    and for selecting one among those.
    """

    def __init__(self, data=None, columns=None, **kwargs):
        """
        @param data: the list of objects to be shown.

        @param columns: a list of B{Column}s that describe
            what to show in the grid, how obtain it from the
            objects, and eventually how to save data back to.
        """

        #self._concreteWidget = self._tv = gtk.TreeView()
        if '_concreteWidget' not in self.__dict__:
            self._concreteWidget = gtk.TreeView()  
        #self._tv = gtk.TreeView()
        self._concreteWidget.set_rules_hint(True)

        if columns is None:
            columns = []
        if data is None:
            data = []

        self._columns = columns
        # build the tv columns and the data types tuple
        if columns:
            (self._tvcolumns, self._dataspec) = \
                              zip(*[ (gtk.TreeViewColumn(column.name),
                                      column.entry._cellDataType)
                                     for column in columns ])
        else:
            self._tvcolumns = self._dataspec = ()
        self.data = data

        # put the TreeView in a scrolled window
        if '_outerWidget' not in self.__dict__:
            self._outerWidget = gtk.ScrolledWindow()
            self._outerWidget.set_policy(gtk.POLICY_NEVER, gtk.POLICY_ALWAYS)
            self._outerWidget.add(self._concreteWidget)

        # add the columns and attrs
        for i, dataColumn in enumerate(columns):
            viewColumn = self._tvcolumns[i]
            dataColumn.entry._setupCell(self, dataColumn, viewColumn, i,
                                        readOnly=True)
            #self._tv.append_column(viewColumn)
            self._concreteWidget.append_column(viewColumn)

        #self._tv.connect('key-release-event', self._keyreleased)
        self._concreteWidget.connect('key-release-event', self._keyreleased)
        #self._tv.connect('cursor_changed', self._cursor_changed)
        self._concreteWidget.connect('cursor_changed', self._cursor_changed)
        #self._tv.connect('row-activated', self._double_click)
        self._concreteWidget.connect('row-activated', self._double_click)

        super (SelectionGrid, self).__init__(**kwargs)


    def _double_click(self, widget, *ignore):
        """
        The user double-clicked a row: fire the action.
        """
        self.onAction ()
        return True

    def _keyreleased(self, widget, key_event, *ignore):
        """
        The user released a key: if it was Return, fire the action.
        """
        if key_event.keyval == gtk.keysyms.Return:
            self.onAction()
            return True
        return False

    def _set_data(self, data):
        # the model data
        self._data = data
        self.refreshFromData()
	
    def refreshFromData(self):
        if len(self._columns) > 0:
            self._tvdata = gtk.ListStore(*self._dataspec)
        else:
            self._tvdata = None
        if self.data is not None:
            for i in self.data:
                # build a ListStore w/ al the values
                # NOTE: this forces the data to be read.
                self._tvdata.append([i.getattr(j.attribute)
                                     for j in self._columns])
        #self._tv.set_model(self._tvdata)
        self._concreteWidget.set_model(self._tvdata)
    def _get_data(self):
        return self._data
    data = property(_get_data, _set_data, None,
                    """The list of objects to be shown.""")

    def _cursor_changed(self, *ignore):
        """
        The user changed the highlighted row.
        """
        #self.__index = int(self._tv.get_cursor()[0][0])
        self.__index = int(self._concreteWidget.get_cursor()[0][0])
    def _set_index(self, index):
        """
        Change which row is highlighted, to the row who's index is C{index}.
        """
        if index is not None:
            #self._tv.set_cursor(index)
            self._concreteWidget.set_cursor(index)
        self.__index = index
    def _get_index(self):
        """
        Get the index of the selected row.
        """
        return self.__index
    index = property(_get_index, _set_index, None,
                     """The index of the object currently selected.
                     If no object is selected, it is None.""")

    def _set_value(self, value):
        """
        Set the value of the L{SelectionGrid} to C{value}. If C{value}
        is not one of the possible values, the value is None.
        """
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
        """
        Return the value of the L{SelectionGrid}, or None if nothing
        is selected.
        """
        ans = None
        if self.index is not None:
            ans = self.data[self.index]
        # print '<- value:', ans, 'index:', self.index
        return ans
    value = property(_get_value, _set_value,
                     doc="The selected object."
                     " If no object is selected, it is None.")
