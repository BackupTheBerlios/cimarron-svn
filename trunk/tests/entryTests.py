import unittest
from papo.cimarron import skin
from commonTests import abstractTestControl

__all__ = ('TestEntry',
           )

class TestEntry(abstractTestControl):
    def setUp(self):
        super(TestEntry, self).setUp()
        self.parent = self.win = skin.Window(title='Test', parent=self.app)
        self.widget = self.entry = skin.Entry(parent=self.win)
        self.setUpControl()

    def testSetValue (self):
        self.widget.value= 'this is a test'
        self.assertEqual (self.widget._widget.get_text(), self.widget.value)
