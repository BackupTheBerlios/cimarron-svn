import unittest
import sys
if '..' not in sys.path:
    sys.path.append('..')
from cStringIO import StringIO

from papo import cimarron

__all__ = ('TestHelloWorld',)

class TestHelloWorld(unittest.TestCase):
    def setUp(self):
        sys.argv[1:] = ['--skin=testable']
        self.app = cimarron.App()
    def testSkinArgv(self):
        self.assertEqual(self.app.skin.__name__, 'papo.cimarron.skins.testable')
    def testWindow(self):
        self.win = self.app.Window()
    def testWindowParent(self):
        self.win = self.app.Window(parent=self.app)
        self.assertEqual(self.app, self.win.parent)
        self.assertEqual(list(self.app.children), [self.win])
    def testWindowTitle(self):
        self.win = self.app.Window(parent=self.app, title='hello')
        self.assertEqual(self.win.title, 'hello')
    def testLabel(self):
        self.testWindowTitle()
        self.label = self.app.Label(text='Hello, World!', parent=self.win)
        self.assertEqual(self.label.text, 'Hello, World!')
        self.assertEqual(self.win, self.label.parent)
    def testShow(self):
        self.testLabel()
        stdout = sys.stdout
        sys.stdout = s = StringIO()
        self.app.show()
        s.seek(0)
        #self.assertEqual(s.read(),
        #                 '\n'.join(['*'*80, self.label.text, '*'*80, '']))

if __name__ == '__main__':
    unittest.main()
