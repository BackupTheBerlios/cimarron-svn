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
from Generic.Label import Label
from Generic.Exceptions import InvalidLabelJustification
from Gtk2Misc import Gtk2Misc

class Gtk2Label(Label, Gtk2Misc):
    def __init__(self, **kw):
        if not hasattr(self, '_obj'):
            # don't remove the empty string: older pygtks need it
            self._obj = gtk.Label('')
        super(Gtk2Label, self).__init__(**kw)

    def _doSetLabel(self, label):
        self._obj.set_label(label)
    def _doGetLabel(self):
        return self._obj.get_label()

    def _doSetJustify(self, justify):
        j = getattr(gtk, ("JUSTIFY_%s" % (justify,)).upper(), None)
        if j is None:
            raise InvalidLabelJustification, \
                  _("I don't know how to %s-justify") % (justify,)
        self._obj.set_justify(j)

    def _doGetJustify(self):
        return ('left', 'right', 'center', 'fill')[self._obj.get_justify()]

    def _doSetMnemonicWidget(self, widget):
        self._obj.set_mnemonic_widget(widget._obj)
    def _doGetMnemonicWidget(self):
        obj = self._obj.get_mnemonic_widget()
        found = self
        parent = self.getParent()
        while parent:
            found = parent
            parent = parent.getParent()
        found = found.findDescendants(lambda x: getattr(x, '_obj', None) is obj)
        if found:
            return found[0]
        else:
            return None
        

    def _doSetUseMarkup(self, use):
        self._obj.set_use_markup(use)
    def _doGetUseMarkup(self):
        return self._obj.get_use_markup()

    def _doSetUseUnderline(self, use):
        self._obj.set_use_underline(use)
    def _doGetUseUnderline(self):
        return self._obj.get_use_underline()

    def _doSetSelectable(self, selectable):
        self._obj.set_selectable(selectable)
    def _doGetSelectable(self):
        return self._obj.get_selectable()

    def _doSetLineWrap(self, wrap):
        self._obj.set_line_wrap(wrap)
    def _doGetLineWrap(self):
        return self._obj.get_line_wrap()

