# -*- coding: utf-8 -*-
#
# Copyright 2005 Fundación Via Libre
#
# This file is part of PAPO.
#
# PAPO is free software; you can redistribute it and/or modify it under the
# terms of the GNU General Public License as published by the Free Software
# Foundation; either version 2 of the License, or (at your option) any later
# version.
#
# PAPO is distributed in the hope that it will be useful, but WITHOUT ANY
# WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
# FOR A PARTICULAR PURPOSE.  See the GNU General Public License for more
# details.
#
# You should have received a copy of the GNU General Public License along with
# PAPO; if not, write to the Free Software Foundation, Inc., 59 Temple Place,
# Suite 330, Boston, MA 02111-1307 USA

import os
import libxml2
from papo import cimarron
from papo.cimarron.skins.common import Control, Container, ForcedYes, Unknown

__all__ = ('Controller', 'App', 'Column', 'SearchEntry', 'WindowController', 'Grid')

class Controller(Control, Container):
    """
    A Controller is the glue between a View and a Model,
    coordinating the reactions to the View's events to
    changes in the Model.
    """
    mainWidget = None # mainWidget is the "default" Control of the
                      # Controller, that which fires when you press
                      # enter.
    def __init__(self, **kw):
        self.__initialized = False
        super (Controller, self).__init__ (**kw)
        self.__initialized = True
    def _set_value(self, value):
        self.__value=value
        if self.__initialized:
            self.refresh()
    def _get_value(self):
        return self.__value
    value = property(_get_value, _set_value, doc="""Holds the Model for the B{Controller}.
        Note that the name is the same that the I{value} for B{Control}.
        That way, Controllers can act as Controls.""")

    def fromXmlFile(klass, filename):
        """
        Load a Cimarrón app from an xml file.
        """
        if os.path.isfile(filename):
            net= klass.fromXmlObj(libxml2.parseFile(filename), cimarron.skin)
            net._connectNet ([net])
            return net
        else:
            raise OSError, "Unable to open file: %r" % filename
    fromXmlFile = classmethod(fromXmlFile)

    def _connectNet (self, widgetList):
        while widgetList:
            w= widgetList.pop (0)
            w._connectWith (self)

            # add children
            if hasattr (w, 'children'):
                widgetList+= w.children

class WindowContainer(list):
    """
    Not public. Please Ignore :)
    """
    def __init__(self, controller):
        super(WindowContainer, self).__init__()
        self.__controller = controller
    def append(self, window):
        super(WindowContainer, self).append(window)
        window.delegates.append(self.__controller)

class App(Controller):
    """
    An App represents the main loop of the application.
    It is the C{parent} for the first B{Window}s.
    """
    def __init__(self, **kw):
        assert 'parent' not in kw, 'App should have no parent'
        super(App, self).__init__(**kw)
        self._children = WindowContainer(self)

    def run(self):
        """
        Run the App. Will actually show any shown window,
        and keep runnuing until:
          - all the windows are closed, or
          - someone calls C{quit()} and no window opposes
            to the action.
        """
        cimarron.skin._run()

    def quit(self):
        """
        Terminates the App.
        """
        cimarron.skin._quit()

    def will_hide(self, window):
        if len([i for i in self._children if i.visible])==1:
            self.quit()
            return ForcedYes
        return Unknown

    def schedule(self, timeout, callback, repeat=False):
        """
        Add a new timer for the app. When the C{timeout} expires,
        the C{callback} gets called.
        """
        return cimarron.skin._schedule(timeout, callback, repeat)

    def concreteParenter (self, child):
        pass

    def refresh(self):
        pass

