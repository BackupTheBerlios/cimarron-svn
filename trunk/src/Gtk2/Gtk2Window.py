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
from Generic.Window import Window
from Gtk2CompositeView import Gtk2CompositeView

class Gtk2Window(Window, Gtk2CompositeView):
    __image_types = {'ok': gtk.STOCK_YES,
                     'nok': gtk.STOCK_NO,
                     'warn': gtk.STOCK_DIALOG_WARNING,
                     'error': gtk.STOCK_DIALOG_ERROR,
                     }

    def __init__(self, **kw):
        if not hasattr(self, '_obj'):
            obj = gtk.Window()
            vbox = gtk.VBox()
            hbox = gtk.HBox()
            prog = gtk.ProgressBar()
            prog.set_sensitive(False)
            prog.set_size_request(75, -1)
            prog.set_fraction(0)
            status = gtk.Statusbar()
            status.set_has_resize_grip(False)
            status.set_size_request(200, -1)
            image = gtk.Image()
            self._obj = obj
            self._vbox = vbox
            self._hbox = hbox
            self._status = status
            self._prog = prog
            self._img = image
            self._img_stack = [gtk.STOCK_YES]
            self._img_dict = {}
            image.set_from_stock(gtk.STOCK_YES, gtk.ICON_SIZE_MENU)
            obj.add(vbox)
            obj.connect('delete_event', self.__delete)
            vbox.pack_end(hbox, False, False)
            hbox.pack_start(image, False, False)
            hbox.pack_start(status, True, True)
            hbox.pack_start(prog, False, False)
        super(Gtk2Window, self).__init__(**kw)

    def startProgress(self):
        self._prog.set_sensitive(True)
        self._prog.set_fraction(0.0)
        #self._prog.set_text('wait')
    def pulseProgress(self):
        self._prog.pulse()
    def stopProgress(self):
        self._prog.set_sensitive(False)
        self._prog.set_fraction(0)
        
    def _doAddChild(self, child):
        self._vbox.add(child._obj)
    def _doRemoveChild(self, child):
        self._vbox.remove(child._obj)

    def _doSetTitle(self, title):
        self._obj.set_title(title)

    def _doHide(self):
        self._obj.hide_all()
    def _doShow(self):
        self._obj.show_all()
        super (Gtk2Window, self)._doShow ()
        
    def _doPushStatus(self, status, timeout, icon):
        icon = self.__image_types.get(icon, gtk.STOCK_MISSING_IMAGE)
        self._img_stack.append(icon)
        self._img.set_from_stock(icon, gtk.ICON_SIZE_MENU)
        msg_id = self._status.push(1, status)
        self._img_dict[msg_id] = len(self._img_stack) - 1
        if timeout:
            gtk.timeout_add(timeout*1000, lambda *a: self._doPopStatus() and False)
        return msg_id
    def _doPopStatus(self):
        self._status.pop(1)
        self._img_stack.pop()
        self._img.set_from_stock(self._img_stack[-1], gtk.ICON_SIZE_MENU)
    def _doRemoveStatus(self, msg_id):
        self._status.remove(1, msg_id)
        self._img_stack.pop(self._img_dict[msg_id])
        self._img.set_from_stock(self._img_stack[-1], gtk.ICON_SIZE_MENU)

    def __delete(self, *a):
        if not self.delete():
            # window wasn't allowed to delete itself, stop the event here
            return True
        # let the event continue
        return False

    def _doDelete(self):
        self.getParent().removeChild(self)

    def _doDisable(self):
        [i.set_sensitive(False) for i in self._vbox.get_children()
         if i is not self._hbox]
    def _doEnable(self):
        [i.set_sensitive(True) for i in self._vbox.get_children()
         if i is not self._hbox]
