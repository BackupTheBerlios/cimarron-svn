from papo.cimarron.skins.common import Widget, Container, Control
import pygtk
pygtk.require('2.0')
import gtk

class _Container(list):
    def __init__(self, parent):
        super(_Container, self).__init__()
        self.__parent = parent
    def append(self, other):
        super(_Container, self).append(other)
        self.__parent.add(other._widget)

class Window(Container):
    def __init__(self, title='', **kw):
        self._widget = self.__window = gtk.Window()
        super(Window, self).__init__(**kw)
        self.__window.connect('destroy', gtk.main_quit)
        self.title = title
        self.children = _Container(self.__window)

    def __set_title(self, title):
        self.__window.set_title(title)
    def __get_title(self):
        return self.__window.get_title()
    title = property(__get_title, __set_title)

    def show(self):
        self.__window.show_all()
        
class Label(Widget):
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

class Button(Control):
    def __init__(self, label='', **kw):
        self._widget = self.__button = gtk.Button()
        super(Button, self).__init__(**kw)
        self.label = label

    def __set_label(self, label):
        self.__button.set_label(label)
    def __get_label(self):
        return self.__button.get_label()
    label = property(__get_label, __set_label)

class Entry(Control):
    def __init__(self, **kw):
        self._widget= self.__entry= gtk.Entry ()
        super(Entry, self).__init__(**kw)
        self.update ()
        self.__entry.connect ('activate', self.__activate)

    def update (self):
        self.__entry.set_text (self.value)

    def __activate (self, *ignore):
        self.value= self.__entry.get_text ()


def run():
    gtk.main()
