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
# Debug.sections.append ('CompositeResponder')

from Responder import Responder, _
from Composite import Composite
from Exceptions import CompositionError

class CompositeResponder(Responder, Composite):
    """
    A container that has delegates.
    """
    def addChild(self, child):
        """
        Add a child to the container. Returns the result of the
        delegation.

        Do not call this, call child.setParent (self) instead
        """
        self.debug ('%s is adding %s' % (self, child))
        if child.getParent() is not None:
            raise CompositionError, _("Child is already parented")
        if self.delegate('will_add_child', args=child):
            super(CompositeResponder, self).addChild(child)
            if hasattr (self, '_doAddChild'):
                try:
                    self._doAddChild(child)
                except:
                    # failed, undo
                    super(CompositeResponder, self).removeChild(child)
                    raise
            return True
        return False

    def removeChild(self, child):
        """
        Remove a child from the container. Returns the result of the
        delegation

        Do not call this, call child.setParent (None) instead
        """
        if child.getParent() is not self:
            raise CompositionError, _("Child is not in parent")
        if self.delegate('will_remove_child', args=child):
            self.debug ('will_remove_child %s from %s' % (child, self))
            if hasattr (self, '_doRemoveChild'):
                self._doRemoveChild(child)
            super(CompositeResponder, self).removeChild(child)
            return True
        return False
