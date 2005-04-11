import unittest
from papo import cimarron

class abstractTestBasic(unittest.TestCase, object):
    def setUp(self):
        self.app = cimarron.App()
        super (abstractTestBasic, self).setUp ()
    def testSkinArgv(self):
        self.assertEqual(self.app.skin.__name__, 'papo.cimarron.skins.gtk2')
    def tearDown(self):
        import gtk
        while gtk.events_pending(): gtk.main_iteration()

class abstractTestWidget(abstractTestBasic):
    def testParenting(self):
        self.assertEqual(self.widget.parent, self.parent)

    def testSkin (self):
        self.assertEqual (self.widget.skin, self.app.skin)

class abstractTestContainer(abstractTestBasic):
    def testChilding(self):
        self.assert_(self.widget in self.parent.children)

class abstractTestControl(abstractTestWidget):
    def setUp(self):
        super(abstractTestControl, self).setUp()
        self.messages_recieved = []
    def setUpControl(self, value='123'):
        self.widget.value = value
        self.value = value

    def testValue(self):
        self.assertEqual (self.value, self.widget.value)

    def testOnAction (self):
        self.widget.onAction= self.notify
        self.widget._widget.activate ()
        self.assert_(self.widget in self.messages_recieved)

    def notify(self, origin):
        self.messages_recieved.append(origin)

if __name__ == '__main__':
    unittest.main()
