from papo.cimarron.tools import Observable

class Widget(object):
    def __init__(self, parent=None, **kw):
        super (Widget, self).__init__ (**kw)
        self.parent = parent

    def __set_parent(self, parent):
        if self.parent is not None:
            raise NotImplementedError, 'Cannot reparent'
        self.__parent = parent
        if parent is not None:
            parent.children.append(self)
    def __get_parent(self):
        return getattr(self, '_Widget__parent', None)
    parent = property(__get_parent, __set_parent)

    def __get_skin (self):
        try:
            return self.__skin
        except AttributeError:
            self.__skin = self.parent.skin
            return self.__skin
    skin = property(__get_skin)

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
