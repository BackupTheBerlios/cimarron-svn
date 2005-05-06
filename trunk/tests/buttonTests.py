import unittest
from papo import cimarron
from commonTests import abstractTestControl

__all__ = ('TestButton',
           'TestCheckbox',
           )

class TestButton(abstractTestControl):
    def setUp(self):
        super(TestButton, self).setUp()
        self.win = cimarron.skin.Window(title='Test', parent=self.app)
        self.parent = cimarron.skin.VBox (parent= self.win)
        self.widget = cimarron.skin.Button(label='Click me', parent=self.parent)
        self.setUpControl()

    def testLabel(self):
        self.assertEqual(self.widget.label, 'Click me')

    def testSetLabel (self):
        raise NotImplementedError

class TestCheckbox(TestButton):
    def setUp(self):
        super(TestCheckbox, self).setUp()
        self.widget = cimarron.skin.Checkbox(label='Click me', parent=self.parent)
        self.setUpControl()

    def testChecked(self):
        self.widget.checked = True
        self.assertEqual(self.widget.checked, True)
        self.widget.checked = False
        self.assertEqual(self.widget.checked, False)
