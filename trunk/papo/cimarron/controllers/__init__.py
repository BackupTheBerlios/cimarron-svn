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

class Column (object):
    def __init__ (self, name='', read=None, write=None, entry=None):
        self.name= name
        if not callable (read):
            raise ValueError, 'read parameter must be callable'
        self.read= read
        if not callable (write):
            raise ValueError, 'write parameter must be callable'
        self.write= write
        self.entry= entry

class Grid (Controller):
    def __init__ (self, data=[], columns=None, **kw):
        self.__initialized= False
        self.columns= columns
        self.labels= []
        self.entries= {}

        self.index= None
        self.data= data

        super (Grid, self).__init__ (**kw)
        self.widget= v= cimarron.skin.VBox (parent=self.parent)
        self.__initialized= True

    def __set_data (self, data):
        self.__data= data
        self.refresh ()
        if len (data)>0:
            self.index= 0
    def __get_data (self):
        return self.__data
    data= property (__get_data, __set_data)
    def updateData (self, entry, *i):
        if self.columns[entry.column].write is not None:
            self.columns[entry.column].write (self.data[entry.row], entry.value)

    def refresh (self):
        for i in xrange (len (self.data)):
            if len (self.labels)<=i:
                # the row does not exist, so we add it
                h= cimarron.skin.HBox (parent=self.widget)
                b= cimarron.skin.Label (
                    parent= h,
                    text= ' ',
                    row= i
                    )

                self.labels.append (b)

                # now the entries
                for j in xrange (len (self.columns)):
                    entryConstr= self.columns[j].entry or cimarron.skin.Entry
                    self.entries[i, j]= entryConstr (
                        parent= h,
                        value= self.columns[j].read (self.data[i]),
                        onAction= self.updateData,
                        column= j,
                        row= i,
                        )
                    self.entries[i, j].delegates.append (self)
            else:
                for j in xrange (len (self.columns)):
                    self.entries[i, j].value= self.columns[j].read (self.data[i])

    def will_focus_in (self, entry, *ignore):
        self.index= entry.row
        return Unknown

    def __set_index (self, index):
        if self.__initialized and self.index is not None:
            self.labels[self.index].text= ' '
            self.labels[index].text= '>'
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

class SelectionWindow (Controller):
    def __init__ (self, columns=[], **kw):
        super (SelectionWindow, self).__init__ (**kw)
        self.win= cimarron.skin.Window (
            parent= self.parent,
            title= 'Select',
            )
        v= cimarron.skin.VBox (parent=self.win)
        self.grid= Grid (
            parent= v,
            columns= columns
        )
        h= cimarron.skin.HBox (parent=v)
        self.ok= cimarron.skin.Button (
            parent= h,
            label= 'Ok',
            onAction= self.onOk,
            )
        self.cancel= cimarron.skin.Button (
            parent= h,
            label= 'Cancel',
            onAction= self.onCancel,
        )

    def show (self):
        self.value= None
        self.win.show ()

    def onOk (self, *ignore):
        self.value= self.grid.value
        self.win.hide ()
        self.onAction ()

    def onCancel (self, *ignore):
        self.value= None
        self.win.hide ()
        self.onAction ()

    def hide (self):
        self.win.hide ()

    def refresh (self):
        self.grid.refresh ()

class Search (Controller):
    def __init__ (self, columns=[], **kw):
        super (Search, self).__init__ (**kw)
        self.columns= columns
        self.entries= []
        self.value= None

        h= cimarron.skin.HBox (
            parent= self.parent,
            )
        for c in self.columns:
            entryConstr= c.entry or cimarron.skin.Entry
            self.entries.append (cimarron.skin.Entry (
                parent= h,
                onAction= self.doSearch
                ))

        b= cimarron.skin.Button (
            parent= h,
            label= 'Search!',
            onAction= self.doSearch,
            )

        # build the selection window
        self.selwin= SelectionWindow (
            columns= self.columns,
            onAction= self.selected,
            )

        # socking tests
        self._widget= b._widget

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
            self.selwin.grid.data= ans
            self.selwin.show ()
        self.onAction ()

    def selected (self, *ignore):
        self.value= self.selwin.value
        self.selwin.hide ()
        self.onAction ()

    def search (self, *data):
        raise NotImplementedError

    def refresh (self):
        if self.value is not None:
            for i in xrange (len (self.entries)):
                self.entries[i].value= self.columns[i].read (self.value)
        else:
            for i in xrange (len (self.entries)):
                self.entries[i].value= ''
