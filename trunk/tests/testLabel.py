import unittest
from papo import cimarron
from testCommon import abstractTestWidget

__all__ = ('TestLabel',
           )

class TestLabel(abstractTestWidget):
    def setUp(self):
        super(TestLabel, self).setUp()
        self.parent = self.win = cimarron.skin.Window(title='Test', parent=self.app)
        self.widget = self.label = cimarron.skin.Label(text='hello', parent=self.win)

    def testLabel(self):
        self.assertEqual(self.label.text, 'hello')

    def testSetLabel(self):
        raise NotImplementedError
        
    def testShow(self):
        self.win.show()
