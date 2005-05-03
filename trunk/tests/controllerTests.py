import unittest
from pprint import pformat
from papo import cimarron
from papo.cimarron.controllers import Controller, App
from commonTests import abstractTestControl

__all__ = ('TestController',
           'TestBarController',
           'TestApp',
           )

def visualTest():
    app = App()
    cimarron.config()
    win = cimarron.skin.Window(parent=app)
    foo = FooController(parent=win, value=dict(foo=1,bar=2,baz=3))
    app.show()
    app.run()

class FooController(Controller):
    def __init__(self, **kw):
        super (FooController, self).__init__ (**kw)
        self.box= cimarron.skin.VBox (parent=self)
        h= cimarron.skin.HBox (parent=self.box)
        self.entry= cimarron.skin.Entry (parent=h)
        self.label= cimarron.skin.Label (parent=h, text='Nothing yet')
        self.button= cimarron.skin.Button (parent=self.box, label='Press me')
        self.daLabel= cimarron.skin.Label (parent=self.box)

        cimarron.skin.concreteParenter(parent=self.parent,
                                       child=self.box)
        self.mainWidget = self.button

        # connect them
        def onButtonAction(button, *a):
            # we put this Controller in the place of the Button
            # so the action seems to come (as it does!) from the controller
            self.onAction(*a)
        self.button.onAction= onButtonAction
        self.entry.onAction= self.changeModel

        # this must be called when finished constructing the Controller
        self.refresh ()

    def changeModel (self, *ignore):
        key = self.entry.value
        try:
            (key, value)= key.split (':', 1)
            self.value[key]= value
            self.entry.value = key
        except ValueError, e:
            pass
        self.refresh()

    def refresh(self):
        self.label.text= str (self.value.get (self.entry.value, 'Not found'))
        self.daLabel.text = pformat(self.value)

class TestController(abstractTestControl):
    def setUp (self):
        self.value = dict(foo=1,
                          bar=2,
                          baz=3)

        super (TestController, self).setUp ()
        self.parent = self.win = cimarron.skin.Window(title='Test',
                                                      parent=self.app)
        self.widget= FooController (parent=self.win, value=self.value)

    def testModel (self):
        self.widget.entry.value = 'foo'
        self.widget.entry.onAction (self.widget)
        self.assertEqual(self.widget.label.text, '1')

    def testChangeModel(self):
        self.widget.entry.value = 'quux:5'
        self.widget.entry.onAction(self.widget)
        self.assertEqual(self.widget.label.text, '5',
                         'Label was not updated')
        self.assertEqual(self.widget.entry.value, 'quux',
                         'Entry was not updated')

    def testRefresh(self):
        self.value['foo'] = '7'
        self.widget.refresh()
        self.widget.entry.value = 'foo'
        self.widget.entry.onAction()
        self.assertEqual(self.widget.label.text, '7')

    def testSetValue(self):
        self.widget.entry.value = 'quux'
        self.widget.value = dict(quux='-13')
        self.assertEqual(self.widget.label.text, '-13')

class BarController (Controller):
    def __init__ (self, **kw):
        super (BarController, self).__init__ (**kw)
        v= cimarron.skin.VBox (parent=self)
        h= cimarron.skin.HBox (parent= v)
        self.prev= cimarron.skin.Button (parent= h, label='<<', value=-1)
        self.next= cimarron.skin.Button (parent= h, label='>>', value=1)
        self.index= 0

        def onFooAction(foo, *a):
            self.onAction(*a)
        self.foo= FooController (parent=v, value=self.value[self.index],
                                 onAction=onFooAction)

        def onOkAction(ok, *a):
            print 'here'
            self.onAction (self.foo.value)
        self.ok= cimarron.skin.Button (parent= v, label='Ok',
                                       onAction=onOkAction)

        def roll(button, *a):
            try:
                self.index+= button.value
                self.foo.value= self.value[self.index]
            except IndexError:
                self.index-= button.value

        self.prev.onAction= roll
        self.next.onAction= roll
        self.mainWidget = self.foo
        self.refresh ()

    def refresh (self):
        self.foo.refresh ()

class TestBarController (abstractTestControl):
    def setUp (self):
        self.value = (dict(foo=1,
                           bar=2,
                           baz=3), dict (a=1, b= 2, c= 3))
        super (TestBarController, self).setUp ()
        self.parent = self.win = cimarron.skin.Window(title='Test 2',
                                                      parent=self.app)
        def here (*a):
            print 'here!'
        self.widget= BarController (parent=self.win, value=self.value,
                                    onAction=here)


    def testRoll (self):
        self.widget.next.onAction()

class TestApp(unittest.TestCase):
    def setUp(self):
        cimarron.config()
        self.app = App()
        self.win1 = cimarron.skin.Window(parent=self.app)
        self.win2 = cimarron.skin.Window(parent=self.app)
        self.app.show()
    def testAppContinuesAfterWindowCloseIfMoreWindowsRemain(self):
        self.win1.hide()
        self.assert_(self.win2.visible)
    def testAppFinishesAfterLastWindowCloses(self):
        def cb(*a):
            self.win1.hide()
            self.win2.hide()
            self.dunnit = True
        self.app.schedule(100, cb)
        self.app.run()
        self.assert_(self.dunnit, 'got here!')
    
    def testScheduledEventsRun(self):
        def cb(*a):
            self.dunnit = True
            self.app.quit()
        self.app.schedule(100, cb)
        self.app.run()
        self.assert_(self.dunnit)
    def tearDown(self):
        self.app.hide()
        self.app.quit()
