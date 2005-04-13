import unittest
from papo.cimarron import skin
from commonTests import abstractTestControl

__all__ = ('TestButton',
           )

class TestButton(abstractTestControl):
    def setUp(self):
        super(TestButton, self).setUp()
        self.parent = self.win = skin.Window(title='Test', parent=self.app)
        self.widget = self.button = skin.Button(label='Click me', parent=self.win)
        self.setUpControl()

    def testLabel(self):
        self.assertEqual(self.button.label, 'Click me')

    def testSetLabel (self):
        self.widget.label= "Don't click me"
        self.assertEqual(self.widget.label, self.widget._widget.get_label ())

