# -*- python -*- coding: ISO-8859-1 -*-
# Copyright 2004 Fundacion Via Libre
#
# This file is part of PAPO.
# 
# PAPO is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
# 
# PAPO is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with PAPO; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA

import operator, sys
from Config import Config, _
from Utils import Debug
# Debug.sections.append ('Responder')

__all__ = ('Failed', 'Reject', 'Unknown', 'Accept', 'Done',
           'Responder')

Failed, Reject, Unknown, Accept, Done = -2, -1, 0, 1, 2

from Exceptions import ResponderError
from Composite import Composite

class Responder(Config):
    """
    Anything that has a parent and delegates.

    Keyword arguments:
    """
    __kwargs = ('parent',)
    __doc__ += "%s\n" % (__kwargs,)
    __obligs = {'_parent': lambda:None,
                '_delegates': list,
                '_delegate_argses': dict}
    def __init__(self, **kw):
        self._processArgs(Responder, kw)

    def getParent(self):
        return getattr(self, '_parent', None)
    def setParent(self, parent):
        self.debug ('setting parent of %s to %s' % (self, parent))

        # child handling
        if parent is None:
            if hasattr (self._parent, 'removeChild'):
                self.debug ('parent is None, removing child')
                self._parent.removeChild (self)
        else:
            if hasattr (parent, 'addChild'):
                # do the inverse link first
                self.debug ('adding child')
                parent.addChild (self)
        self._parent = parent

    def addDelegation(self, delegate, delegate_args=None):
        self._delegates.append(delegate)
        self._delegate_argses[delegate] = delegate_args
    def removeDelegation(self, delegate):
        self._delegates.remove(delegate)
        del self._delegate_argses[delegate]
    def delegate(self, message, comp=None, unknown=None, null=None, args=None):
        """
        The default delegation is with 'or', i.e. any 'Accept' is
        enough, 'Unknown' is True, and null the same as 'Unknown'.

        Parameters are:

           comp     composition operator
           unknown  value of 'Unknown'
           null     value of empty delegation list
           args     extra args to be passed on delegation

        """
        if comp is None:
            comp = operator.or_
        if null is None:
            null = unknown
            
        if self._delegates:
            res = unknown
            for i in self._delegates:
                if hasattr(i, message):
                    rv = getattr(i, message)(self, args, self._delegate_argses[i])
                    b = rv > 0 or (rv >= 0 and unknown)
                else:
                    b = rv = unknown
                if rv and abs(rv)==2:
                    res = b
                    break
                if res is unknown:
                    res = b
                elif b is not unknown:
                    res = comp(res, b)
        else:
            res = null
        if res is None:
            res = True
        return res
    
