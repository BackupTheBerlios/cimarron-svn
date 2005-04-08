import unittest
from papo import cimarron
from commonTests import abstractTestControl

__all__ = ('TestEntry',
           )

class TestEntry(abstractTestControl):
    def setUp(self):
        super(TestEntry, self).setUp()
        self.parent = self.win = self.app.Window(title='Test', parent=self.app)
        self.widget = self.entry = self.app.Entry(parent=self.win)
        self.setUpControl()
