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

from Generic.Frame import Frame
from Gtk2CompositeView import Gtk2CompositeView
import gtk

class Gtk2Frame (Frame, Gtk2CompositeView):
    def __init__ (self, **kw):
        if not hasattr(self,'_obj'):
            self._obj = gtk.Frame ()
        super (Gtk2Frame, self).__init__ (**kw)
    
    def _doSetLabel (self, label):
        self._obj.set_label (label)
    def _doGetLabel(self):
        return self._obj.get_label()
