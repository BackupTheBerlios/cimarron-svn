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

from fvl import cimarron
from fvl.cimarron.controllers.base import Controller
from fvl.cimarron.controllers.column import ColumnAwareXmlMixin

logger = logging.getLogger('fvl.cimarron.controllers.search')
# logger.setLevel(logging.DEBUG)

class SelectionWindow(Controller):
    """
    Not public. Please Ignore :)

    XXX: why isn't this inheriting from WindowController?
    """
    def __init__(self, columns=None, **kwargs):
        if columns is None:
            columns = []
        super(SelectionWindow, self).__init__(**kwargs)
        self.win = cimarron.skin.Window(parent=self.parent,
                                       title='Select', size=(30, 5))
        vbox = cimarron.skin.VBox(parent=self.win)
        self.grid = cimarron.skin.SelectionGrid(parent=vbox, columns=columns,
                                               onAction=self.onOk)
        hbox = cimarron.skin.HBox(parent=vbox, expand=False)
        self.ok = cimarron.skin.Button(parent=hbox, label='Ok',
                                      onAction=self.onOk)
        self.cancel = cimarron.skin.Button(parent=hbox, label='Cancel',
                                          onAction=self.onCancel)

    def show(self):
        # FIXME: explain this assignment to value from within show
        self.value = None
        self.win.show()

    def onOk(self, *ignore):
        """
        onAction for 'Ok' button.
        """
        self.value = self.grid.value
        self.win.hide()
        self.onAction()

    def onCancel(self, *ignore):
        """
        onAction for 'Cancel' button
        """
        self.value = None
        self.win.hide()
        self.onAction()

    def hide(self):
        self.win.hide()

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
    
    def __init__(self, columns=None, transaction=None, searcher=None, **kwargs):
        """
        @param columns: A list of Columns. Only the C{read} attribute
            needs to be set.
        """
        super(Search, self).__init__(**kwargs)
        self.entries = []
        self.h = cimarron.skin.HBox(parent=self, expand=False)
        self.columns = columns
        self.value = None
        self.searcher = searcher
        self.trans = transaction

    def _set_columns(self, columns):
        logger.debug (`columns`)
        if columns is not None:
            for c in columns:
                cimarron.skin.Label(text=c.name+":", parent=self.h)
                entryConstr = c.entry
                self.entries.append (entryConstr(
                    parent = self.h,
                    onAction = self.action
                    ))

            b = cimarron.skin.Button(
                parent = self.h,
                label = 'Search!',
                onAction = self.action,
                )
            
            self.mainWidget = b
        self.__columns = columns
    def _get_columns(self):
        return self.__columns
    columns = property(_get_columns, _set_columns)

    def doSearch(self, *ignore):
        """
        Performs the abstract search, and handles the case
        when more than one object is found.
        """
        data = {}
        for i in xrange(len(self.columns)):
            e= self.entries[i]
            c= self.columns[i]
            if e.value!='':
                # '' means `don't filter by me'
                data[c.attribute] = e.value

        # print 'searching', self.searcher, data
        self.value= self.searcher.search (self.trans, **data)
        return len(self.value)
    def search (self, *ignore):
        ans= self.doSearch()
        self.onAction()
        return ans
    action = search

class SearchEntry(Search):
    def _set_columns(self, columns):
        logger.debug (`columns`)
        super(SearchEntry,self)._set_columns(columns)
        if columns is not None:
            # build the selection window
            self.selwin= SelectionWindow (columns= columns,
                                          onAction= self.selected,)
    def _get_columns(self):
        return super(SearchEntry, self)._get_columns()
    columns= property (_get_columns, _set_columns)
        
    def search (self, *ignore):
        """
        Performs the abstract search, and handles the case
        when more than one object is found.
        """
        self.doSearch()

        # print 'searching', self.searcher, data
        ans = self.value
        if len(ans)==0:
            self.value = None
        elif len(ans)==1:
            self.value = ans[0]
        if len(ans)>1:
            # select
            self.selwin.grid.data = ans
            self.selwin.show()
        else:
            self.onAction()
        return len(ans)
    action = search

    def selected(self, *ignore):
        """
        Callback for the selection window when finally
        one object is selected.
        """
        self.value = self.selwin.value
        self.selwin.hide()
        self.onAction()

    def refresh(self):
        """
        Show the value.
        """
        super(SearchEntry, self).refresh()
        entries = self.entries
        if self.value is not None:
            value_getattr = self.value.getattr
            columns = self.columns
            for i in xrange(len(entries)):
                entries[i].value = value_getattr(columns[i].attribute)
        else:
            for i in xrange(len(entries)):
                entries[i].value = ''
