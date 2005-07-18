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
In fvl.cimarron.model you will find classes that aid in building
models that cooperate with cimarrón.
"""

__revision__ = int('$Rev$'[5:-1])

from fvl.cimarron.tools import traverse

class Model(object):
    """
    Model provides a very basic model for cimarron.
    """
    def getattr(self, attr):
        """
        Find the attribute referred to by 'attr', and return it.
        """
        return traverse(self, attr)
    def setattr(self, attr, value):
        """
        Find the attribute referred to by 'attr', and set it to 'value'.
        """
        pos = attr.rfind('.')
        if pos > -1:
            path = attr[:pos]
            attr = attr[pos+1:]
            obj = traverse(self, path)
        else:
            obj = self
        return setattr(obj, attr, value)

    def values(cls, trans, **qual):
        ans = trans.search(cls, **qual)
    return ans
    values = classmethod(values)
