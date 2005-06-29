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
logger = logging.getLogger('fvl.cimarron.skins.gtk2.mixin')

class GtkVisibilityMixin(object):
    """
    Mixin that lets show and hide the object.
    Used only by Window.
    """
    def _get_visible(self):
        w = self._widget.window
        return w is not None and w.is_visible()
    visible = property(_get_visible, None, None, """""")

    def show(self):
        """
        Show the object.
        """
        self._widget.show_all()

    def hide(self):
        """
        Hide the object, after delegates agrees.
        """
        if self.delegate ('will_hide'):
            self._widget.hide_all()

class GtkFocusableMixin(object):
    """
    Mixin that delegates focus in/out and makes the object
    to be focusable programatically.
    """
    def __init__ (self, **kw):
        super (GtkFocusableMixin, self).__init__ (**kw)
        self._widget.connect ('focus-in-event', self._focusIn)
        self._widget.connect ('focus-out-event', self._focusOut)

    def _focusIn (self, *ignore):
        return not self.delegate ('will_focus_in')

    def _focusOut (self, *ignore):
        return not self.delegate ('will_focus_out')

    def focus (self):
        """
        Set the focus on this object.
        """
        self._widget.grab_focus ()

