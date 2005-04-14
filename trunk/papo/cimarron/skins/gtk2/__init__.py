from papo.cimarron.skins.common import Widget, Container, Control
import pygtk
pygtk.require('2.0')
import gtk

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

class GtkMixin(GtkVisibilityMixin):
    """
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
            parent._children.append(self)
            parent._widget.add(self._widget)
            self.__parent = parent
    def __get_parent(self):
        try:
            return self.__parent
        except AttributeError:
            # only happens during init
            return None
    parent = property(__get_parent, __set_parent)

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

class Label(GtkMixin, Widget):
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

class Button(GtkMixin, Control):
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

class Entry(GtkMixin, Control):
    def __init__(self, **kw):
        self._widget= self.__entry= gtk.Entry ()
        super(Entry, self).__init__(**kw)
        self.update ()
        self.__entry.connect ('activate', self._activate)

    def __get_value (self):
        return self.__value
    def __set_value (self, value):
        self.__value = value
        self.__entry.set_text(value)
    value= property (__get_value, __set_value)

    def update (self):
        self.__entry.set_text (self.value)

    def _activate (self, *ignore):
        self.__value= self.__entry.get_text ()
        super (Entry, self)._activate ()

class VBox(GtkMixin, Container):
    def __init__ (self, **kw):
        self._widget= self.__vbox = gtk.VBox()
        super (VBox, self).__init__ (**kw)

class HBox(GtkMixin, Container):
    def __init__ (self, **kw):
        self._widget= self.__vbox = gtk.HBox()
        super (HBox, self).__init__ (**kw)

def _run():
    gtk.main()
