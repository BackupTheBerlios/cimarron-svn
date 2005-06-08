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

from papo import cimarron
from base import Controller
from column import ColumnAwareXmlMixin

class SelectionWindow (Controller):
    """
    Not public. Please Ignore :)
    """
    def __init__ (self, columns=[], **kw):
        super (SelectionWindow, self).__init__ (**kw)
        self.win= cimarron.skin.Window (
            parent= self.parent,
            title= 'Select',
            )
        v= cimarron.skin.VBox (parent=self.win)
        self.grid= cimarron.skin.SelectionGrid (
            parent= v,
            columns= columns,
            onAction= self.onOk,
        )
        h= cimarron.skin.HBox (parent=v)
        self.ok= cimarron.skin.Button (
            parent= h,
            label= 'Ok',
            onAction= self.onOk,
            )
        self.cancel= cimarron.skin.Button (
            parent= h,
            label= 'Cancel',
            onAction= self.onCancel,
        )

    def show (self):
        self.value= None
        self.win.show ()

    def onOk (self, *ignore):
        self.value= self.grid.value
        self.win.hide ()
        self.onAction ()

    def onCancel (self, *ignore):
        self.value= None
        self.win.hide ()
        self.onAction ()

    def hide (self):
        self.win.hide ()

    def refresh (self):
        self.grid.refresh ()

class SearchEntry (ColumnAwareXmlMixin, Controller):
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
    def attributesToConnect (klass):
        attrs= super (SearchEntry, klass).attributesToConnect ()
        return attrs+['searcher']
    attributesToConnect= classmethod (attributesToConnect)
    
    def __init__ (self, columns=None, searcher=None, **kw):
        """
        @param columns: A list of Columns. Only the C{read} attribute
            needs to be set.
        """
        super (SearchEntry, self).__init__ (**kw)
        self.entries= []
        self.h= cimarron.skin.HBox (parent= self)
        self.columns= columns
        self.value= None
        self.searcher= searcher

    def _set_columns (self, columns):
        if columns is not None:
            for c in columns:
                entryConstr= c.entry
                self.entries.append (entryConstr (
                    parent= self.h,
                    onAction= self.doSearch
                    ))

            b= cimarron.skin.Button (
                parent= self.h,
                label= 'Search!',
                onAction= self.doSearch,
                )
            
            # build the selection window
            self.selwin= SelectionWindow (
                columns= columns,
                onAction= self.selected,
                )
            
            self.mainWidget = b
        self.__columns= columns
    def _get_columns (self):
        return self.__columns
    columns= property (_get_columns, _set_columns)

    def doSearch (self, *ignore):
        """
        Performs the abstract search, and handles the case
        when more than one object is found.
        """
        data= []
        for e in self.entries:
            if e.value=='':
                # '' means `don't filter by me'
                data.append (None)
            else:
                data.append (e.value)

        # print 'searching', self.searcher, data
        ans= self.searcher.search (data)
        if len (ans)==0:
            self.value= None
        elif len (ans)==1:
            self.value= ans[0]
        if len (ans)>1:
            # select
            self.selwin.grid.data= ans
            self.selwin.show ()
        else:
            self.onAction ()

    def selected (self, *ignore):
        """
        Callback for the selection window when finally
        one object is selected.
        """
        self.value= self.selwin.value
        self.selwin.hide ()
        self.onAction ()

    def refresh (self):
        """
        Show the value.
        """
        if self.value is not None:
            for i in xrange (len (self.entries)):
                self.entries[i].value= self.columns[i].read (self.value)
        else:
            for i in xrange (len (self.entries)):
                self.entries[i].value= ''


class Search (SearchEntry):
    pass
