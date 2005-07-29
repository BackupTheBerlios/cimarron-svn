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

"""
L{Control}s are L{Widget}s the user can interact with.
"""

__revision__ = int('$Rev$'[5:-1])

import logging
logger = logging.getLogger('fvl.cimarron.skins.gtk2.control')
# logger.setLevel(logging.DEBUG)

import gtk
import gobject

from fvl.cimarron.skins.gtk2.mixin import GtkFocusableMixin
from fvl.cimarron.skins.common import Control, Unknown

class Button(GtkFocusableMixin, Control):
    """
    A Button is a Control that can be pressed, and when it does,
    it fires the action.
    """
    dirty = staticmethod(bool)

    def __init__(self, label='', **kwargs):
        """
        @param label: text that is shown in the middle of the button.
        """
        if '_concreteWidget' not in self.__dict__:
            self._activableWidget = self._focusWidget = self._outerWidget = self._concreteWidget = gtk.Button()
            self._concreteWidget.set_use_underline(True)
        super(Button, self).__init__(**kwargs)
        self.label = label
        self._concreteWidget.connect('clicked', self._activate)

    def _set_label(self, label):
        """
        Set the button's label.

        label must be a unicode object.
        """
        self._concreteWidget.set_label(label)
    def _get_label(self):
        """
        Get the button's label.
        """
        return self._concreteWidget.get_label()
    label = property(_get_label, _set_label, None,
                     """See the C{label} parameter for the constructor.""")

    def skelargs(self):
        """
        See L{XmlMixin.skelargs}
        """
        skelargs = super(Button, self).skelargs()
        skelargs['label'] = self.label
        return skelargs

class Checkbox(Button):
    """
    A Control that represents a boolean value.
    """
    def __init__(self, checked=False, **kwargs):
        if '_concreteWidget' not in self.__dict__:
            self._activableWidget = self._focusWidget = self._outerWidget = \
                                    self._concreteWidget = gtk.CheckButton()
        super(Checkbox, self).__init__(**kwargs)
        self.checked = checked
    _cellDataType = gobject.TYPE_BOOLEAN
    def _setupCell(cls, grid, dataColumn, viewColumn, index, readOnly=False):
        renderer = gtk.CellRendererToggle()
        if not (readOnly or dataColumn.readOnly):
            renderer.set_property('activatable', True)
            renderer.connect('toggled', grid._cell_toggled, index)
        viewColumn.pack_start(renderer, True)
        viewColumn.add_attribute(renderer, 'active', index)
    _setupCell = classmethod(_setupCell)
    def _get_checked(self):
        """
        Get whether the checkbox is checked.
        """
        return self._concreteWidget.get_active()
    def _set_checked(self, checked):
        """
        Set the checkedness of the checkbox.
        """
        self._concreteWidget.set_active(checked)
    checked = property(_get_checked, _set_checked)

class Entry(GtkFocusableMixin, Control):
    """
    The simplest text input control.
    """
    def __init__(self, emptyValue=None, **kwargs):
        if '_concreteWidget' not in self.__dict__:
            self._activableWidget = self._focusWidget = self._outerWidget = self._concreteWidget = gtk.Entry()
            self._concreteWidget.connect ('activate', self._activate)
            self._concreteWidget.connect ('key-release-event', self._keyreleased)
        self.emptyValue = emptyValue
        super(Entry, self).__init__(**kwargs)
        self.refresh ()

    _cellDataType = gobject.TYPE_STRING
    def _setupCell(cls, grid, dataColumn, viewColumn, index, readOnly=False):
        renderer = gtk.CellRendererText()
        if not (readOnly or dataColumn.readOnly):
            renderer.set_property('editable', True)
            renderer.connect('edited', grid._cell_edited, index)
        viewColumn.pack_start(renderer, True)
        viewColumn.add_attribute(renderer, 'text', index)
    _setupCell = classmethod(_setupCell)

    def _get_value (self):
        """
        Get the C{entry}'s value.
        """
        #value = self._concreteWidget.get_text() or self.emptyValue
        return self._concreteWidget.get_text() or self.emptyValue
    def _set_value (self, value):
        """
        Set the C{Entry}'s value. C{value} must be a unicode object.
        """
        if value is None:
            value = ''
        self._concreteWidget.set_text(unicode(value))
        # traceback.print_stack()
        # logger.error('%r -> %r' % (value, self.value))
    value = property (_get_value, _set_value)

    def _focusOut(self, *ignore):
        """
        The widget is about to lose focus.

        If the delegate agrees, go ahead and save the changes.
        """
        if self.delegate('will_focus_out'):
            self.commitValue()
            self.dirty()
        return False

    def _keyreleased (self, widget, key_event):
        """
        Called whenever a key is hit.
        If that key is <Esc>, undo the edition.
        Do not call directly.
        """
        if key_event.keyval == gtk.keysyms.Escape:
            # esc; `reset' the value
            self.refresh()
            widget.select_region(0, -1)
        self.dirty()

    def dirty(self):
        """
        has the user modified the C{Entry}'s value?
        """
        dirty = self._targetValue() != (self.value or self.emptyValue)
        if dirty:
            self._concreteWidget.modify_bg(gtk.STATE_NORMAL, gtk.gdk.color_parse('red'))
        else:
            self._concreteWidget.modify_bg(gtk.STATE_NORMAL, None)
        return dirty


class MultiLine(Entry):
    """
    A multiline Text input (we could call it a Text Area, but we don't:D).
    """
    def __init__(self, emptyValue=None, aBuffer=None,**kwargs):
        if not aBuffer:
            self.buffer = gtk.TextBuffer()
        else:
            self.buffer = aBuffer
        self._focusWidget = self._outerWidget = self._concreteWidget = gtk.TextView(self.buffer)
        """
        WRAP_CHAR gives word wraping character boundaries,
        this can be changed to words or not to wrap (WRAP_WORD, WRAP_NONE)
        a parameter should be added for this, meanwhile it will stay
        like this beacause i think is the most frequent use case
        """
        self._concreteWidget.set_wrap_mode(gtk.WRAP_CHAR)
        """
        Same here that in wraping but options are (JUSTIFY_RIGHT, JUSTIFY_CENTER)
        """
        self._concreteWidget.set_justification(gtk.JUSTIFY_LEFT)
        self._tc = self._concreteWidget #_tc for text container
        self._concreteWidget = gtk.ScrolledWindow()
        self._concreteWidget.add(self._tc)
        self.emptyValue = emptyValue
        super(MultiLine, self).__init__(**kwargs)
        self._focusWidget = self._outerWidget = self._concreteWidget
        self.refresh ()

    def _get_value (self):
        """
        Get the C{MlEntry}'s buffer value.
        """
        return self.buffer.get_text(self.buffer.get_start_iter(),
                                     self.buffer.get_end_iter(),
                                     include_hidden_chars=False) or self.emptyValue
    def _set_value (self, value):
        """
        Set the C{MlEntry}'s buffer value. C{value} must be a unicode object.
        """
        if value is None:
            value = ''
        self.buffer.set_text(unicode(value))
        self._tc.set_buffer(self.buffer)
        #traceback.print_stack()
        logger.debug(`value`)
    value = property (_get_value, _set_value)
