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

from Utils import Debug
# Debug.sections.append ('Composite')

from Utils.MagicArgs import MagicArgs

class Composite(MagicArgs):
    """
    An object that acts as a container of objects of the same
    class. 'Composite' implements container management functions, and
    forwards everything else on to its children.

    Additional keyword args:
    """
    __kwargs = ('children', )
    __doc__ += "%s\n" % (__kwargs,)
    __obligs = {'_children': list,
                }

    def getChildren(self):
        """
        Returns a list of children.
        """
        return self._children

    def getChildrenRecursively(self):
        """
        Recursively find all children that are not themselves
        'Composite's.
        """
        children = []
        for i in self.getChildren():
            if isinstance(i, Composite):
                children.extend(i.getChildrenRecursively())
            else:
                children.append(i)
        return children
    def getDescendantsTree(self):
        """
        [self, [descendantsTree of all children]]
        """
        tree = []
        for i in self.getChildren():
            if isinstance(i, Composite):
                tree.append(i.getDescendantsTree())
            else:
                tree.append(i)
        return [self, tree]
    def getDescendants(self):
        """
        [self, descendants of all children]
        """
        descendants = [self]
        for i in self.getChildren():
            if isinstance(i, Composite):
                descendants.extend(i.getDescendants())
            else:
                descendants.append(i)
        return descendants
    def findDescendants(self, cond):
        """
        [descendants (_not_ tree) filtered by cond] 

        less memory-hungry than filter(cond, x.getDescendants())
        """
        descendants = []
        if cond(self):
            descendants.append(self)
        for i in self.getChildren():
            if cond(i):
                descendants.append(i)
            if isinstance(i, Composite):
                descendants.extend(i.findDescendants(cond))
        return descendants

    def addChild(self, child):
        """
        Add a child to the container.

        You should not call this. Call setParent() in the child instead.
        """
        self._children.append(child)

    def removeChild(self, child):
        """
        Remove a child from the container.

        You should not call this. Call setParent(None) in the child instead.
        """
        self._children.remove(child)
