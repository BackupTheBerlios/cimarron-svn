# -*- coding: utf-8 -*-
#
# Copyright 2005 Fundación Via Libre
#
# This file is part of PAPO.
#
# PAPO is free software; you can redistribute it and/or modify it under the
# terms of the GNU General Public License as published by the Free Software
# Foundation; either version 2 of the License, or (at your option) any later
# version.
#
# PAPO is distributed in the hope that it will be useful, but WITHOUT ANY
# WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
# FOR A PARTICULAR PURPOSE.  See the GNU General Public License for more
# details.
#
# You should have received a copy of the GNU General Public License along with
# PAPO; if not, write to the Free Software Foundation, Inc., 59 Temple Place,
# Suite 330, Boston, MA 02111-1307 USA
"""
In here you'll find the mithical L{Application}
"""

__revision__ = int('$Rev$'[5:-1])

import logging

from fvl import cimarron
from fvl.cimarron.skins.common import Unknown, ForcedYes
from fvl.cimarron.controllers.base import Controller

__all__ = ('Application',)

logger = logging.getLogger('fvl.cimarron.controllers.app')

class WindowContainer(list):
    """
    Not public. Please Ignore :)
    """
    def __init__(self, controller):
        super(WindowContainer, self).__init__()
        self.__controller = controller
    def append(self, window):
        super(WindowContainer, self).append(window)
        window.delegates.append(self.__controller)

class Application(Controller):
    """
    An Application represents the main loop of the application.
    It is the C{parent} for the first B{Window}s.
    """
    def __init__(self, **kwargs):
        assert 'parent' not in kwargs, 'Application should have no parent'
        super(Application, self).__init__(**kwargs)
        self._children = WindowContainer(self)

    def run(self):
        """
        Run the Application. Will actually show any shown window,
        and keep runnuing until:
          - all the windows are closed, or
          - someone calls C{quit()} and no window opposes
            to the action.
        """
        cimarron.skin._run()

    def quit(self):
        """
        Terminates the Application.
        """
        cimarron.skin._quit()

    def will_hide(self, window):
        """
        Somebody asked us to close the
        L{Window<fvl.cimarron.skins.gtk2.Window>}. Can we?
        """
        if len([i for i in self._children if i.visible])==1:
            self.quit()
            return ForcedYes
        return Unknown

    def schedule(self, timeout, callback, repeat=False):
        """
        Add a new timer for the app. When the C{timeout} expires,
        the C{callback} gets called.
        """
        return cimarron.skin._schedule(timeout, callback, repeat)

    def _concreteParenter (self, child):
        """
        Dummy override of L{Widget._concreteParenter
        <fvl.cimarron.skins.common.Widget._concreteParenter>}.
        """

    def refresh(self):
        """
        Dummy override of L{Control.refresh
        <fvl.cimarron.skins.common.Control.refresh>}
        """

