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

import os
import inspect
import logging
logger = logging.getLogger('fvl.cimarron.skins.gtk2.window')

from zope import interface
import gtk
import pango

from fvl.cimarron.skins.common import Container
from fvl.cimarron.interfaces import IWindow

from mixin import GtkVisibilityMixin

class Window(GtkVisibilityMixin, Container):
    """
    A Window. Duh.
    """
    interface.implements(IWindow)
    
    def __init__(self, title='', size=(-1,-1), **kw):
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
        self.size = size

    def _set_title(self, title):
        self._widget.set_title(title)
    def _get_title(self):
        return self._widget.get_title()
    title = property(_get_title, _set_title, None, """The title for the window.""")

    def screenshot(self, filename=None, frame=True):
        """
        Take a screenshot of the window.

        Store the image in file <filename>.

        If <filename> isn't given, use the filename of the caller with
        '.png' appended.

        If <frame> is true, include the windowmanager frames.

        """
        xid = self._widget.window.xid
        if filename is None:
            filename = inspect.stack()[1][1] + '.png'
        if frame:
            cmd = 'import -frame -window %d %s'
        else:
            cmd = 'import -window %d %s'
        os.system(cmd % (xid, filename))

    def _get_cell_size(self):
        ctx = self._widget.get_pango_context()
        metrics = ctx.get_metrics(ctx.get_font_description())
        cell = ( float(metrics.get_approximate_char_width()) / pango.SCALE,
                 float(metrics.get_ascent() + metrics.get_descent()) / pango.SCALE )
        return cell

    def _get_size(self):
        size = self._widget.get_size()
        if size != (-1,-1):
            cell = self._get_cell_size()
            size = int(size[0] / cell[0]), int(size[1] / cell[1])
        return size
    def _set_size(self, (width, height)):
        if (width, height) != (-1,-1):
            cell = self._get_cell_size()
            width = int(width * cell[0])
            height = int(height * cell[1])
        self._widget.set_size_request(width, height)
    size = property(_get_size, _set_size)
