import unittest
from papo import cimarron
from commonTests import abstractTestControl
from papo.cimarron.controllers import App, Grid, Column

__all__= ('TestGrid', 'Person')


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
            Column (name='Nombre', read=Person.getName, write=Person.setName),
            Column (name='Apellido', read=Person.getSurname, write=Person.setSurname),
            )

        self.parent = self.win = cimarron.skin.Window(title='Test', parent=self.app)
        self.widget= self.grid= Grid (
            parent= self.parent,
            columns= columns,
            rows= 5,
            )

        # so testValue passes
        self.value= None
        self.widget.data= self.model

    def testIndex (self):
        for i in xrange (len (self.model)):
            self.widget.index= i
            self.assertEqual (self.model[i], self.widget.value)

    def testValue (self):
        for i in xrange (len (self.model)):
            self.widget.value= self.model[i]
            self.assertEqual (self.model[i], self.widget.value)

    def testNoValue (self):
        self.widget.data = []
        self.widget.value= None
        self.assertEqual (self.widget.value, None)

    def testWrite (self):
        # self.widget.entries[0, 0]._widget.set_text ('juan')
        self.widget.entries[0, 0].value= 'juan'
        self.widget.entries[0, 0].onAction ()
        self.widget.index= 0
        self.assertEqual (self.widget.value.name, 'juan')
