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

import gtk
import operator

from Generic.Dialog import Dialog
from Gtk2Window import Gtk2Window
from Generic.Control import Control

class Gtk2Dialog (Dialog, Gtk2Window):
    _defaultTitle = 'dialog'
    def __init__ (self, **kw):
        if kw.has_key('title'):
            title = kw['title']
            del kw['title']
        else:
            title = self._defaultTitle
        if not hasattr(self, '_obj'):
            self._obj= gtk.Dialog (title, None, gtk.DIALOG_MODAL|gtk.DIALOG_NO_SEPARATOR)
        if not hasattr(self, '_default'):
            self._default = None

        self._obj.set_border_width(12)
        self._obj.vbox.set_spacing(12)
        super (Gtk2Dialog, self).__init__ (**kw)
        self._obj.connect ('response', self.__response)
        
    def _doSetContents(self, contents):
        for i in self._obj.vbox.get_children()[:-1]:
            self._obj.vbox.remove(i)
        self._obj.vbox.add (contents._obj)
    def _doSetButtons(self, buttons):
        for i in self._obj.action_area.get_children():
            self._obj.action_area.remove(i)
        for button in buttons:
            self._obj.add_action_widget (button._obj, button.getValue ())
    def _doSetDefault(self, default):
        if isinstance(default, Control):
            self._default = default
            default = default.getValue()
            
        self._obj.set_default_response (default)

    def _doSetParent (self, parent):
        self._parent= parent
        self._obj.set_transient_for (parent._obj)
        
    def _doRun (self):
        # from gtk's doc:
        # Before entering the recursive main loop, gtk_dialog_run() calls gtk_widget_show() on the dialog for you.
        # Note that you still need to show any children of the dialog yourself. 
        self.show ()
        if self._default:
            self._default._obj.grab_default()
            self._default._obj.grab_focus()
        parent = self.getParent()
        if parent:
            parent.disable ()
        try:
            ans= self._obj.run ()
        finally:
            if parent:
                parent.enable ()
        return ans

    def __response (self, *a):
        self.hide ()
