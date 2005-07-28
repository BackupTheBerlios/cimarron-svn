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
From http://c2.com/cgi/wiki?MixIn::

    A mixin class is a parent class that is inherited from - but not
    as a means of specialization. Typically, the mixin will export
    services to a child class, but no semantics will be implied about
    the child "being a kind of" the parent.

For some examples see UserDict.DictMixin, and
http://c2.com/cgi/wiki?MixinsForPython.

In this module live gtk2-skin-specific mixins; as such, they assume
they'll be subclassed by subclasses of L{Widget}. Mixins can do that.
"""

__revision__ = int('$Rev$'[5:-1])

import logging
logger = logging.getLogger('fvl.cimarron.skins.gtk2.mixin')

class GtkVisibilityMixin(object):
    """
    Mixin that lets show and hide the object.
    """
    def _get_visible(self):
        """
        Find out whether the L{Widget} is visible.

        Currently this relies on the C{Widget} having a GdkWindow,
        which isn't true for e.g. L{Label}s.
        """
        window = self._concreteWidget.window
        return window is not None and window.is_visible()
    visible = property(_get_visible)

    def show(self):
        """
        Show the object.
        """
        self._concreteWidget.show_all()

    def hide(self):
        """
        Hide the object, after delegates agrees.
        """
        if self.delegate ('will_hide'):
            self._concreteWidget.hide_all()

class GtkFocusableMixin(object):
    """
    Mixin that delegates focus in/out and makes the object
    to be focusable programatically.
    """
    def __init__ (self, **kwargs):
        super (GtkFocusableMixin, self).__init__ (**kwargs)
        self._concreteWidget.connect ('focus-in-event', self._focusIn)
        self._concreteWidget.connect ('focus-out-event', self._focusOut)

    def _focusIn (self, *ignore):
        """
        The widget is about to receive focus.
        """
        return not self.delegate('will_focus_in')

    def _focusOut (self, *ignore):
        """
        The widget is about to lose focus.
        """
        return not self.delegate('will_focus_out')

    def focus (self):
        """
        Set the focus on this object.
        """
        self._concreteWidget.grab_focus ()

