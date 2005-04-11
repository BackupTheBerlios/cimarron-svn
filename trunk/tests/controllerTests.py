import unittest
from papo.cimarron import skin
from papo.cimarron.skins.common import Control
from commonTests import abstractTestControl

__all__ = ('TestController',
           'TestBarController',
           )

class FooController(Control):
    def __init__(self, **kw):
        super (FooController, self).__init__ (**kw)
        self.box= skin.VBox (parent=self.parent)
        h= skin.HBox (parent=self.box)
        self.entry= skin.Entry (parent=h)
        self.label= skin.Label (parent=h, text='Nothing yet')
        self.defaultWidget = self.button= skin.Button (parent=self.box, label='Press me')
        self.daLabel= skin.Label (parent=self.box)

        # this is BAAAAAD
        self._widget= self.defaultWidget._widget

        # connect them
        def onButtonAction(button, *a):
            # we put this Controller in the place of the Button
            # so the action seems to come (and indeed does!) from the controller
            self.onAction(*a)
        self.button.onAction= onButtonAction
        self.entry.onAction= self.changeModel

    def changeModel (self, *ignore):
        key = self.entry.value
        try:
            (key, value)= key.split (':', 1)
            self.value[key]= value
        except ValueError:
            pass
        self.label.text= str (self.value.get (key, 'Not found'))
        self.daLabel.text= str (self.value)

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

class BarController (Control):
    def __init__ (self, **kw):
        super (BarController, self).__init__ (**kw)
        v= skin.VBox (parent=self.parent)
        h= skin.HBox (parent= v)
        self.prev= skin.Button (parent= h, label='<<', value=-1)
        self.next= skin.Button (parent= h, label='>>', value=1)
        self.index= 0

        def onFooAction(foo, *a):
            self.onAction(*a)
        self.defaultWidget= self.foo= FooController (parent=v, value=self.value[self.index], onAction=onFooAction)

        def roll(button, *a):
            try:
                self.index+= button.value
                self.foo.value= self.value[self.index]
            except IndexError:
                self.index-= button.value

        self.prev.onAction= roll
        self.next.onAction= roll

class TestBarController (abstractTestControl):
    def setUp (self):
        self.value = (dict(foo=1,
                           bar=2,
                           baz=3), dict (a=1, b= 2, c= 3))
        super (TestBarController, self).setUp ()
        self.parent = self.win = skin.Window(title='Test 2', parent=self.app)
        def here (*a):
            print 'here!'
        self.widget= BarController (parent=self.win, value=self.value, onAction=here)


    def testRoll (self):
        self.widget.next.onAction()

    def tearDown(self):
        import gtk
        self.app.show()
        gtk.main()

