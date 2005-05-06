import unittest
from papo import cimarron
from commonTests import abstractTestControl

__all__ = ('TestEntry',
           )

class TestEntry(abstractTestControl):
    def setUp(self):
        super(TestEntry, self).setUp()
        self.win = cimarron.skin.Window(title='Test', parent=self.app)
        self.parent = cimarron.skin.VBox (parent= self.win)
        self.widget = self.entry = cimarron.skin.Entry(parent=self.parent)
        self.setUpControl()

    def testSetValue (self):
        raise NotImplementedError, 'you should subclass testEntry'
