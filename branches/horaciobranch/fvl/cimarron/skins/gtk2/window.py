# -*- coding: utf-8 -*-
#
# Copyright 2003, 2004, 2005 Fundación Via Libre
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

import logging
logger = logging.getLogger('fvl.cimarron.skins.gtk2.window')

from zope import interface
import gtk

from fvl.cimarron.skins.common import Container
from fvl.cimarron.interfaces import IWindow

from mixin import GtkVisibilityMixin

class Window(GtkVisibilityMixin, Container):
    """
    A Window. Duh.
    """
    interface.implements(IWindow)
    
    def __init__(self, title='', **kw):
        """
        @param title: the title for the window.
        """
        self._widget = gtk.Window()
        super(Window, self).__init__(**kw)

        def delete_callback(*a):
            self.hide()
            return True

        self._widget.connect('delete-event', delete_callback)
        self.title = title

    def _set_title(self, title):
        self._widget.set_title(title)
    def _get_title(self):
        return self._widget.get_title()
    title = property(_get_title, _set_title, None, """The title for the window.""")

