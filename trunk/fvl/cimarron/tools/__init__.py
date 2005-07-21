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
Different utility functions that don't yet warrant a class of their own.
"""

__revision__ = int('$Rev$'[5:-1])


import re

def makeName(name):
    """
    Change C{name} from underscore-delimited words to camelcase.
    """
    def __upper__(letter):
        return letter.group(1).upper()
    # some_thing
    name = re.sub(r'_([a-z])', __upper__, name)
    # someThing
    return name

def MakeName(name):
    """
    Change C{name} from lowercase camelcase to uppercase camelcase.
    """
    name = makeName(name)
    # someThing
    name = name[0:1].upper()+name[1:]
    # SomeThing
    return name

def traverse (obj, path):
    """
    Returns the object found by traversing the path
    (as a string) starting from obj.
    """
    path = path.split('.')
    while path:
        elem = path[0]
        try:
            obj = getattr(obj, elem)
        except AttributeError, e:
            if callable(obj):
                return obj(*path)
            else:
                e.args = ('while traversing %r for %r on the %r path'
                          % (obj, elem, path), )
                raise
        del path[0]
    return obj
