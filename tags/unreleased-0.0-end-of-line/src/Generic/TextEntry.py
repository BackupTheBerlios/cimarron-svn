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

from StatefulControl import StatefulControl, _

class TextEntry(StatefulControl):
    _default_value = ''
    def setMaxLength(self, max_len):
        if self.delegate('will_set_max_length', args=max_len):
            self._doSetMaxLength(max_len)
    def getMaxLength(self):
        return self._doGetMaxLength()

    def setEditable(self, editable=True):
        if self.delegate('will_set_editable', args=editable):
            self._doSetEditable(editable)
    def getEditable(self):
        return self._doGetEditable()

    def frame(self):
        if self.delegate('will_frame'):
            self._doFrame()
    def unframe(self):
        if self.delegate('will_unframe'):
            self._doUnframe()
    def hasFrame(self):
        return self._doHasFrame()

