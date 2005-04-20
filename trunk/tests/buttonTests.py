import unittest
from papo import cimarron
from commonTests import abstractTestControl

__all__ = ('TestButton',
           )

class TestButton(abstractTestControl):
    def setUp(self):
        super(TestButton, self).setUp()
        self.win = cimarron.skin.Window(title='Test', parent=self.app)
        self.parent = cimarron.skin.VBox (parent= self.win)
        self.widget = self.button = cimarron.skin.Button(label='Click me', parent=self.parent)
        self.setUpControl()

    def testLabel(self):
        self.assertEqual(self.button.label, 'Click me')

    def testSetLabel (self):
        raise NotImplementedError
