import unittest
from papo import cimarron
from commonTests import abstractTestControl

__all__ = ('TestController',
           )

class FooController(cimarron.skins.common.Control):
    def __init__(self, **kw):
        super (FooController, self).__init__ (**kw)
        self.box= self.parent.skin.VBox (parent=self.parent)
        h= self.parent.skin.HBox (parent=self.box)
        self.entry= self.parent.skin.Entry (parent=h)
        self.label= self.parent.skin.Label (parent=h, text='Nothing yet')
        self.button= self.skin.Button (parent= self.box, label='Press me')

        # connect them
        def onButtonAction(button, *a):
            self.onAction(self, *a)
        self.button.onAction= onButtonAction
        self.entry.onAction= self.modelChanged
        self._widget= self.button._widget

    def modelChanged (self, *ignore):
        self.label.text= repr (self.value.get (self.entry.value, 'Not found'))

class TestController(abstractTestControl):
    def setUp (self):
        self.value = dict(foo=1,
                          bar=2,
                          baz=3)

        super (TestController, self).setUp ()
        self.parent = self.win = self.app.Window(title='Test', parent=self.app)
        self.widget= FooController (parent=self.win, value=self.value)

#         self.setUpControl (value=self.model)

#     def testActivated (self):
#         def activated (*ignore):
#             self.activated= True
#         self.widget.onAction= activated
#         self.widget.button.onAction (self.widget)
#         self.assertEqual(self.activated, True)
#
#     def testModel (self):
#         self.widget.entry.value = 'foo'
#         self.widget.entry.onAction (self.widget)
#         self.assertEqual(self.widget.label.text, '1')

#     def tearDown(self):
#         import gtk
#         self.app.show()
#         gtk.main()
