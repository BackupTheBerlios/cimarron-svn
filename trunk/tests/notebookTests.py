import unittest
from papo import cimarron
from commonTests import abstractTestContainer

__all__= ('TestNotebook', )

class TestNotebook (abstractTestContainer):
    def setUp (self):
        super (TestNotebook, self).setUp ()
        self.parent= cimarron.skin.Window (parent= self.app)
        self.widget= cimarron.skin.Notebook (parent= self.parent)

    def testAddChild (self):
        self.other= cimarron.skin.Entry ()
        self.other.label= 'first'
        self.other.parent= self.widget

        self.assertEqual (True, True)

    def testVisual (self):
        self.testAddChild ()
        self.app.show ()
        self.app.run ()
