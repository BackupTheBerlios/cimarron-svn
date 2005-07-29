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
The default (and currently only) skin, based on Gtk version 2.4 or above.
"""

__revision__ = int('$Rev$'[5:-1])

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

def _splash():
    _splash_win = win = gtk.Window()
    win.set_type_hint(gtk.gdk.WINDOW_TYPE_HINT_SPLASHSCREEN)
    win.set_title('Cimarrón splash')
    win.set_size_request(200, 100)
    win.set_position(gtk.WIN_POS_CENTER_ALWAYS)

    lbl = gtk.Label()
    lbl.set_text('Loading...')
    lbl.set_alignment(1, 1)

    gtk.window_set_auto_startup_notification(False)
    win.add(lbl)
    win.show_all()
    while gtk.events_pending(): gtk.main_iteration()
    gtk.window_set_auto_startup_notification(True)
    _splash_win.hide()
_splash()

def _run():
    """
    Fills the hook for L{Application.run}
    """
    gtk.main()

def _quit():
    """
    Fills the hook for L{Application.quit}
    """
    if gtk.main_level():
        gtk.main_quit()

def _schedule(timeout, callback, repeat=0):
    """
    Fills the hook for L{Application.schedule}
    """
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
    if '_outerWidget' in child.__dict__:
        # print 'parenting', parent, child,
        if '_innerWidget' in parent.__dict__:
            # print 'concreted'
            try:
                packer = parent._innerWidget.pack_start
            except AttributeError:
                # maybe it's a Window?
                parent._innerWidget.add(child._outerWidget)
                parent._innerWidget.set_border_width(child.border)
            else:
                try:
                    packer(child._outerWidget, child.expand, child.fill,
                           child.border)
                except:
                    print `child`
        else:
            if parent.parent is None:
                # print 'postponed'
                try:
                    parent._childrenToParent.append (child)
                except AttributeError:
                    parent._childrenToParent = [child]
            else:
                # print 'forwarded to', parent.parent
                parent.parent._concreteParenter (child)

moduleProvides(ISkin)
