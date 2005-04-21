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

class Grid (Controller):
    def __init__ (self, data=[], columns=None, **kw):
        self.__initialized= False
        self.columns= columns
        self.buttons= []
        self.entries= {}

        self.index= None
        self.data= data

        super (Grid, self).__init__ (**kw)
        self.widget= v= cimarron.skin.VBox (parent=self.parent)
        self.__initialized= True

    def updateCursor (self, entry, *ignore):
        self.index= entry.row

    def __set_data (self, data):
        self.__data= data
        self.update ()
        if len (data)>0:
            self.index= 0
    def __get_data (self):
        return self.__data
    data= property (__get_data, __set_data)

    def update (self):
        for i in xrange (len (self.data)):
            if len (self.buttons)<=i:
                # the row does not exist, so we add it
                h= cimarron.skin.HBox (parent=self.widget)
                self.buttons.append (cimarron.skin.Button (
                    parent= h,
                    label= ' ',
                    ))
            for j in xrange (len (self.columns)):
                if self.entries.has_key ((i, j)):
                    self.entries[i, j].value= self.columns[j]['read'](self.data[i])
                else:
                    self.entries[i, j]= cimarron.skin.Entry (
                        parent= h,
                        value= self.columns[j]['read'](self.data[i]),
                        onFocusIn= self.updateCursor,
                        onAction= self.updateData,
                        column= j,
                        row= i,
                        )

    def updateData (self, entry, *i):
        self.columns[entry.column]['write'](self.data[entry.row], entry.value)

    def __set_index (self, index):
        if self.__initialized and self.index is not None:
            self.buttons[self.index].label= ' '
            self.buttons[index].label= '>'
        self.__index= index
    def __get_index (self):
        return self.__index
    index= property (__get_index, __set_index)

    def __get_value (self):
        ans= None
        if self.index is not None:
            ans= self.data[self.index]
        return ans
    def __set_value (self, value):
        try:
            index= self.data.index (value)
        except ValueError:
            index= None
        self.index= index
    value= property (__get_value, __set_value)

class Search (Controller):
    def __init__ (self, search= None, entries= [], **kw):
        super (Search, self).__init__ (**kw)
        self.search= search
        box= HBox (
            parent= self.parent,
            )

        self.entries= []
        for e in entries:
            e.parent= box
            e.onAction= self.doSearch
            self.entries.append (e)

    def doSearch (self, *ignore):
        data= []
        for e in self.entries:
            data.append (e.value)

        ans= self.search (data)
        if len (ans)==0:
            self.value= None
        elif len (ans)==1:
            self.value= ans[0]
        else:
            # select
            self.value= ans[-1]
