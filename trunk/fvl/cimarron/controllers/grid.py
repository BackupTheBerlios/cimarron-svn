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

from fvl import cimarron
from base import Controller
from column import ColumnAwareXmlMixin

class Grid (ColumnAwareXmlMixin, Controller):
    def __init__ (self, data=[], columns=None, **kw):
        self.__initialized= False
        self.columns= columns
        self.labels= []
        self.entries= {}

        self.index= None
        self.data= data

        super (Grid, self).__init__ (**kw)
        self.widget= v= cimarron.skin.VBox (parent=self.parent)
        self.__initialized= True

    def mainWidget(self):
        return self.entries[self.index,0]
    mainWidget = property(mainWidget)

    def _set_data (self, data):
        self.__data= data
        self.refresh ()
        if data is not None and len (data)>0:
            self.index= 0
    def _get_data (self):
        return self.__data
    data= property (_get_data, _set_data)
    def updateData (self, entry, *i):
        if self.columns[entry.column].write is not None:
            self.columns[entry.column].write (self.data[entry.row], entry.value)

    def selected (self, entry, *ignore):
        self.updateData (entry)
        self.onAction ()

    def refresh (self):
        try:
            # normal case: data is some sequence
            for i in xrange (len (self.data)):
                if len (self.labels)<=i:
                    # the row does not exist, so we add it
                    h= cimarron.skin.HBox (parent=self.widget)
                    b= cimarron.skin.Label (
                        parent= h,
                        text= ' ',
                        row= i
                        )

                    self.labels.append (b)
                    
                    # now the entries
                    for j in xrange (len (self.columns)):
                        entryConstr= self.columns[j].entry or cimarron.skin.Entry
                        self.entries[i, j]= entryConstr (
                            parent= h,
                            value= self.columns[j].read (self.data[i]),
                            onAction= self.selected,
                            column= j,
                            row= i,
                            )
                        self.entries[i, j].delegates.append (self)
                else:
                    for j in xrange (len (self.columns)):
                        self.entries[i, j].value= self.columns[j].read (self.data[i])
            for i in xrange (len (self.data), len (self.labels)):
                for j in xrange (len (self.columns)):
                    self.entries[i, j].value= ''

        except TypeError:
            # except case: data is something else (tipically, `NoneÂ´)
            for i in xrange (len (self.labels)):
                for j in xrange (len (self.columns)):
                    self.entries[i, j].value= ''

    def will_focus_in (self, entry, *ignore):
        self.index= entry.row
    def will_focus_out (self, entry, *ignore):
        self.updateData (entry)

    def _set_index (self, index):
        if self.__initialized and self.index is not None:
            self.labels[self.index].text= ' '
            if index is not None:
                self.labels[index].text= '>'
        self.__index= index
    def _get_index (self):
        return self.__index
    index= property (_get_index, _set_index)

    def _get_value (self):
        ans= None
        if self.index is not None:
            ans= self.data[self.index]
        return ans
    def _set_value (self, value):
        try:
            index= self.data.index (value)
        except (ValueError, AttributeError):
            index= None
        self.index= index
    value= property (_get_value, _set_value)

