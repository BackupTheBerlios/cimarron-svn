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

from Control import Control
from Exceptions import BoolEntryError

class BoolEntry (Control):
    """
    A BoolEntry is a checkbox, with an optional label. It has three
    possible values: True, False, and None. None is used to indicate
    `inconsistent', whose meaning is application specific, and is only
    settable by the application, not the user.
    """
    __kwargs = ('label', 'inconsistent')
        
    def setLabel(self, label):
        """
        Change the label part of the caption. Only text.
        """
        if self.delegate ('will_set_label'):
            try:
                self._doSetLabel(label)
            except:
                raise BoolEntryError, _("Unable to set label")
            return True
        return False

    def setInconsistent(self, inconsistent):
        """
        Mark the checkbox as inconsistent; this is some kind of
        in-between state, that
        """
        if self.delegate('will_set_inconsistent', args=inconsistent):
            try:
                self._doSetInconsistent(inconsistent)
            except:
                if inconsistent:
                    raise BoolEntryError, \
                          _("Unable to set `inconsistent' flag")
                else:
                    raise BoolEntryError, \
                          _("Unable to clear `inconsistent' flag")
            return True
        return False

    def getInconsistent(self):
        return self._doGetInconsistent()

    def getValue (self):
        if self.getInconsistent():
            return None
        else:
            return self._doGetValue ()
    def setValue (self, value):
        if value is None:
            self.setInconsistent(True)
        else:
            self.setInconsistent(False)
            self._doSetValue(bool(value))
