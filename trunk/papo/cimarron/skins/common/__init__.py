from papo.cimarron.tools import Observable

class Widget(object):
    def __init__(self, parent=None, **kw):
        super (Widget, self).__init__ (**kw)
        self.parent = parent
        if parent is not None:
            parent.children.append(self)

class Container(Widget):
    def __init__(self, **kw):
        super(Container, self).__init__(**kw)
        self.children = []

    def show(self):
        for i in self.children:
            i.show()

class Control(Widget, Observable):
    def __init__(self, value='', **kw):
        super(Control, self).__init__(**kw)
        self.value = value

