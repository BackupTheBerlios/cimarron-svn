# -*- coding: utf-8 -*-
#
# Copyright 2005 Fundación Via Libre
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
L{Search}es and related junk.
"""

__revision__ = int('$Rev$'[5:-1])

import logging

from fvl.cimarron.controllers.base import Controller, WindowController
from fvl.cimarron.controllers.column import ColumnAwareXmlMixin
from fvl.cimarron.skins.common import No as DelegateNo

logger = logging.getLogger('fvl.cimarron.controllers.search')
# logger.setLevel(logging.DEBUG)

class SelectionWindow(WindowController):
    """
    Not public. Please Ignore :)
    """
    def __init__(self, columns=None, **kwargs):
        from fvl.cimarron import skin
        
        if columns is None:
            columns = []
        super(SelectionWindow, self).__init__(parent=self.parent,
                                              title='Select', size=(30, 5),
                                              **kwargs)
        vbox = skin.VBox(parent=self.win)
        self.grid = skin.SelectionGrid(parent=vbox, columns=columns,
                                       onAction=self.onOk)
        hbox = skin.HBox(parent=vbox, expand=False)
        self.ok = skin.Button(parent=hbox, label='Ok',
                              onAction=self.onOk)
        self.cancel = skin.Button(parent=hbox, label='Cancel',
                                  onAction=self.onCancel)

    def onOk(self, *ignore):
        """
        onAction for 'Ok' button.
        """
        self.value = self.grid.value
        self.hide()
        self.onAction()

    def onCancel(self, *ignore):
        """
        onAction for 'Cancel' button
        """
        self.value = None
        self.hide()
        self.onAction()

    def refresh(self):
        self.grid.refresh()

class Search(ColumnAwareXmlMixin, Controller):
    """
    Abstract class for searching. Consist of a widget
    with one Entry for each Column.

    The method C{search()} must be
    implemented in the subclass, which sould take one parameter
    for each column and return the list of objects found to that
    search criteria.

    This class already handles the case when the amount of objets
    found is greater that one. In that case, it presents a window
    where the user can select from a list.

    When one object is found or selected, it calls the action.
    """
    def attributesToConnect(cls):
        """
        See L{XmlMixin.attributesToConnect
        <fvl.cimarron.skins.common.XmlMixin.attributesToConnect>}
        """
        attrs = super (Search, cls).attributesToConnect()
        return attrs+['searcher']
    attributesToConnect = classmethod(attributesToConnect)
    
    def __init__(self, columns=None, cls=None, searcher=None, **kwargs):
        """
        @param columns: A list of Columns. Only the C{read} attribute
            needs to be set.

        @param searcher: an object that knows the values() for the right type of
            objects. Typically, the Class itself.

        @param cls: The class that we'll want to look for with C{searcher}.
        """
        from fvl.cimarron.skin import HBox

        super(Search, self).__init__(**kwargs)
        self.entries = []
        self.h = HBox(parent=self, expand=False)
        self.columns = columns
        self.value = None
        self.searcher = searcher
        self.cls = cls

    def _set_columns(self, columns):
        logger.debug (`columns`)
        if columns is not None:
            from fvl.cimarron.skin import Label, Button
            for column in columns:
                # build label and entry
                Label(text=column.name+":", parent=self.h)
                entryConstr = column.entry
                entry = entryConstr(parent=self.h, onAction=self.search,
                                    attribute=column.attribute)
                entry.delegates.append (self)
                self.entries.append (entry)

            # search button
            b = Button(parent=self.h, label='Search!', onAction=self.search)
            
            # the widget that fires the action.
            self.mainWidget = b
        self.__columns = columns
    def _get_columns(self):
        return self.__columns
    columns = property(_get_columns, _set_columns)

    def doSearch(self, *ignore):
        """
        Performs the abstract search. The result ends up in aSearch.value as a
        list and returns the length of the list.
        """
        data = {}
        for i in xrange(len(self.columns)):
            e = self.entries[i]
            c = self.columns[i]
            if e.value != '':
                # '' means `don't filter by me'
                data[c.attribute] = e.value

        logger.debug ('searching %r, %r', self.searcher, data)
        self.value = self.searcher.search(self.cls, **data)
        return len(self.value)
    def search (self, *ignore):
        """
        Performs the search and fires the action thereupon.
        """
        ans = self.doSearch()
        self.onAction()
        return ans

    def will_focus_out(self, *ignore):
        return DelegateNo

class SearchEntry(Search):
    def _set_columns(self, columns):
        logger.debug (`columns`)
        super(SearchEntry,self)._set_columns(columns)
        if columns is not None:
            # build the selection window here because:
            # a) we can't build it w/o columns (well, we *could*,
            # but then we'll needmore API just for this case) and
            # b) we must change the columns in the SelectionWindow
            # when new Columns are supplied.
            self.selwin= SelectionWindow (columns= columns,
                                          onAction= self.selected,)
    def _get_columns(self):
        return super(SearchEntry, self)._get_columns()
    columns= property (_get_columns, _set_columns)
        
    def search (self, *ignore):
        """
        Performs the search, and handles the case
        when more than one object is found.
        """
        self.doSearch()

        ans = self.value
        if len(ans)==0:
            self.commitValue(None)
        elif len(ans)==1:
            self.commitValue(ans[0])
            self.refresh()
        if len(ans)>1:
            # too much information, select one please.
            self.selwin.grid.data = ans
            # this `comes back` in selected() (see below).
            self.selwin.show()
        else:
            self.onAction()
        logger.debug(`self.value`)
        return len(ans)

    def selected(self, *ignore):
        """
        Callback for the selection window when finally
        one object is selected.
        """
        self.commitValue(self.selwin.value)
        self.refresh()
        self.selwin.hide()
        self.onAction()
        logger.debug(`self.value`)

    def refresh(self):
        """
        Show the value.
        """
        # traceback.print_stack()
        logger.debug(`self.value`)
        super(SearchEntry, self).refresh()
        logger.debug(`self.value`)
        entries = self.entries
        for entry in self.entries:
            entry.newTarget(self.value)
