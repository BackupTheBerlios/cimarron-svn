import unittest
from papo.cimarron import skin, App

__all__ = ('TestHelloWorld',)

class TestHelloWorld(unittest.TestCase):
    def setUp(self):
        #sys.argv[1:] = ['--skin=testable']
        self.app = App()
    def testSkinArgv(self):
        self.assertEqual(skin.__name__, 'papo.cimarron.skins.gtk2')
    def testWindow(self):
        self.win = skin.Window()
    def testWindowParent(self):
        self.win = skin.Window(parent=self.app)
        self.assertEqual(self.app, self.win.parent)
        self.assertEqual(list(self.app.children), [self.win])
    def testWindowTitle(self):
        self.win = skin.Window(parent=self.app, title='hello')
        self.assertEqual(self.win.title, 'hello')
    def testLabel(self):
        self.testWindowTitle()
        self.label = skin.Label(text='Hello, World!', parent=self.win)
        self.assertEqual(self.label.text, 'Hello, World!')
        self.assertEqual(self.win, self.label.parent)
#     def testShow(self):
#         self.testLabel()
#         stdout = sys.stdout
#         sys.stdout = s = StringIO()
#         self.app.show()
#         s.seek(0)
        #self.assertEqual(s.read(),
        #                 '\n'.join(['*'*80, self.label.text, '*'*80, '']))

if __name__ == '__main__':
    unittest.main()