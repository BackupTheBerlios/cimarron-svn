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

from TextEntry import TextEntry
from Exceptions import NumEntryError

class NumEntry(TextEntry):
    """
    NumEntries are entries for numerical values.

    Additional keyword arguments:
    """
    __kwargs = {'range': (0, 100),
                'increments': (1, 10),
                'digits': 1,
                }
    __doc__ += "%s\n" % (__kwargs.keys(),)

    def setRange(self, *nums):
        """
        The Range of a NumEntry is the interval that contains valid
        values for the entry.

        It takes a 2-tuple (min, max), or two args min, max.

        Returns the result of the delegation; raises NumEntryError on
        error.
        """
        try:
            min_num, max_num = nums
        except ValueError:
            min_num, max_num = nums[0]
        if self.delegate('will_set_range', args=(min_num, max_num)):
            try:
                self._doSetRange(min_num, max_num)
            except:
                raise NumEntryError, _("Unable to set range")
            return True
        return False
    def getRange(self):
        return self._doGetRange()

    def setIncrements(self, *incs):
        try:
            pri, sec = incs
        except ValueError:
            pri, sec = incs[0]
        if self.delegate('will_set_increments', args=(pri, sec)):
            try:
                self._doSetIncrements(pri, sec)
            except:
                raise NumEntryError, _("Unable to set range")
            return True
        return False
    def getIncrements(self):
        return self._doGetIncrements()

    def setDigits(self, digits):
        if self.delegate('will_set_digits', args=digits):
            self._doSetDigits(digits)
    def getDigits(self):
        return self._doGetDigits()

