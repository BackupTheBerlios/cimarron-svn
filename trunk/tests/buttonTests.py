import unittest
import sys
from cStringIO import StringIO

if '..' not in sys.path:
    sys.path.append('..')

from papo import cimarron
from commonTests import abstractTestControl

__all__ = ('TestButton',
           )

class TestButton(abstractTestControl):
    def setUp(self):
        super(TestButton, self).setUp()
        self.parent = self.win = self.app.Window(title='Test', parent=self.app)
        self.widget = self.button = self.app.Button(label='Click me', parent=self.win)
        self.setUpControl()

    def testLabel(self):
        self.assertEqual(self.button.label, 'Click me')
