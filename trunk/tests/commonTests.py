import unittest
import sys

if '..' not in sys.path:
    sys.path.append('..')

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

class abstractTestContainer(abstractTestBasic):
    def testChilding(self):
        self.assert_(self.widget in self.parent.children)

class abstractTestObservable(unittest.TestCase, object):
    def setUp(self):
        super(abstractTestObservable, self).setUp()
        self.messages_recieved = []
        
    def testAddObserver(self):
        self.widget.observers.append(self)

    def testObserverNotified(self):
        self.testAddObserver ()
        self.widget.announce('event')
        self.assert_('event' in self.messages_recieved)

    def notify(self, message):
        self.messages_recieved.append(message)

class abstractTestControl(abstractTestWidget, abstractTestObservable):
    def setUpControl(self):
        self.widget.value = '123'
    def testValue(self):
        self.assertEqual ('123', self.widget.value)
    
    

if __name__ == '__main__':
    unittest.main()
