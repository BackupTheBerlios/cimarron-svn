class Widget(object):
    def __init__(self, parent=None, **kw):
        super (Widget, self).__init__ (**kw)
        self.parent = parent
        self.defaultWidget= self

    def __set_parent(self, parent):
        if parent is not None:
            parent._children.append(self)
            self.__parent = parent
    def __get_parent(self):
        try:
            return self.__parent
        except AttributeError:
            # only happens during init
            return None
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
        self._children = []

    def show(self):
        for i in self.children:
            i.show()

    def __get_children(self):
        return iter(self._children)
    children = property(__get_children)

class Control(Widget):
    def __init__(self, onAction=None, value='', **kw):
        super(Control, self).__init__(**kw)
        self.value = value
        self.onAction= onAction

    def _activate(self, *ignore):
        if self.onAction is not None:
            self.onAction(self)
