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

from Window import Window, _

class Dialog (Window):
    """
    Implements a dialog, which is a modal window with a content area
    and a button box below.  You must specify the buttons giving a
    Button list. The buttons in this list must have associated values
    that should not be negative integers; those values are used for
    window related events (such as closing).

    Additional keyword arguments:
    """
    __kwargs = ('contents', 'buttons', 'default', 'parent')
    __doc__ += "%s\n" % (__kwargs,)
        
    def setParent (self, parent):
        self._doSetParent (parent)

    def run (self):
        """
        Shows the dialog until a button from the button bar below is
        pressed or the window is closed by other means.  Returns the
        value associated to the button pressed or the negative integer
        associated to the window event.
        """
        if self.delegate ('will_run'):
            return self._doRun ()
        else:
            return None

    def setContents(self, contents):
        self._doSetContents(contents)
    def setButtons(self, buttons):
        self._doSetButtons(buttons)
    def setDefault(self, default):
        self._doSetDefault(default)
