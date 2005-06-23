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
L{cimarron} is...
"""
import sys

from zope.schema import Object
from zope.interface.verify import verifyObject, verifyClass

from fvl.cimarron.interfaces import ISkin

DEFAULT_SKIN_NAME = 'gtk2'

def config(skin_name=DEFAULT_SKIN_NAME):
    """

    Although currently a function, L{config} will probably become a class
    because we strongly suspect people will want to actually do some
    configuration loading here. In fact, one thing we learned while
    implementing the first Cimarrón is that a lot of functionality is actually
    too installation-dependant to I{not} keep it in a configuration file
    somewhere (an example of this is, of course, the default skin name).

    This Cimarrón is at this time much leaner than its previous incarnation,
    and thus the only work done by L{config} is the choosing of the
    appropriate skin (and loading thereof). Expect this to change as the
    L{Controller <cimarron.controllers.Controller>}s and L{Widget
    <cimarron.skins.common.Widget>}s are filled out.

    @param skin_name: the name of the skin to load
    @type skin_name: str
    """
    global skin
    try:
        skin
    except NameError:
        skin = __import__('fvl.cimarron.skins.' + skin_name,
                          globals(), locals(), skin_name)
        verifyObject(ISkin, skin)
        for name, desc in ISkin.namesAndDescriptions(1):
            if isinstance(desc, Object):
                verifyClass(desc.schema, getattr(skin, name))

        sys.modules['fvl.cimarron.skin'] = skin
