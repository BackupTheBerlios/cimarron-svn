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
# Debug.sections.append ('Notebook')

from CompositeView import CompositeView, _
from Exceptions import NotebookError

class Notebook(CompositeView):
    """
    A tabbed notebook container.

    No additional keyword arguments.
    """
    
    def appendPage(self, child, label, menu=None):
        """
        Alias for insertPage(-1)
        """
        return self.insertPage(-1, child, label, menu)
    def prependPage(self, child, label, menu=None):
        """
        Alias for insertPage(0)
        """
        return self.insertPage(0, child, label, menu)
    def insertPage(self, pos, child, label, menu=None):
        """
        Insert a page into the notebook.

        If pos is -1, insert at the end; otherwise, insert a page at
        position pos (starting at 0).

        The page is made up of:
          child  in the body of the frame
          label  the label on the tab
           menu  the label in the pop-up menu (label is used if menu is None)

        Returns the result of the delegation (i.e., True if delegates
        agreed to doing it). Raises a NotebookError if anything bad
        happens.
        """
        if menu is None:
            menu=label
        if self.delegate('will_insert_page', args=(pos, child, label, menu)):
            try:
                self._doInsertPage(pos, child, label, menu)
                self.debug ("notebook: setting %s's parent to %s" % (child, self))
                child.setParent (self)
            except:
                raise NotebookError, _("Unable to insert page")
            return True
        return False

    def nextPage(self):
        """
        Switch to the next page, if there is one.

        Returns the result of the delegation (i.e., True if delegates
        agreed to doing it). Raises a NotebookError if anything bad
        happens.
        """
        if self.delegate('will_change_to_next_page'):
            try:
                self._doNextPage()
            except:
                raise NotebookError, _("Unable to advance to next page")
            return True
        return False
    def prevPage(self):
        """
        Switch to the previous page, if there is one.

        Returns the result of the delegation (i.e., True if delegates
        agreed to doing it). Raises a NotebookError if anything bad
        happens.
        """
        if self.delegate('will_change_to_prev_page'):
            try:
                self._doPrevPage()
            except:
                raise NotebookError, _("Unable to go back to previous page")
            return True
        return False
    def changePage(self, n):
        """
        Switch to page number n.

        Returns the result of the delegation (i.e., True if delegates
        agreed to doing it). Raises a NotebookError if anything bad
        happens.
        """
        if self.delegate('will_change_to_page', args=n):
            try:
                self._doChangePage(n)
            except:
                raise NotebookError, _("Unable to change to page %d") % (n,)
            return True
        return False
