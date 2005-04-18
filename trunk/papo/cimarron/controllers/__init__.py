from papo import cimarron
from papo.cimarron.skins.common import Control, Container, ForcedYes, Unknown

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

class WindowContainer(list):
    def __init__(self, controller):
        super(WindowContainer, self).__init__()
        self.__controller = controller
    def append(self, window):
        super(WindowContainer, self).append(window)
        window.delegates.append(self.__controller)
        

class App(Controller, Container):
    def __init__(self, **kw):
        assert 'parent' not in kw, 'App should have no parent'
        super(App, self).__init__(**kw)
        self._children = WindowContainer(self)

    def run(self):
        cimarron.skin._run()

    def quit(self):
        cimarron.skin._quit()

    def will_hide(self, window):
        if len([i for i in self._children if i.visible])==1:
            self.quit()
            return ForcedYes
        return Unknown

    def schedule(self, timeout, callback, repeat=False):
        return cimarron.skin._schedule(timeout, callback, repeat)
