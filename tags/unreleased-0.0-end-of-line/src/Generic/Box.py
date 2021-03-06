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
from Exceptions import BoxError

class Box(CompositeView):
    """
    Base class for box containers.

    Keyword arguments, in addition to those in the base classes, are:
    """
    __kwargs = ('spacing', 'homogeneous')
    __doc__ += "%s\n" % (__kwargs,)
      
    def setSpacing(self, spacing):
        """
        Set the number of pixels to place between children.

        Argument is an integer number (the number of pixels).

        Returns the result of the delegation (i.e., True if delegates
        agreed to doing it). Raises a BoxError if anything bad
        happens.
        """
        if self.delegate('will_set_spacing', args=spacing):
            try:
                self._doSetSpacing(spacing)
            except:
                raise BoxError, _("Unable to set spacing")
            return True
        return False

    def getSpacing(self):
        """
        Return the requested child spacing.
        """
        return self._doGetSpacing()

    def setHomogeneous(self, homogeneous):
        """
        Set whether all child widgets use the same amount of space.

        Argument is True or False.

        Returns the result of the delegation (i.e., True if delegates
        agreed to doing it). Raises a BoxError if anything bad
        happens.
        """
        if self.delegate('will_set_homogeneous', args=homogeneous):
            try:
                self._doSetHomogeneous(homogeneous)
            except:
                if homogeneous:
                    raise BoxError, _("Unable to set `homogeneous' flag")
                else:
                    raise BoxError, _("Unable to clear `homogeneous' flag")
            return True
        return False
    def getHomogeneous(self):
        """
        Retrieve the requested geneousosity.
        """
        return self._doGetHomogeneous()
