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
from Exceptions import MiscError

class Misc(View):
    __kwargs = ('align', 'padding')
    def setAlign(self, *align):
        """
        Sets the alignment of the widget.

        one arg, a tuple, (xalign, yalign):
          xalign: the horizontal alignment, from 0 (left) to 1 (right).
          yalign: the vertical alignment, from 0 (top) to 1 (bottom).
        """
        try:
            xalign, yalign = align
        except ValueError:
            xalign, yalign = align[0]
        if self.delegate('will_align', args=(xalign, yalign)):
            try:
                self._doSetAlign(xalign, yalign)
            except:
                raise MiscError, _("Unable to set alignment")
            return True
        return False
    def getAlign(self):
        """
        returns the current alignment
        """
        return self._doGetAlign()

    def setPadding(self, *pad):
        """
        Sets the amount of space to add around the widget.

        one optional arg, a tuple (xpad, ypad):
          xpad: the amount of space to add on the left and right of the widget,
                in pixels.
          ypad: the amount of space to add on the top and bottom of the widget,
                in pixels.

        """
        try:
            xpad, ypad = pad
        except ValueError:
            xpad, ypad = pad[0]
        if self.delegate('will_pad', args=(xpad, ypad)):
            try:
                self._doSetPadding(xpad, ypad)
            except:
                raise MiscError, _("Unable to set padding")
            return True
        return False
    def getPadding(self):
        """
        returns current padding
        """
        return self._doGetPadding()
    
