import unittest
from papo.cimarron import skin
from papo.cimarron.skins.common import Control
from commonTests import abstractTestControl

__all__ = ('TestController',
           )

class BarController (Control):
    def __init__ (self, **kw):
        super (BarController, self).__init__ (**kw)

class FooController(Control):
    def __init__(self, **kw):
        super (FooController, self).__init__ (**kw)
        self.box= skin.VBox (parent=self.parent)
        h= skin.HBox (parent=self.box)
        self.entry= skin.Entry (parent=h)
        self.label= skin.Label (parent=h, text='Nothing yet')
        self.button= skin.Button (parent= self.box, label='Press me')

        # connect them
        def onButtonAction(button, *a):
            # we put this Controller in the place of the Button
            # so the action seems to come (and indeed does!) from the controller
            self.onAction(self, *a)
        self.button.onAction= onButtonAction
        self.entry.onAction= self.changeModel
        self.defaultWidget = self.button

    def changeModel (self, *ignore):
        key = self.entry.value
        try:
            (key, value)= key.split (':', 1)
            self.value[key]= value
        except ValueError:
            pass
        self.label.text= str (self.value.get (key, 'Not found'))

class TestController(abstractTestControl):
    def setUp (self):
        self.value = dict(foo=1,
                          bar=2,
                          baz=3)

        super (TestController, self).setUp ()
        self.parent = self.win = skin.Window(title='Test', parent=self.app)
        self.widget= FooController (parent=self.win, value=self.value)

    def testModel (self):
        self.widget.entry.value = 'foo'
        self.widget.entry.onAction (self.widget)
        self.assertEqual(self.widget.label.text, '1')

    def testChangeModel(self):
        self.widget.entry.value = 'quux:5'
        self.widget.entry.onAction(self.widget)
        self.assertEqual(self.widget.label.text, '5')

    def tearDown(self):
        import gtk
        self.app.show()
        gtk.main()

class TestBarController (abstractTestControl):
    pass
