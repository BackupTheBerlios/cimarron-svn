import unittest
from papo import cimarron
from commonTests import abstractTestWidget, abstractTestContainer

__all__ = ('TestWindow',
           )

class TestWindow(abstractTestContainer, abstractTestWidget):
    def setUp(self):
        super(TestWindow, self).setUp()
        self.widget = self.win = cimarron.skin.Window(title='Test', parent=self.app)
        self.parent = self.app

    def testWindowTitle(self):
        self.assertEqual(self.win.title, 'Test')

if __name__ == '__main__':
    unittest.main()
