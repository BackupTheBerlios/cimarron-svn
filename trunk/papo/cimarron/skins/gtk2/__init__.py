# -*- coding: utf-8 -*-
#
# Copyright 2003 Fundación Via Libre
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

from new import instancemethod
import pygtk
pygtk.require('2.0')
import gtk, gobject

# clients of cimarron won't want to worry where their stuff is coming
# from
from papo.cimarron.skins.common import *
from papo.cimarron.controllers import *

class GtkVisibilityMixin(object):
    def _get_visible(self):
        w = self._widget.window
        return w is not None and w.is_visible()
    visible = property(_get_visible)

    def show(self):
        self._widget.show_all()

    def hide(self):
        if self.delegate ('will_hide'):
            self._widget.hide_all()

class GtkFocusableMixin(object):
    """
    """
    def __init__ (self, **kw):
        super (GtkFocusableMixin, self).__init__ (**kw)
        self._widget.connect ('focus-in-event', self._focusIn)
        self._widget.connect ('focus-out-event', self._focusOut)

    def _focusIn (self, *ignore):
        return not self.delegate ('will_focus_in')

    def _focusOut (self, *ignore):
        return not self.delegate ('will_focus_out')

    def focus (self):
        self._widget.grab_focus ()

class Window(GtkVisibilityMixin, Container):
    def __init__(self, title='', **kw):
        self._widget = gtk.Window()
        super(Window, self).__init__(**kw)

        def delete_callback(*a):
            self.hide()
            return True

        self._widget.connect('delete-event', delete_callback)
        self.title = title

    def _set_title(self, title):
        self._widget.set_title(title)
    def _get_title(self):
        return self._widget.get_title()
    title = property(_get_title, _set_title)


class Label(Widget):
    def __init__(self, text='', **kw):
        self._widget = gtk.Label()
        super(Label, self).__init__(**kw)
        self.text = text

    def show(self):
        self._widget.show()

    def _set_text(self, text):
        self._widget.set_text(text)
    def _get_text(self):
        return self._widget.get_text()
    text = property(_get_text, _set_text)

class Button(GtkFocusableMixin, Control):
    def __init__(self, label='', **kw):
        if not '_widget' in self.__dict__:
            self._widget = gtk.Button()
        super(Button, self).__init__(**kw)
        self.label = label
        self._widget.connect('clicked', self._activate)

    def _set_label(self, label):
        self._widget.set_label(label)
    def _get_label(self):
        return self._widget.get_label()
    label = property(_get_label, _set_label)

    def skelargs(self):
        skelargs = super(Button, self).skelargs()
        skelargs['label'] = self.label
        return skelargs

class Checkbox(Button):
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
    def __init__(self, **kw):
        self._widget = gtk.Entry ()
        super(Entry, self).__init__(**kw)
        self.update ()
        self._widget.connect ('activate', self._activate)
        self._widget.connect ('key-press-event', self._keypressed)
        self.delegates.append (self)

    def _get_value (self):
        return self.__value
    def _set_value (self, value):
        # set the value only if:
        # we haven't set any value yet OR
        # NOT (our value is None AND the value to set is an empty string)
        # if not hasattr (self, '__value') or not (self.__value is None and value==''):
        self.__value = value
        self.update ()
    value= property (_get_value, _set_value)

    def update (self):
        value= self.value
        if value is None:
            value= ''
        self.__entry.set_text (value)
    def will_focus_out (self, *ignore):
        # is not the same as _activate ()
        self.value= self.__entry.get_text ()
        return Unknown

    def _activate (self, *ignore):
        self.value= self.__entry.get_text ()
        super (Entry, self)._activate ()
    def _keypressed (self, widget, key_event, *ignore):
        # gotta find the symbolics of these
        if key_event.keyval==gtk.keysyms.Escape:
            # esc; `reset' the value
            self.update ()

class VBox(Container):
    def __init__ (self, **kw):
        self._widget = gtk.VBox()
        # self._widget.set_border_width (5)
        self._widget.set_spacing (5)
        super (VBox, self).__init__ (**kw)

class HBox(Container):
    def __init__ (self, **kw):
        self._widget = gtk.HBox()
        # self._widget.set_border_width (5)
        self._widget.set_spacing (5)
        super (HBox, self).__init__ (**kw)

class Notebook (Container):
    def __init__ (self, **kw):
        self._widget = gtk.Notebook ()
        super (Notebook, self).__init__ (**kw)
        self._widget.connect ('change-current-page', self.__change_page)

    def activate (self, other):
        if type (other)==int:
            # assume it's the page no
            pageNo= other
        else:
            # assume it's a child
            pageNo= self._children.index (other)
        if 0<=pageNo and pageNo<len (self._children) and self.delegate ('will_change_page'):
            self._widget.set_current_page (pageNo)

    def concreteParenter (self, child):
        super (Notebook, self).concreteParenter (child)
        if getattr (child, '_widget', None):
            label= gtk.Label()
            label.set_text (child.label)
            self._widget.set_tab_label (child._widget, label)

    def __change_page (self, *ignore):
        ans= False
        if self.delegate ('will_change_page'):
            ans= True
        return ans
        

def _run():
    gtk.main()

def _quit():
    if gtk.main_level():
        gtk.main_quit()

def _schedule(timeout, callback, repeat=False):
    def cb():
        gobject.timeout_add(timeout, callback)
        if repeat:
            cb()
    cb()

def concreteParenter(parent, child):
    if '_widget' in child.__dict__:
        if '_widget' in parent.__dict__:
            parent._widget.add(child._widget)
        else:
            parent.parent.concreteParenter (child)
