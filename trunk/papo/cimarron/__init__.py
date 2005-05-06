# -*- coding: utf-8 -*-
#
# Copyright 2003 Fundación Via Libre
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

import new
import libxml2

DEFAULT_SKIN_NAME = 'gtk2'

class config(object):
    def __init__(self, skin_name=DEFAULT_SKIN_NAME):
        global skin
        skin = __import__('papo.cimarron.skins.' + skin_name,
                          globals(), locals(), skin_name)


def fromXmlObj(xmlObj, parent=None):
    if isinstance(xmlObj, libxml2.xmlDoc):
        # get at root element
        xmlObj = xmlObj.children
    obj = getattr(skin, xmlObj.name)()
    prop = xmlObj.properties
    while prop:
        setattr(obj, prop.name, eval(prop.content))
        prop = prop.next
    if parent is not None:
        obj.parent = parent
    xmlObj = xmlObj.children
    while xmlObj:
        fromXmlObj(xmlObj, parent=obj)
        xmlObj = xmlObj.next
            
    return obj
