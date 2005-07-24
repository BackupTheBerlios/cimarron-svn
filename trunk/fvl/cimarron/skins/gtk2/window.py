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

"""
Here you'll find the gtk2 skin's Window class.
"""

__revision__ = int('$Rev$'[5:-1])

import os
import inspect
import logging
logger = logging.getLogger('fvl.cimarron.skins.gtk2.window')

from zope import interface
import gtk
import pango

from fvl.cimarron.skins.common import Container
from fvl.cimarron.interfaces import IWindow
from fvl.cimarron.skins.gtk2.mixin import GtkVisibilityMixin

class Window(GtkVisibilityMixin, Container):
    """
    A Window. Duh.
    """
    interface.implements(IWindow)
    
    def __init__(self, title='', size=(-1, -1), **kwargs):
        """
        @param title: the title for the window.
        """
        if '_widget' not in self.__dict__:
            self._widget = gtk.Window()
        super(Window, self).__init__(**kwargs)

        self._widget.connect('delete-event', self._delete_callback)
        self.title = title
        self.size = size

    def _delete_callback(self, *ignore):
        """
        Called when a window is deleted from the window manager.  We
        should to hide the window, and stop gtk from destroying it.
        """
        self.hide()
        return True


    def _set_title(self, title):
        """
        Set the window's title. C{title} must be a unicode object.
        """
        self._widget.set_title(title)
    def _get_title(self):
        """
        Get the window's title.
        """
        return self._widget.get_title()
    title = property(_get_title, _set_title,
                     doc="""The title for the window.""")

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
        """
        Try to guess the size of a character cell.

        The window size is specified in cells.
        """
        ctx = self._widget.get_pango_context()
        metrics = ctx.get_metrics(ctx.get_font_description())
        cell = ( float(metrics.get_approximate_char_width()) / pango.SCALE,
                 float(metrics.get_ascent()
                       + metrics.get_descent()) / pango.SCALE )
        return cell

    def _get_size(self):
        """
        Get the window size, in cells.
        """
        size = self._widget.get_size()
        if size != (-1, -1):
            cell = self._get_cell_size()
            size = int(size[0] / cell[0]), int(size[1] / cell[1])
        return size
    def _set_size(self, (width, height)):
        """
        Try to set the window size, in cells.

        The window might not be able to change size.
        """
        if (width, height) != (-1, -1):
            cell = self._get_cell_size()
            width = int(width * cell[0])
            height = int(height * cell[1])
        self._widget.set_size_request(width, height)
    size = property(_get_size, _set_size)
