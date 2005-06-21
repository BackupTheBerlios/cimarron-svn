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

import re

def makeName (name):
    def __upper__ (letter):
        return letter.group (1).upper ()
    # some_thing
    name= re.sub (r'_([a-z])', __upper__, name)
    # someThing
    return name

def MakeName (name):
    name= makeName (name)
    # someThing
    name= name[0:1].upper ()+name[1:]
    # SomeThing
    return name

simple_types = (str, unicode, type(None), bool, int, long, float, complex )

def is_simple(obj):
    t = type(obj)

    return (t in simple_types # really simple
            or ( t in (tuple, list) and 
                 len(filter(None, map(is_simple, obj))) == len(obj)) # composite of simples
            or ( t is dict and
                 len(filter(None, map(is_simple, obj.keys()))) == \
                 len(filter(None, map(is_simple, obj.values()))) == len(obj))
            )
                 

def traverse (obj, path):
    """
    Returns the object found by traversing the path
    (as a string) starting from obj.
    """
    for e in path.split ('.'):
        obj= getattr (obj, e)

    return obj
