import unittest
import sys
from cStringIO import StringIO

if '..' not in sys.path:
    sys.path.append('..')

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
        stdout = sys.stdout
        sys.stdout = s = StringIO()
        self.label.show()
        s.seek(0)
        self.assertEqual(s.read(), self.label.text + '\n')
        sys.stdout = stdout

    def testShowAll(self):
        stdout = sys.stdout
        sys.stdout = s = StringIO()
        self.win.show()
        s.seek(0)
        title = '*'*80 + ' ' + self.win.title
        title = title[len(title)-80:]
        self.assertEqual(s.read(),
                         '\n'.join([title, self.label.text, '*'*80, '']))
        sys.stdout = stdout
        
