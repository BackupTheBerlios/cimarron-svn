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
from Exceptions import WindowError

class Window(CompositeView):
    """
    The toplevel widget.

    Additional keyword arguments:
    """
    __kwargs = ('title',)
    __doc__ += "%s\n" % (__kwargs,)

    def getWindow(self):
        """
        Get the toplevel widget. That's me.
        """
        return self

    def setTitle(self, title):
        """
        Set the title of the Window.

        Returns the result of the delegation (i.e., True if delegates
        agreed to doing it). Raises a WindowError if anything bad
        happens.
        """
        if self.delegate('will_set_title', args=title):
            try:
                title = unicode(title)
                self._doSetTitle(title)
            except:
                raise WindowError, _("Unable to set title")
            return True
        return False

    def getTitle(self):
        """
        Gets the title of the Window.
        """
        return self._doGetTitle()
        
    def pushStatus(self, status, timeout=0, icon='ok'):
        """
        Push a message onto the status area.

        Parameters:
          message  The message to be pushed
          timeout  How many seconds to leave display it,
                   0 for 'for ever'.
          icon     If possible, give the user feedback as to the
                   nature of the message. 
                   One of "ok", "nok", "warn", and "error".


        Returns a handle that can be used to remove the message later
        on, if the delegation succeeds, and False otherwise. The
        handle is True, booleanly.
        """
        if self.delegate('will_push_status', args=(status, timeout, icon)):
            try:
                return self._doPushStatus(status, timeout, icon)
            except:
                raise WindowError, _("Unable to push status")
        return False

    def popStatus(self):
        """
        Remove the last message pushed onto the status area.

        Returns the result of the delegation (i.e., True if delegates
        agreed to doing it). Raises a WindowError if anything bad
        happens.
        """
        if self.delegate('will_pop_status'):
            try:
                self._doPopStatus()
            except:
                raise WindowError, _("Unable to pop status")
            return True
        return False

    def removeStatus(self, msgid):
        """
        Remove a specific message from the status area.

        Returns the result of the delegation (i.e., True if delegates
        agreed to doing it). Raises a WindowError if anything bad
        happens.
        """
        if self.delegate('will_remove_status', args=msgid):
            try:
                self._doRemoveStatus(msgid)
            except:
                raise WindowError, _("Unable to remove status")
            return True
        return False

    def delete(self):
        """
        Delete the window: hide it, and remove it from the
        application.

        This is *not* destroy().

        Returns the result of the delegation (i.e., True if delegates
        agreed to doing it). Raises a WindowError if anything bad
        happens.
        """
        if self.delegate('will_delete'):
            try:
                self._doHide()
                self._doDelete()
            except:
                raise WindowError, _("Unable to delete")
            return True
        return False
