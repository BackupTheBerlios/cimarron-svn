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

from Box import Box, _
from Exceptions import ButtonBoxError

class ButtonBox(Box):
    """
    Base class for button boxes.

    Keyword arguments, in addition to those in the base classes, are:
    """
    __kwargs = ('layout', 'minChildSize', 'internalPadding')
    __doc__ += "%s\n" % (__kwargs,)

    def setLayout(self, layout_style):
        """
        Change the way the buttons are arrange in the container.

        layout_style can be one of:
          'default':  reset to default
           'spread':  buttons are evenly spread across the ButtonBox
             'edge':  buttons are placed at the edges of the ButtonBox.
            'start':  buttons are grouped towards the start of box.
              'end':  buttons are grouped towards the end of a box.

        Returns the result of the delegation (i.e., True if delegates
        agreed to doing it). Raises a ButtonBoxError if anything bad
        happens.
        """
        if self.delegate('will_set_layout', args=layout_style):
            try:
                self._doSetLayout(layout_style)
            except:
                raise ButtonBoxError, _("Unable to set layout style")
            return True
        return False

    def getLayout(self):
        """
        Return the currently requested layout.
        """
        return self._doGetLayout()

    def setMinChildSize(self, *mins):
        """
        Set the minimum size of child widgets.

        Argument is a 2-tuple of ints, or two ints.

        Returns the result of the delegation (i.e., True if delegates
        agreed to doing it). Raises a ButtonBoxError if anything bad
        happens.
        """
        try:
            min_width, min_height = mins
        except ValueError:
            min_width, min_height = mins[0]
        if self.delegate('will_set_child_size', args=(min_width, min_height)):
            try:
                self._doSetMinChildSize(min_width, min_height)
            except:
                raise ButtonBoxError, _("Unable to set minimum child size")
            return True
        return False

    def getMinChildSize(self):
        """
        Get the requested minimum size of child widgets.
        """
        return self._doGetMinChildSize()
    
    def setChildSecondary(self, child, is_secondary):
        """
        Set whether child should appear in a secondary group of
        children.

        A typical use of a secondary child is the help button in a
        dialog.

        Takes one argument, True or False.
        
        Returns the result of the delegation (i.e., True if delegates
        agreed to doing it). Raises a ButtonBoxError if anything bad
        happens.
        """
        if self.delegate('will_set_child_secondary',
                         args=(child, is_secondary)):
            try:
                self._doSetChildSecondary(child, is_secondary)
            except:
                raise ButtonBoxError, _("Unable to set child as secondary")
            return True
        return False

    def getChildSecondary(self, child):
        """
        Get whether a child is secondary or not.
        """
        return self._doGetChildSecondary(child)
    
    def setInternalPadding(self, *pads):
        """
        Change the amount of internal padding used by all buttons.

        Argument is a 2-tuple of ints, or two ints.
        
        Returns the result of the delegation (i.e., True if delegates
        agreed to doing it). Raises a ButtonBoxError if anything bad
        happens.
        """
        try:
            xpad, ypad = pads
        except ValueError:
            xpad, ypad = pads[0]
        if self.delegate('will_set_internal_padding', args=(xpad, ypad)):
            try:
                self._doSetInternalPadding(xpad, ypad)
            except:
                raise ButtonBoxError, _("Unable to set internal padding")
            return True
        return False

    def getInternalPadding(self):
        """
        Get the currently requested internal padding.
        """
        return self._doGetInternalPadding()
