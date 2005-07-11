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
Several widgets that are L{Container}s.
"""

__revision__ = int('$Rev$'[5:-1])

import logging
logger = logging.getLogger('fvl.cimarron.skins.gtk2.container')

import gtk

from fvl.cimarron.skins.common import Container

class VBox(Container):
    """
    A vertical container. The children of this object
    will be placed one on top of the other.
    """
    def __init__ (self, **kwargs):
        self._widget = gtk.VBox()
        # self._widget.set_border_width (5)
        self._widget.set_spacing (5)
        super(VBox, self).__init__(**kwargs)

class HBox(Container):
    """
    A horizontal container. The children of this object
    will be placed from left to right.
    """
    def __init__ (self, **kwargs):
        self._widget = gtk.HBox()
        # self._widget.set_border_width (5)
        self._widget.set_spacing(5)
        super(HBox, self).__init__(**kwargs)

class Notebook (Container):
    """
    A container where all the children are put in `tabs´ and
    only one of them is shown at any given time.
    """
    def __init__ (self, **kwargs):
        self._widget = gtk.Notebook()
        super(Notebook, self).__init__(**kwargs)
        self._widget.connect('change-current-page', self.__change_page)

    def activate (self, other):
        """
        Show a particular tab.

        @param other: either the child to show or
            the index of the child.
        """
        if type (other)==int:
            # assume it's the page no
            pageNo = other
        else:
            # assume it's a child
            pageNo = self._children.index(other)
        if 0 <= pageNo and pageNo < len(self._children) \
               and self.delegate('will_change_page'):
            self._widget.set_current_page(pageNo)

    def _concreteParenter (self, child):
        """
        See L{fvl.cimarron.skins.gtk2._concreteParenter}
        """
        super(Notebook, self)._concreteParenter(child)
        if getattr(child, '_widget', None):
            label = gtk.Label()
            label.set_text(child.label)
            self._widget.set_tab_label(child._widget, label)

    def __change_page (self, *ignore):
        """
        Makes that page switching
        """
        return self.delegate('will_change_page')

