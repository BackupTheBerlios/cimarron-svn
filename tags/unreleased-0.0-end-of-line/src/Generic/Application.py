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
# Debug.sections.append ('Application')

from CompositeResponder import CompositeResponder

class Application(CompositeResponder):
    """
    Applications are objects whose only purpose is to coordinate the
    windows. In other words, controllers needing to ensure that their
    windows behave in some manner, e.g. not allowing the user to close
    window A before window B is finished, would install delegates in A
    and B's (common) Application.

    The other job of applications is to set up and destroy the
    environment the widgets expect; in Gtk that would be starting the
    main loop; in curses, doing initscr; etc.

    The utility of having two applications is... unexplored. However,
    it is not a singleton, so you can try it yourself. Probably not
    useful for much.
    """
    def run(self):
        """
        Set up the environment the Views expect; start the ball
        rolling.
        """
        self._doRun()

    def stop(self):
        """
        Destroy the environment; puncture the ball.
        """
        self._doStop()

    def removeChild(self, child):
        """
        Remove a child.

        Do not call this, call child.setParent (None) instead
        """
        if self.delegate('will_remove_child', args=child):
            self.debug ('will_remove_child')
            super (Application, self).removeChild (child)
            if not self.shownChildren():
                self.stop()
            return True
        return False
        
    def shownChildren (self):
        return [x for x in self._children if x.isShown ()]
