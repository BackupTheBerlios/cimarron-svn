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

from CompositeView import CompositeView, _
from Exceptions import TableError

class Table(CompositeView):
    """
    Container that packs widgets into regular patterns.

    Additional keyword arguments are:
    """
    __kwargs = ('size', 'rowSpacings', 'colSpacings', 'homogeneous')
    __doc__ += "%s\n" % (__kwargs,)
        
    def attach(self, widget, left, right, top, bottom):
        """
        Add widget to the table between left and right, and between
        top and bottom.

        Returns the result of the delegation (i.e., True if delegates
        agreed to doing it). Raises a TableError if anything bad
        happens.
        """
        if self.delegate('will_attach', args=(widget, left, right, top, bottom)):
            try:
                self._doAttach(widget, left, right, top, bottom)
            except:
                raise TableError, _("Unable to attach")
            return True
        return False
   
    def setColSpacings(self, spacing):
        """
        Set the space around every column.

        Returns the result of the delegation (i.e., True if delegates
        agreed to doing it). Raises a TableError if anything bad
        happens.
        """
        if self.delegate('will_set_col_spacings', args=spacing):
            try:
                self._doSetColSpacings(spacing)
            except:
                raise TableError, _("Unable to set spacings")
            return True
        return False
    def setColSpacing(self, col, spacing):
        """
        Set the space around the specified column.

        Returns the result of the delegation (i.e., True if delegates
        agreed to doing it). Raises a TableError if anything bad
        happens.
        """
        if self.delegate('will_set_col_spacing', args=(col, spacing)):
            try:
                self._doSetColSpacing(col, spacing)
            except:
                raise TableError, _("Unable to set spacing")
            return True
        return False
    def getColSpacing(self, col):
        """
        Get the requested space around a specific column
        """
        return self._doGetColSpacing(col)
    def getDefaultColSpacing(self):
        """
        Get the default space around columns.
        """
        return self._doGetDefaultColSpacing()
        
    def setRowSpacings(self, spacing):
        """
        Set the space around every row.

        Returns the result of the delegation (i.e., True if delegates
        agreed to doing it). Raises a TableError if anything bad
        happens.
        """
        if self.delegate('will_set_row_spacings', args=spacing):
            try:
                self._doSetRowSpacings(spacing)
            except:
                raise TableError, _("Unable to set spacings")
            return True
        return False
    def setRowSpacing(self, row, spacing):
        """
        Set the space around the specified row.

        Returns the result of the delegation (i.e., True if delegates
        agreed to doing it). Raises a TableError if anything bad
        happens.
        """
        if self.delegate('will_set_row_spacing', args=(row, spacing)):
            try:
                self._doSetRowSpacing(row, spacing)
            except:
                raise TableError, _("Unable to set spacing")
            return True
        return False
    def getRowSpacing(self, row):
        """
        Get the requested space around a specific row
        """
        return self._doGetRowSpacing(row)
    def getDefaultRowSpacing(self):
        """
        Get the default space around rows.
        """
        return self._doGetDefaultRowSpacing()
        
    def setHomogeneous(self, homogeneous):
        """
        Set whether all cells should be equally sized.

        Returns the result of the delegation (i.e., True if delegates
        agreed to doing it). Raises a TableError if anything bad
        happens.
        """
        if self.delegate('will_set_homogeneous', args=homogeneous):
            try:
                self._doSetHomogeneous(homogeneous)
            except:
                if homogeneous:
                    raise TableError, _("Unable to set `homogeneous' flag")
                else:
                    raise TableError, _("Unable to clear `homogeneous' flag")
            return True
        return False
    def getHomogeneous(self):
        """
        Get the requested homogeneousosity.
        """
        return self._doGetHomogeneous()
        
    def setSize(self, size):
        """
        Alias for resize.
        """
        return self.resize(*size)
    def resize(self, rows, columns):
        """
        Resize the table to the given number of rows and columns.

        This is for performance reasons: attach() resizes on-the-fly,
        but it's expensive to do so.

        Returns the result of the delegation (i.e., True if delegates
        agreed to doing it). Raises a TableError if anything bad
        happens.
        """
        if self.delegate('will_resize', args=(rows, columns)):
            try:
                self._doResize(rows, columns)
            except:
                raise TableError, _("Unable to resize")
            return True
        return False
