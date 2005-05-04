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
        self._widget = self.__window = gtk.Window()
        super(Window, self).__init__(**kw)

        def delete_callback(*a):
            self.hide()
            return True

        self.__window.connect('delete-event', delete_callback)
        self.title = title

    def _set_title(self, title):
        self.__window.set_title(title)
    def _get_title(self):
        return self.__window.get_title()
    title = property(_get_title, _set_title)


class Label(Widget):
    def __init__(self, text='', **kw):
        self._widget = self.__label = gtk.Label()
        super(Label, self).__init__(**kw)
        self.text = text

    def show(self):
        self.__label.show()

    def _set_text(self, text):
        self.__label.set_text(text)
    def _get_text(self):
        return self.__label.get_text()
    text = property(_get_text, _set_text)

class Button(GtkFocusableMixin, Control):
    def __init__(self, label='', **kw):
        self._widget = self.__button = gtk.Button()
        super(Button, self).__init__(**kw)
        self.label = label
        self.__button.connect('clicked', self._activate)

    def _set_label(self, label):
        self.__button.set_label(label)
    def _get_label(self):
        return self.__button.get_label()
    label = property(_get_label, _set_label)

    def skelargs(self):
        skelargs = super(Button, self).skelargs()
        skelargs.append('label=%s' % repr(self.label))
        return skelargs

class Entry(GtkFocusableMixin, Control):
    def __init__(self, **kw):
        self._widget= self.__entry= gtk.Entry ()
        super(Entry, self).__init__(**kw)
        self.update ()
        self.__entry.connect ('activate', self._activate)
        self.__entry.connect ('key-press-event', self._keypressed)
        self.delegates.append (self)

    def _get_value (self):
        return self.__value
    def _set_value (self, value):
        self.__value = value
        self.__entry.set_text(value)
    value= property (_get_value, _set_value)

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

class VBox(Container):
    def __init__ (self, **kw):
        self._widget= self.__vbox = gtk.VBox()
        super (VBox, self).__init__ (**kw)

class HBox(Container):
    def __init__ (self, **kw):
        self._widget= self.__vbox = gtk.HBox()
        super (HBox, self).__init__ (**kw)

class Notebook (Container):
    def __init__ (self, **kw):
        self._widget= self.__notebook= gtk.Notebook ()
        super (Notebook, self).__init__ (**kw)

    def activate (self, other):
        if type (other)==int:
            # assume it's the page no
            pageNo= other
        else:
            # assume it's a child
            pageNo= self._children.index (other)
        if 0<=pageNo and pageNo<len (self._children):
            self._widget.set_current_page (pageNo)

    def concreteParenter (self, child):
        super (Notebook, self).concreteParenter (child)
        if getattr (child, '_widget', None):
            label= gtk.Label()
            label.set_text (child.label)
            self._widget.set_tab_label (child._widget, label)
        

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
