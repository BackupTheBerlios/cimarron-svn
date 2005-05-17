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

from new import instancemethod
import pygtk
pygtk.require('2.0')
import gtk, gobject
from itertools import izip, repeat

# clients of cimarron won't want to worry where their stuff is coming
# from
from papo.cimarron.skins.common import *
from papo.cimarron.controllers import *

class GtkVisibilityMixin(object):
    """
    Mixin that lets show and hide the object.
    Used only by Window.
    """
    def _get_visible(self):
        w = self._widget.window
        return w is not None and w.is_visible()
    visible = property(_get_visible, None, None, """""")

    def show(self):
        """
        Show the object.
        """
        self._widget.show_all()

    def hide(self):
        """
        Hide the object, after delegates agrees.
        """
        if self.delegate ('will_hide'):
            self._widget.hide_all()

class GtkFocusableMixin(object):
    """
    Mixin that delegates focus in/out and makes the object
    to be focusable programatically.
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
        """
        Set the focus on this object.
        """
        self._widget.grab_focus ()

class Window(GtkVisibilityMixin, Container):
    """
    A Window. Duh.
    """
    def __init__(self, title='', **kw):
        """
        @param title: the title for the window.
        """
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
    title = property(_get_title, _set_title, None, """The title for the window.""")


class Label(Widget):
    """
    A Label is a piece of uneditable static text.
    """
    def __init__(self, text='', **kw):
        """
        @param text: The static test.
        """
        self._widget = gtk.Label()
        super(Label, self).__init__(**kw)
        self.text = text

    def show(self):
        self._widget.show()

    def _set_text(self, text):
        self._widget.set_text(text)
    def _get_text(self):
        return self._widget.get_text()
    text = property(_get_text, _set_text, None, """The static test.""")

class Button(GtkFocusableMixin, Control):
    """
    A Button is a Control that can be pressed, and when it does,
    it fires the action.
    """
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
    value= property (_get_value, _set_value, None, """""")

    def update (self):
        """
        Show the value on the control.
        """
        value= self.value
        if value is None:
            value= ''
        self._widget.set_text (value)
    def will_focus_out (self, *ignore):
        """
        Called when the focus goes out the Entry.
        Copies the shown value to the value property.
        Do not call directly.
        """
        # is not the same as _activate ()
        self.value= self._widget.get_text ()
        return Unknown

    def _activate (self, *ignore):
        """
        Called when <Enter> is hit.
        Copies the shown value to the value property.
        Do not call directly.
        """
        self.value= self._widget.get_text ()
        super (Entry, self)._activate ()
    def _keypressed (self, widget, key_event, *ignore):
        """
        Called whenever a key is hit.
        If that key is <Esc>, undo the edition.
        Do not call directly.
        """
        if key_event.keyval==gtk.keysyms.Escape:
            # esc; `reset' the value
            self.update ()

class VBox(Container):
    """
    A vertical container. The children of this object
    will be placed one on top of the other.
    """
    def __init__ (self, **kw):
        self._widget = gtk.VBox()
        # self._widget.set_border_width (5)
        self._widget.set_spacing (5)
        super (VBox, self).__init__ (**kw)

class HBox(Container):
    """
    A horizontal container. The children of this object
    will be placed from left to right.
    """
    def __init__ (self, **kw):
        self._widget = gtk.HBox()
        # self._widget.set_border_width (5)
        self._widget.set_spacing (5)
        super (HBox, self).__init__ (**kw)

class Notebook (Container):
    """
    A container where all the children are put in `tabs´ and
    only one of them is shown at any given time.
    """
    def __init__ (self, **kw):
        self._widget = gtk.Notebook ()
        super (Notebook, self).__init__ (**kw)
        self._widget.connect ('change-current-page', self.__change_page)

    def activate (self, other):
        """
        Show a particular tab.

        @param other: either the child to show or
            the index of the child.
        """
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
        """
        Makes that page switching
        """
        ans= False
        if self.delegate ('will_change_page'):
            ans= True
        return ans


class Grid (Controller):
    """
    Grids are used for showing and may be editing a list of objects,
    or for selecting one among those.
    """
    def __init__ (self, data=[], columns=[], **kw):
        """
        @param data: the list of objects to be shown.

        @param columns: a list of B{Column}s that describe
            what to show in the grid, how obtain it from the
            objects, and eventually how to save data back to.
        """
        self._tv= gtk.TreeView ()

        self._columns= columns
        # build the tv columns and the data types tuple
        (self._tvcolumns, self._dataspec)= izip(*izip(
            [ gtk.TreeViewColumn (c.name) for c in columns ],
            repeat(str)
            ))
        self.data= data

        # put the TreeView in a scrolled window
        self._widget= gtk.ScrolledWindow ()
        self._widget.set_policy(gtk.POLICY_NEVER, gtk.POLICY_ALWAYS)
        self._widget.add (self._tv)

        # add the columns and attrs
        for i in xrange (len (columns)):
            c= self._tvcolumns[i]
            crt= gtk.CellRendererText ()
            if columns[i].write is not None:
                # editable
                crt.set_property ('editable', True)
                crt.connect ('edited', self._cell_edited, (i, columns[i].write))
            c.pack_start (crt, True)
            c.add_attribute (crt, 'text', i)
            self._tv.append_column (c)

        self._tv.connect ('key-press-event', self._keypressed)

        super (Grid, self).__init__ (**kw)

    def _cell_edited (self, cell, path, text, data, *ignore):
        (colNo, write)= data
        # modify the ListStore model...
        self._tvdata[path][colNo]= text
        # ... and our model
        write (self.data[int (path)], text)
        # coming soon: our models will (should) suport the generic TreeModel protocol
        # also: if write() returns false, the entry flashes and
        # a) rollbacks the value or
        # b) leaves it with wrong value, so the user can edit it (preferred)
        return False
    def _keypressed (self, widget, key_event, *ignore):
        if key_event.keyval==gtk.keysyms.Return:
            self.onAction ()
            return True
        return False

    def _set_data (self, data):
        # the model data
        self._data= data

        if len (self._columns)>0:
            self._tvdata= gtk.ListStore (*self._dataspec)
        if data is not None:
            for i in data:
                # build a ListStore w/ al the values
                # NOTE: this forces the data to be read.
                self._tvdata.append ([j.read (i) for j in self._columns])
        self._tv.set_model (self._tvdata)
    def _get_data (self):
        return self._data
    data= property (_get_data, _set_data, None,
                    """The list of objects to be shown.""")

    def _set_index (self, index):
        if index is not None:
            self._tv.set_cursor (index)
    def _get_index (self):
        try:
            # goddam get_cursor() returns path as tuple,
            # not like the path passed to cell_edited()
            return int (self._tv.get_cursor ()[0][0])
        except:
            # print self._tv.get_cursor ()
            return None
    index= property (_get_index, _set_index, None,
                     """The index of the object currently selected.
                     If no object is selected, it is None.""")

    def _set_value (self, value):
        try:
            index= self.data.index (value)
        except (ValueError, AttributeError):
            index= None
        self.index= index
    def _get_value (self):
        ans= None
        if self.index is not None:
            ans= self.data[self.index]
        return ans
    value= property (_get_value, _set_value, None,
                     """The selected object. If no object is selected, it is None.""")

    def refresh (self):
        pass


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
    """
    Does the skin-specific magic that `glues' a child with its parent.
    Do not call directly.
    """
    if '_widget' in child.__dict__:
        if '_widget' in parent.__dict__:
            parent._widget.add(child._widget)
        else:
            parent.parent.concreteParenter (child)
