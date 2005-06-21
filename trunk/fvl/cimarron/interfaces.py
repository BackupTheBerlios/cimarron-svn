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

from zope import interface, schema

class IWindow(interface.Interface):
    def __init__(title, **kw): pass
    title = interface.Attribute('')

class ISkin(interface.Interface):
    def _run():
        """
        _run() is called from App.run, to set in motion whatever
        mechanism the concrete backend uses to display widgets.
        """

    def _quit():
        """
        _quit() is called from App.quit to terminate the application;
        it might never return (or leave the backend in an unspecified
        state)
        """

    def _schedule(timeout, callback, repeat=False):
        """
        _schedule is called from App.schedule to actually do the
        scheduling of the delayed action.
        """

    def concreteParenter(parent, child):
        """
        concreteParenter dos the skin-specific magic that `glues' a
        child with its parent.
        """

    # thanks to Stephan Richter <srichter@cosmos.phy.tufts.edu>
    Window = schema.Object(
        schema = IWindow,
        title = u'Window',
        required = True,
        )
