from papo.cimarron.skins.common import Widget, Container, Control

class Window(Container):
    def __init__(self, title='', **kw):
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

class Button(Control):
    def __init__(self, label='', **kw):
        super(Button, self).__init__(**kw)
        self.label = label

class Entry(Control):
    pass
