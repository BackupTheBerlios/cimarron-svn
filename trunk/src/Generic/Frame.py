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
from Exceptions import FrameError

class Frame(CompositeView):
    """
    A bin with a decorative frame and optional label.

    Keyword arguments, in addition to those in the base classes, are:
    """
    __kwargs = ('label',)
    __doc__ += "%s\n" % (__kwargs,)
        
    def setLabel (self, text):
        """
        Set the text of the label.

        If text is None, remove the current label.

        Returns the result of the delegation (i.e., True if delegates
        agreed to doing it). Raises a FrameError if anything bad
        happens.
        """
        if self.delegate ('will_set_label', args=text):
            try:
                self._doSetLabel (unicode(text))
            except:
                raise FrameError, _("Unable to set label")
            return True
        return False

    def getLabel(self):
        return self._doGetLabel()
