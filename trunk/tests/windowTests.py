import unittest
import sys
from cStringIO import StringIO

if '..' not in sys.path:
    sys.path.append('..')

from papo import cimarron
from commonTests import abstractTestWidget, abstractTestContainer

__all__ = ('TestWindow',
           )

class TestWindow(abstractTestContainer, abstractTestWidget):
    def setUp(self):
        super(TestWindow, self).setUp()
        self.widget = self.win = self.app.Window(title='Test', parent=self.app)
        self.parent = self.app

    def testWindowTitle(self):
        self.assertEqual(self.win.title, 'Test')

    def testShow(self):
        self.app.show()

if __name__ == '__main__':
    unittest.main()
