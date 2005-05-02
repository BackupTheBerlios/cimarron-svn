from new import instancemethod
import operator

def nullAction(*a, **k): pass

ForcedNo, No, Unknown, Yes, ForcedYes = -5, -1, 0, 1, 5

class Widget(object):

    def __init__(self, parent=None, **kw):
        super (Widget, self).__init__ (**kw)
        self.delegates = []
        self.parent = parent
        for k, v in kw.items ():
            setattr (self, k, v)

    def __set_parent(self, parent):
        if parent is not None and self.parent is parent:
            raise ValueError, 'Child already in parent'
        if self.parent is not None:
            if parent is None:
                raise NotImplementedError, 'Cannot deparent'
            else:
                raise NotImplementedError, 'Cannot reparent'
        if parent is not None:
	    self.skin.concreteParenter(parent, self)
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
	    from papo.cimarron import skin
            self.__skin = skin
            return skin
    skin = property(__get_skin)

    def delegate(self, message, *args):
        if self.delegates:
            truthTable = ((Unknown, Yes, No), (Yes, Yes, Yes), (No, Yes, No))
            av= Unknown
            for i in self.delegates:
                try:
                    rv= getattr(i, message)(self, *args)
                    av= truthTable[av][rv]
                except AttributeError:
                    rv = Unknown
                except IndexError:
                    av= rv
                    break
            return av>=0
        return True

class Container(Widget):
    def __init__(self, **kw):
        super(Container, self).__init__(**kw)
        self._children = []

    def show(self):
        for i in self.children:
            i.show()

    def hide(self):
        for i in self.children:
            if i.delegate('will_hide'):
                i.hide()

    def __get_children(self):
        return iter(self._children)
    children = property(__get_children)


class Control(Widget):
    def __init__(self, onAction=None, value='', **kw):
        super(Control, self).__init__(**kw)
        self.value = value
        self.onAction= onAction

    def __get_on_action (self):
        return self.__on_action
    def __set_on_action (self, onAction):
        if onAction is None:
            onAction = nullAction
        self.__on_action= instancemethod (onAction, self, Control)
    onAction= property (__get_on_action, __set_on_action)

    def _activate(self, *ignore):
        if self.onAction is not None:
            self.onAction()
