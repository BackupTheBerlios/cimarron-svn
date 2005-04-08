import unittest
from papo import cimarron
from commonTests import abstractTestWidget

__all__ = ('TestLabel',
           )

class TestLabel(abstractTestWidget):
    def setUp(self):
        super(TestLabel, self).setUp()
        self.parent = self.win = self.app.Window(title='Test', parent=self.app)
        self.widget = self.label = self.app.Label(text='hello', parent=self.win)

    def testLabel(self):
        self.assertEqual(self.label.text, 'hello')

    def testShow(self):
        self.win.show()
