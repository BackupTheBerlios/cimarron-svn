import new
from papo.cimarron.skins.common import Widget, Container

class Window(Container):
    def __init__(self, title=None, **kw):
        super(Window, self).__init__(**kw)
        self.title = title

    def show(self):
        s = '*'*80 + ' ' + self.title
        print s[len(s)-80:]
        super(Window, self).show()
        print '*' * 80
        
class Label(Widget):
    def __init__(self, text='', **kw):
        super(Label, self).__init__(**kw)
        self.text = text
        
    def show(self):
        print self.text

class Observable(object):
    def __init__ (self, **kw):
        super (Observable, self).__init__ (**kw)
        self.observers= []

    def announce (self, message):
        for o in self.observers:
            o.notify (message)

class Control(Widget, Observable):
    def __init__(self, action=None, value=None, **kw):
        super(Control, self).__init__(**kw)
        if action is None:
            action = lambda s: None
        self.action = action
        self.value = value
    def __set_action(self, action):
        self.__action = new.instancemethod(action, self, type(self))
    def __get_action(self):
        return self.__action
    action = property(__get_action, __set_action)

class Button(Control):
    def __init__(self, label='', **kw):
        super(Button, self).__init__(**kw)
        self.label = label

class Entry(Control):
    pass
