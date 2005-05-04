from new import instancemethod
import operator

__all__ = ('Widget', 'Container', 'Control',
           'ForcedNo', 'No', 'Unknown', 'Yes', 'ForcedYes',)

from papo.cimarron.tools import is_simple

def nullAction(*a, **k): pass

ForcedNo, No, Unknown, Yes, ForcedYes = -5, -1, 0, 1, 5

from papo import cimarron

class Widget(object):

    def __init__(self, parent=None, **kw):
        super (Widget, self).__init__ (**kw)
        self.delegates = []
        self.parent = parent
        for k, v in kw.items ():
            setattr (self, k, v)

    def skeleton(self, parentstr='', position=None):
        skelargs = self.skelargs()
        if not parentstr:
            skel = 'skel = '
        else:
            skelargs.append('parent=' + parentstr)
            skel = ''
        return [ skel + 'skin.%s(%s)' % (self.__class__.__name__,
                                         ', '.join(skelargs)) ]

    def skelargs(self):
        return []

    def _set_parent(self, parent):
        if parent is not None and self.parent is parent:
            raise ValueError, 'Child already in parent'
        if self.parent is not None:
            if parent is None:
                raise NotImplementedError, 'Cannot deparent'
            else:
                raise NotImplementedError, 'Cannot reparent'
        if parent is not None:
            parent.concreteParenter(self)
            parent._children.append(self)
            self.__parent = parent
    def _get_parent(self):
        try:
            return self.__parent
        except AttributeError:
            # only happens during init
            return None
    parent = property(_get_parent, _set_parent)

    def _get_skin (self):
        try:
            return self.__skin
        except AttributeError:
            from papo.cimarron import skin
            self.__skin = skin
            return skin
    skin = property(_get_skin)

    def delegate(self, message, *args):
        if self.delegates:
            truthTable = ((Unknown, Yes, No), (Yes, Yes, Yes), (No, Yes, No))
            av= Unknown
            for i in self.delegates:
                try:
                    rv= getattr(i, message, lambda *a: Unknown)(self, *args)
                    av= truthTable[av][rv]
                except IndexError:
                    av= rv
                    break
            return av>=0
        return True

    def concreteParenter (self, child):
        cimarron.skin.concreteParenter (self, child)

class Container(Widget):
    def __init__(self, **kw):
        super(Container, self).__init__(**kw)
        self._children = []

    def show(self):
        for i in self.children:
            i.show()

    def hide(self):
        for i in self.children:
            i.hide()

    def _get_children(self):
        return tuple(self._children)
    children = property(_get_children)

    def skeleton(self, parentstr='', position=None):
        skels = super(Container, self).skeleton(parentstr)
        if position is None:
            parentstr = 'skel'
        else:
            parentstr = parentstr + '.children[%d]' % position
        for index, child in enumerate(self.children):
            skels.extend(child.skeleton(parentstr, index))
                
        return skels

class Control(Widget):
    def __init__(self, onAction=None, value='', **kw):
        super(Control, self).__init__(**kw)
        self.value = value
        self.onAction= onAction

    def _get_on_action (self):
        return self.__on_action
    def _set_on_action (self, onAction):
        if onAction is None:
            onAction = nullAction
        self.__on_action= instancemethod (onAction, self, Control)
    onAction= property (_get_on_action, _set_on_action)

    def _activate(self, *ignore):
        if self.onAction is not None:
            self.onAction()

    def skelargs(self):
        skelargs = super(Control, self).skelargs()
        value = self.value
        if is_simple(value):
            skelargs.append('value=%s' % repr(value))
        return skelargs
