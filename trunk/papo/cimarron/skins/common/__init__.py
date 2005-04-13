from new import instancemethod
import operator

def nullAction(*a, **k): pass

ForcedNo, No, Unknown, Yes, ForcedYes = -5, -1, 0, 1, 5

class Widget(object):

    def __init__(self, parent=None, **kw):
        super (Widget, self).__init__ (**kw)
        self.parent = parent
        self.delegates = []
        if kw:
            raise RuntimeError, 'unhandled keyword arguments %s' % repr(kw)

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

    def delegate(self, message):
        if self.delegates:
#             truthTable= { (0,0): Unknown, (0,1): Yes, (0,-1): No,
#                           (1,0): Yes, (1,1): Yes, (1,-1): Yes,
#                           (-1,0): No, (-1, 1): Yes, (-1,-1): No }
#            truthTable = [[Unknown, Yes, No], [Yes, Yes, Yes], [No, Yes, No]]
            truthTable = ((Unknown, Yes, No), (Yes, Yes, Yes), (No, Yes, No))
            av= Unknown
            for i in self.delegates:
                try:
                    rv= getattr(i, message)(self)
                    #av= truthTable[av,rv]
                    av= truthTable[av][rv]
                except AttributeError:
                    rv = Unknown
                except IndexError:
                    av= rv
                    break
            return av>=0
        return True



#     def delegate(self, message, comp=None, unknown=None, null=None, args=None):
#         """
#         The default delegation is with 'or', i.e. any 'Accept' is
#         enough, 'Unknown' is True, and null the same as 'Unknown'.
#
#         Parameters are:
#
#            comp     composition operator
#            unknown  value of 'Unknown'
#            null     value of empty delegation list
#            args     extra args to be passed on delegation
#
#         """
#         if comp is None:
#             comp = operator.or_
#         if null is None:
#             null = unknown
#            
#         if self.delegates:
#             res = unknown
#             for i in self.delegates:
#                 if hasattr(i, message):
#                     rv = getattr(i, message)(self, args)
#                     b = rv > 0 or (rv >= 0 and unknown)
#                 else:
#                     b = rv = unknown
#                 if rv and abs(rv)==5:
#                     res = b
#                     break
#                 if res is unknown:
#                     res = b
#                 elif b is not unknown:
#                     res = comp(res, b)
#         else:
#             res = null
#         if res is None:
#             res = True
#         return res

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

class Controller(Control):
    def __init__(self, **kw):
        self.__initialized = False
        super (Controller, self).__init__ (**kw)
        self.__initialized = True
    def __set_value(self, value):
        self.__value=value
        if self.__initialized:
            self.refresh()
    def __get_value(self):
        return self.__value
    value = property(__get_value, __set_value)
