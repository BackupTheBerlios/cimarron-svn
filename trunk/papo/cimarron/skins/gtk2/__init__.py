from new import instancemethod
import pygtk
pygtk.require('2.0')
import gtk, gobject

from papo.cimarron.skins.common import Widget, Container, Control, nullAction, Unknown

class GtkVisibilityMixin(object):
    def __get_visible(self):
        w = self._widget.window
        return w is not None and w.is_visible()
    visible = property(__get_visible)

    def show(self):
        self._widget.show_all()

    def hide(self):
        if self.delegate('will_hide'):
            self._widget.hide_all()

class GtkParentizableMixin(object):
    """
        Takes care of the parenting issues under gtk2.
        Add this mixin class *before* any Widget-derived class.
    """
    def __set_parent(self, parent):
        if parent is not None and self.parent is parent:
            raise ValueError, 'Child already in parent'
        if self.parent is not None:
            if parent is None:
                raise NotImplementedError, 'Cannot deparent'
            else:
                raise NotImplementedError, 'Cannot reparent'
        if parent is not None:
            parent._widget.add(self._widget)
            parent._children.append(self)
            self.__parent = parent
    def __get_parent(self):
        try:
            return self.__parent
        except AttributeError:
            # only happens during init
            return None
    parent = property(__get_parent, __set_parent)

class GtkFocusableMixin(object):
    """
    """
    def __init__ (self, onFocusIn=None, onFocusOut=None, **kw):
        super (GtkFocusableMixin, self).__init__ (**kw)
        self.onFocusIn= onFocusIn
        self.onFocusOut= onFocusOut
        self._widget.connect ('focus-in-event', self._focusIn)
        self._widget.connect ('focus-out-event', self._focusOut)

    def _focusIn (self, *ignore):
        # print "I'm in!", self
        return not self.delegate ('will_focus_in')

    def _focusOut (self, *ignore):
        # print "I'm out!", self
        return not self.delegate ('will_focus_out')

    def focus (self):
        self._widget.grab_focus ()

class Window(GtkVisibilityMixin, Container):
    def __init__(self, title='', **kw):
        self._widget = self.__window = gtk.Window()
        super(Window, self).__init__(**kw)

        def delete_callback(*a):
            self.hide()
            return True

        self.__window.connect('delete-event', delete_callback)
        self.title = title

    def __set_title(self, title):
        self.__window.set_title(title)
    def __get_title(self):
        return self.__window.get_title()
    title = property(__get_title, __set_title)

class Label(GtkParentizableMixin, Widget):
    def __init__(self, text='', **kw):
        self._widget = self.__label = gtk.Label()
        super(Label, self).__init__(**kw)
        self.text = text

    def show(self):
        self.__label.show()

    def __set_text(self, text):
        self.__label.set_text(text)
    def __get_text(self):
        return self.__label.get_text()
    text = property(__get_text, __set_text)

class Button(GtkParentizableMixin, GtkFocusableMixin, Control):
    def __init__(self, label='', **kw):
        self._widget = self.__button = gtk.Button()
        super(Button, self).__init__(**kw)
        self.label = label
        self.__button.connect('clicked', self._activate)

    def __set_label(self, label):
        self.__button.set_label(label)
    def __get_label(self):
        return self.__button.get_label()
    label = property(__get_label, __set_label)

class Entry(GtkParentizableMixin, GtkFocusableMixin, Control):
    def __init__(self, **kw):
        self._widget= self.__entry= gtk.Entry ()
        super(Entry, self).__init__(**kw)
        self.update ()
        self.__entry.connect ('activate', self._activate)
        self.__entry.connect ('key-press-event', self._keypressed)
        self.delegates.append (self)

    def __get_value (self):
        return self.__value
    def __set_value (self, value):
        self.__value = value
        self.__entry.set_text(value)
    value= property (__get_value, __set_value)

    def update (self):
        self.__entry.set_text (self.value)
    def will_focus_out (self, *ignore):
        self.__value= self.__entry.get_text ()
        return Unknown

    def _activate (self, *ignore):
        self.__value= self.__entry.get_text ()
        super (Entry, self)._activate ()
    def _keypressed (self, widget, key_event, *ignore):
        # gotta find the symbolics of these
        if key_event.keyval==gtk.keysyms.Escape:
            # esc; `reset' the value
            self.update ()

class VBox(GtkParentizableMixin, Container):
    def __init__ (self, **kw):
        self._widget= self.__vbox = gtk.VBox()
        super (VBox, self).__init__ (**kw)

class HBox(GtkParentizableMixin, Container):
    def __init__ (self, **kw):
        self._widget= self.__vbox = gtk.HBox()
        super (HBox, self).__init__ (**kw)

class NotebookChildren (list):
    def __init__ (self, notebook):
        self.notebook= notebook
    def append (self, other):
        label= gtk.Label()
        label.set_text (other.label)
        self.notebook._widget.set_tab_label (other._widget, label)
        super (NotebookChildren, self).append (other)

class Notebook (GtkParentizableMixin, Container):
    def __init__ (self, **kw):
        self._widget= self.__notebook= gtk.Notebook ()
        super (Notebook, self).__init__ (**kw)
        self._children= NotebookChildren (self)

    def activate (self, other):
        if type (other)==int:
            # assume it's the page no
            pageNo= other
        else:
            # assume it's a child
            pageNo= self._children.index (other)
        if 0<=pageNo and pageNo<len (self._children):
            self._widget.set_current_page (pageNo)

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
