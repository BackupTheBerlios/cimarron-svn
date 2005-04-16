import unittest
from papo import cimarron
from commonTests import abstractTestControl
from papo.cimarron.controllers import App, Controller

__all__= ('TestGrid', )

class Grid (Controller):
    def __init__ (self, data=[], columns=None, **kw):
        self.__initialized= False
        self.columns= columns
        self.buttons= []
        self.entries= {}

        # these two update the view :(
        self.index= None
        self.data= data

        super (Grid, self).__init__ (**kw)
        self.widget= v= cimarron.skin.VBox (parent=self.parent)
        self.__initialized= True

        # and then another update :(
        self.update ()

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
                self.buttons.append (cimarron.skin.Button (parent=h, label=' '))
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

class Person (object):
    def __init__ (self, name, surname):
        self.setName (name)
        self.setSurname (surname)

    def getName (self):
        return self.__name
    def setName (self, name):
        self.__name= name
    name= property (getName, setName)

    def getSurname (self):
        return self.__surname
    def setSurname (self, sn):
        self.__surname= sn
    surname= property (getSurname, setSurname)

class TestGrid (abstractTestControl):
    def setUp (self):
        super (TestGrid, self).setUp ()
        self.model= [
            Person ('jose', 'perez'),
            Person ('marcos', 'dione'),
            Person ('john', 'lenton'),
            ]
        columns= (
            dict (name='Nombre', read=Person.getName, write=Person.setName, search=None),
            dict (name='Apellido', read=Person.getSurname, write=Person.setSurname, search=None),
            )

        self.parent = self.win = cimarron.skin.Window(title='Test', parent=self.app)
        self.widget= self.grid= Grid (
            parent= self.parent,
            columns= columns,
            )

        # so testValue passes
        self.value= None

    def testData (self):
        self.widget.data= self.model

    def testIndex (self):
        self.testData ()
        for i in xrange (len (self.model)):
            self.widget.index= i
            self.assertEqual (self.model[i], self.widget.value)

    def testValue (self):
        self.testData ()
        for i in xrange (len (self.model)):
            self.widget.value= self.model[i]
            self.assertEqual (self.model[i], self.widget.value)

#         self.app.show()
#         self.app.run ()

    def testNoValue (self):
        self.widget.value= None
        self.assertEqual (self.widget.value, None)

    def testWrite (self):
        self.testData ()
        # self.widget.entries[0, 0]._widget.set_text ('juan')
        self.widget.entries[0, 0].value= 'juan'
        self.widget.entries[0, 0].onAction ()
        self.widget.index= 0
        self.assertEqual (self.widget.value.name, 'juan')

if 0:
    def testLive(self):
        self.testData ()
        self.app.show()
        self.app.run ()
