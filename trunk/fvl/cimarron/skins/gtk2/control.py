# -*- coding: utf-8 -*-
#
# Copyright 2003, 2004, 2005 Fundación Via Libre
#
# This file is part of PAPO.
#
# PAPO is free software; you can redistribute it and/or modify it under the
# terms of the GNU General Public License as published by the Free Software
# Foundation; either version 2 of the License, or (at your option) any later
# version.
#
# PAPO is distributed in the hope that it will be useful, but WITHOUT ANY
# WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
# FOR A PARTICULAR PURPOSE.  See the GNU General Public License for more
# details.
#
# You should have received a copy of the GNU General Public License along with
# PAPO; if not, write to the Free Software Foundation, Inc., 59 Temple Place,
# Suite 330, Boston, MA 02111-1307 USA

import logging
logger = logging.getLogger('fvl.cimarron.skins.gtk2.control')

import gtk

from mixin import GtkFocusableMixin
from fvl.cimarron.skins.common import Control, Unknown

class Button(GtkFocusableMixin, Control):
    """
    A Button is a Control that can be pressed, and when it does,
    it fires the action.
    """
    is_dirty = False

    def __init__(self, label='', **kw):
        """
        @param label: text that is shown in the middle of the button.
        """
        if not '_widget' in self.__dict__:
            self._widget = gtk.Button()
        super(Button, self).__init__(**kw)
        self.label = label
        self._widget.connect('clicked', self._activate)

    def _set_label(self, label):
        self._widget.set_label(label)
    def _get_label(self):
        return self._widget.get_label()
    label = property(_get_label, _set_label, None,
                     """See the C{label} parameter for the constructor.""")

    def skelargs(self):
        skelargs = super(Button, self).skelargs()
        skelargs['label'] = self.label
        return skelargs

class Checkbox(Button):
    """
    A Control that represents a boolean value.
    """
    def __init__(self, checked=False, **kw):
        self._widget = gtk.CheckButton()
        super(Checkbox, self).__init__(**kw)
        self.checked = checked
    def _get_checked(self):
        return self._widget.get_active()
    def _set_checked(self, checked):
        self._widget.set_active(checked)
    checked = property(_get_checked, _set_checked)

class Entry(GtkFocusableMixin, Control):
    """
    The simplest text input control.
    """
    def __init__(self, value='', **kw):
        self._widget = gtk.Entry()
        super(Entry, self).__init__(value=value, **kw)
        self.refresh ()
        self._widget.connect ('activate', self._activate)
        self._widget.connect ('key-release-event', self._keyreleased)
        self.delegates.append (self)

    def _get_value (self):
        value = self._widget.get_text()
        if '_given_value' in self.__dict__:
            logger.error('using workaround :(')
            if self._used_value == value:
                return self._given_value
        return value
    def _set_value (self, value):
        if not isinstance(value, basestring):
            logger.error('provided non-string value to gtk2 entry')
            logger.error('using workaround -- FOR NOW!')
            self._given_value = value
            self._used_value = value = unicode(value)
        elif '_given_value' in self.__dict__:
            logger.error('string provided, cleaning up workaround')
            del self._given_value
            del self._used_value
        self._widget.set_text(value)
    value= property (_get_value, _set_value, None, """""")

    def will_focus_out (self, *ignore):
        """
        Called when the focus goes out the Entry.
        Copies the shown value to the value property.
        Do not call directly.
        """
        # is not the same as _activate ()
        self.value= self._widget.get_text ()
        return Unknown

    def _activate(self, widget=None):
        """
        Called when <Enter> is hit. 
        Copies the shown value to the value property.
        Do not call directly.
        """
        if widget is None:
            widget = self._widget
        self.value = widget.get_text()
        super(Entry, self)._activate()

    def _keyreleased (self, widget, key_event):
        """
        Called whenever a key is hit.
        If that key is <Esc>, undo the edition.
        Do not call directly.
        """
        if key_event.keyval == gtk.keysyms.Escape:
            # esc; `reset' the value
            self.refresh()
            widget.select_region(0,-1)
        self.is_dirty

    def _is_dirty(self):
        is_dirty = self.targetValue != self._widget.get_text()
        if is_dirty:
            self._widget.modify_bg(gtk.STATE_NORMAL, gtk.gdk.color_parse('red'))
        else:
            self._widget.modify_bg(gtk.STATE_NORMAL, None)
        return is_dirty
    is_dirty = property(_is_dirty)