class Column (object):
    """
    A Column describes a field. This field can be used for both
    B{SearchEntry}s and B{Grid}s.
    """
    def __init__ (self, name='', read=None, write=None, entry=None):
        """
        @param name: A text associated with the field.
            In the case of B{Grids}, it's the colunm header.

        @param read: A callable that, given an object, returns the value
            of that object for the field. Tipically, is an unbound getter
            method from the object class.

        @param write: A callable that, given an object and a new value,
            modifies the object. Tipically, is an unbound setter method
            from the object class.
        """
        self.name= name
        if not callable (read):
            raise ValueError, 'read parameter must be callable'
        self.read= read
        if write is not None and not callable (write):
            raise ValueError, 'write parameter must be callable'
        self.write= write
        if entry is None:
            entry = cimarron.skin.Entry
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

    def mainWidget(self):
        return self.entries[self.index,0]
    mainWidget = property(mainWidget)

    def _set_data (self, data):
        self.__data= data
        self.refresh ()
        if data is not None and len (data)>0:
            self.index= 0
    def _get_data (self):
        return self.__data
    data= property (_get_data, _set_data)
    def updateData (self, entry, *i):
        if self.columns[entry.column].write is not None:
            self.columns[entry.column].write (self.data[entry.row], entry.value)

    def selected (self, entry, *ignore):
        self.updateData (entry)
        self.onAction ()

    def refresh (self):
        try:
            # normal case: data is some sequence
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
                            onAction= self.selected,
                            column= j,
                            row= i,
                            )
                        self.entries[i, j].delegates.append (self)
                else:
                    for j in xrange (len (self.columns)):
                        self.entries[i, j].value= self.columns[j].read (self.data[i])
            for i in xrange (len (self.data), len (self.labels)):
                for j in xrange (len (self.columns)):
                    self.entries[i, j].value= ''

        except TypeError:
            # except case: data is something else (tipically, `NoneÂ´)
            for i in xrange (len (self.labels)):
                for j in xrange (len (self.columns)):
                    self.entries[i, j].value= ''

    def will_focus_in (self, entry, *ignore):
        self.index= entry.row
    def will_focus_out (self, entry, *ignore):
        self.updateData (entry)

    def _set_index (self, index):
        if self.__initialized and self.index is not None:
            self.labels[self.index].text= ' '
            if index is not None:
                self.labels[index].text= '>'
        self.__index= index
    def _get_index (self):
        return self.__index
    index= property (_get_index, _set_index)

    def _get_value (self):
        ans= None
        if self.index is not None:
            ans= self.data[self.index]
        return ans
    def _set_value (self, value):
        try:
            index= self.data.index (value)
        except (ValueError, AttributeError):
            index= None
        self.index= index
    value= property (_get_value, _set_value)

