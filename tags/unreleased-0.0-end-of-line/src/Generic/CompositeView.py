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

from View import View, _
from CompositeResponder import CompositeResponder
from Exceptions import CompositeViewError

class CompositeView(View, CompositeResponder):
    """
    CompositeView is the base class for views that have children
    inside them.
    
    Keyword arguments, in addition to those in the base classes, are:
    """
    __kwargs =  ('borderWidth',)
    __doc__ += "%s\n" % (__kwargs,)
        
    def update(self):
        [getattr(i, 'update', lambda:None)() for i in self._children]
    def setBorderWidth(self, width):
        """
        Set the border width of the CompositeView.

        The border width of a CompositeView is the amount of space to
        leave around the outside of the container. The only exception
        to this is Window; because toplevel windows can't leave space
        outside, they leave the space inside. The border is added on
        all sides of the container.
        

        Returns the result of the delegation (i.e., True if delegates
        agreed to doing it). Raises a CompositeViewError if anything
        bad happens.
        """
        if self.delegate('will_set_border_width', args=width):
            try:
                self._doSetBorderWidth(width)
            except:
                raise CompositeViewError, _("Unable to set border width")
            return True
        return False
    def getBorderWidth(self):
        """
        Return the requested border width.
        """
        return self._doGetBorderWidth()
            
    def busy(self):
        """
        Same as View.busy, but for composites.
        """
        if self.delegate('will_busy'):
            try:
                self._doBusy()
                for i in self._children:
                    i.busy()
            except:
                raise CompositeViewError, _("Unable to busy")
            return True
        return False
    def idle(self):
        """
        Same as View.idle, but for composites.
        """
        if self.delegate('will_idle'):
            try:
                self._doIdle()
                for i in self._children:
                    i.idle()
            except:
                raise CompositeViewError, _("Unable to idle")
            return True
        return False

    def show (self):
        """
        Same as View.show, but for composites.
        """
        super (CompositeView, self).show ()
        for i in self._children:
            i.show ()
    def hide (self):
        """
        Same as View.hide, but for composites.
        """
        super (CompositeView, self).hide ()
        for i in self._children:
            i.hide ()
