import unittest
from papo.cimarron import skin
from commonTests import abstractTestControl

__all__ = ('TestEntry',
           )

class TestEntry(abstractTestControl):
    def setUp(self):
        super(TestEntry, self).setUp()
        self.win = skin.Window(title='Test', parent=self.app)
        self.parent = skin.VBox (parent= self.win)
        self.widget = self.entry = skin.Entry(parent=self.parent)
        self.setUpControl()

    def testSetValue (self):
        raise NotImplementedError, 'you should subclass testEntry'

