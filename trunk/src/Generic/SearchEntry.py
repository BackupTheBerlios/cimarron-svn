# -*- python -*- coding ISO-8859-1 -*-
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
from Exceptions import SearchTextEntryError
from Responder import Responder

class SearchEntry(Responder):
    __kwargs = ('finder',)
    __obligs = {'_finder': lambda:None,}
    def setFinder(self, finder):
        self._finder = finder
    def getFinder(self):
        return self._finder
    def find(self, *a, **kw):
        return self._finder.finder(*a, **kw)
    def getGetter (self):
        return self._finder.getter

class SearchTextEntry(SearchEntry,TextEntry):
    def search(self, val):
        self.getParent().search(self, val)

    def notifyNotFound(self):
        self.pushStatus(_('No objects found'), timeout=2, type='nok')
        self._doNotifyNotFound()