class SelectionWindow (Controller):
    """
    Not public. Please Ignore :)
    """
    def __init__ (self, columns=[], **kw):
        super (SelectionWindow, self).__init__ (**kw)
        self.win= cimarron.skin.Window (
            parent= self.parent,
            title= 'Select',
            )
        v= cimarron.skin.VBox (parent=self.win)
        self.grid= cimarron.skin.Grid (
            parent= v,
            columns= columns,
            onAction= self.onOk,
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

class SearchEntry (Controller):
    """
    Abstract class for searching. Consist of a widget
    with one Entry for each Column.

    The method C{search()} must be
    implemented in the subclass, which sould take one parameter
    for each column and return the list of objects found to that
    search criteria.

    This class already handles the case when the amount of objets
    found is greater that one. In that case, it presents a window
    where the user can select from a list.

    When one object is found or selected, it calls the action.
    """
    def __init__ (self, columns=[], **kw):
        """
        @param columns: A list of Columns. Only the C{read} attribute
            needs to be set.
        """
        super (SearchEntry, self).__init__ (**kw)
        self.columns= columns
        self.entries= []
        self.value= None

        h= cimarron.skin.HBox (
            parent= self.parent,
            )
        for c in self.columns:
            entryConstr= c.entry
            self.entries.append (entryConstr (
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

        self.mainWidget = b

    def doSearch (self, *ignore):
        """
        Performs the abstract search, and handles the case
        when more than one object is found.
        """
        data= []
        for e in self.entries:
            data.append (e.value)

        ans= self.search (data)
        if len (ans)==0:
            self.value= None
        elif len (ans)==1:
            self.value= ans[0]
        if len (ans)>1:
            # select
            self.selwin.grid.data= ans
            self.selwin.show ()
        else:
            self.onAction ()

    def selected (self, *ignore):
        """
        Callback for the selection window when finally
        one object is selected.
        """
        self.value= self.selwin.value
        self.selwin.hide ()
        self.onAction ()

    def search (self, *data):
        """
        This abstract method is called for performing the actual search
        with the values of the Entrys as search criteria. Must return the
        list of objects that match that criteria.
        """
        raise NotImplementedError

    def refresh (self):
        """
        Show the value.
        """
        if self.value is not None:
            for i in xrange (len (self.entries)):
                self.entries[i].value= self.columns[i].read (self.value)
        else:
            for i in xrange (len (self.entries)):
                self.entries[i].value= ''

class WindowController (Controller):
    """
    A WindowController just handles a Window.
    Is typical that each Window will have an associated Controller.
    Those Controllers must inherit from this class.
    """
    def __init__ (self, **kw):
        super (WindowController, self).__init__ (**kw)
        self.win= cimarron.skin.Window (parent= self)
        self.win.delegates.insert (0, self)

    def visibleChildren (self):
        return [i for i in self._children if getattr (i, 'visible', False) and i.visible]

    def will_hide (self, *ignore):
        return self.delegate ('will_hide')

    def show (self):
        """
        Show the window.
        """
        self.win.show ()

    def hide (self):
        """
        Hide the window.
        """
        self.win.hide ()

    def _get_visible (self):
        return len(self.visibleChildren ())>0
    visible= property (_get_visible, None, None,
        """Is the window shown?""")

class Grid (Controller):
    """
    Fallback implementation of Grid.
    """
    def __init__ (self, data=[], columns=None, **kw):
        self.__initialized= False
        self.columns= columns
        self.labels= []
        self.entries= {}

        self.index= None
        self.widget= v= cimarron.skin.VBox (parent=self.parent)
        self.data= data

        super (Grid, self).__init__ (**kw)
        self.__initialized= True

    def mainWidget(self):
        return self.entries[self.index,0]
    mainWidget = property(mainWidget)

    def _set_data (self, data):
        self.__data= data
        self.refresh ()
        if data is not None and len (data)>0:
            self.index= 0
    def _get_data (self):
        return self.__data
    data= property (_get_data, _set_data, None,
        """The list of objects to be shown.""")
    def updateData (self, entry, *i):
        if self.columns[entry.column].write is not None:
            self.columns[entry.column].write (self.data[entry.row], entry.value)

    def selected (self, entry, *ignore):
        self.updateData (entry)
        self.onAction ()

    def refresh (self):
        try:
            # normal case: data is some sequence
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
                            onAction= self.selected,
                            column= j,
                            row= i,
                            )
                        self.entries[i, j].delegates.append (self)
                else:
                    for j in xrange (len (self.columns)):
                        self.entries[i, j].value= self.columns[j].read (self.data[i])
            for i in xrange (len (self.data), len (self.labels)):
                for j in xrange (len (self.columns)):
                    self.entries[i, j].value= ''

        except TypeError:
            # except case: data is something else (tipically, `None´)
            for i in xrange (len (self.labels)):
                for j in xrange (len (self.columns)):
                    self.entries[i, j].value= ''

    def will_focus_in (self, entry, *ignore):
        self.index= entry.row
    def will_focus_out (self, entry, *ignore):
        self.updateData (entry)

    def _set_index (self, index):
        if self.__initialized and self.index is not None:
            self.labels[self.index].text= ' '
            if index is not None:
                self.labels[index].text= '>'
        self.__index= index
    def _get_index (self):
        return self.__index
    index= property (_get_index, _set_index, None,
                     """The index of the object currently selected.
                     If no object is selected, it is None.""")

    def _get_value (self):
        ans= None
        if self.index is not None:
            ans= self.data[self.index]
        return ans
    def _set_value (self, value):
        try:
            index= self.data.index (value)
        except (ValueError, AttributeError):
            index= None
        self.index= index
    value= property (_get_value, _set_value, None,
                     """The selected object. If no object is selected, it is None.""")

class CrUDController (WindowController):
    """
    Cr(eate)U(pdate)D(elete) Controller.
    """
    def __init__ (self, klass=None, editorKlass=None, filename='', **kw):
        super (CrUDController, self).__init__ (**kw)
        self.note= cimarron.skin.Notebook (parent=self.win)

        # first tab
        v= cimarron.skin.VBox ()
        v.label= 'Search'
        v.parent= self.note

        self.new= cimarron.skin.Button (
            parent= v,
            label= 'New',
            onAction= lambda control, *ignore: self.newModel (control, klass, *ignore),
            )

        # second tab
        # load the beast from xml
        self.modelEditor= editorKlass.fromXmlFile (filename)
        self.modelEditor.parent= self.note

        # more tabs?

    def newModel (self, control, klass, *ignore):
        self.value= klass ()
        self.modelEditor.value= self.value
        self.note.activate (self.modelEditor)
        # and this?
        # self.editor.focus ()

    def refresh (self):
        # update all the `children'
        for child in self.note.children:
            try:
                child.refresh ()
            except AttributeError:
                pass
