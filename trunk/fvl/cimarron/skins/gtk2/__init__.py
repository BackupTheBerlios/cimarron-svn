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
logger = logging.getLogger('fvl.cimarron.skins.gtk2')

import pygtk
pygtk.require('2.0')
import gtk, gobject
from zope.interface import moduleProvides

from fvl.cimarron.interfaces import ISkin, IWindow
from fvl.cimarron.skins.common import *
from fvl.cimarron.controllers import *

from mixin import *
from widget import *
from container import *
from control import *
from window import *
from grid import *

def _run():
    gtk.main()

def _quit():
    if gtk.main_level():
        gtk.main_quit()

def _schedule(timeout, callback, repeat=0):
    if repeat:
        def cb():
            callback()
            gobject.timeout_add(timeout, cb)
    else:
        cb = callback
    gobject.timeout_add(timeout, cb)

def _concreteParenter(parent, child):
    """
    Does the skin-specific magic that `glues' a child with its parent.
    Do not call directly.
    """
    if '_widget' in child.__dict__:
        # print 'parenting', parent, child,
        if '_widget' in parent.__dict__:
            # print 'concreted'
            try:
                packer = parent._widget.pack_start
            except AttributeError:
                # maybe it's a Window?
                parent._widget.add(child._widget)
                parent._widget.set_border_width(child.border)
            else:
                packer(child._widget, child.expand, child.fill, child.border)
        else:
            if parent.parent is None:
                # print 'postponed'
                try:
                    parent._childrenToParent.append (child)
                except AttributeError:
                    parent._childrenToParent= [child]
            else:
                # print 'forwarded to', parent.parent
                parent.parent._concreteParenter (child)

moduleProvides(ISkin)
