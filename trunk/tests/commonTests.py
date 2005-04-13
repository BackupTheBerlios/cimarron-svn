import unittest
from papo.cimarron import skin, App

class abstractTestBasic(unittest.TestCase, object):
    def setUp(self):
        self.app = App()
        super (abstractTestBasic, self).setUp ()
    def testSkinArgv(self):
        self.assertEqual(skin.__name__, 'papo.cimarron.skins.gtk2')
#     def tearDown(self):
#         import gtk
#         while gtk.events_pending(): gtk.main_iteration()

class abstractTestDelegate(abstractTestBasic):
    def setUp(self):
        super(abstractTestDelegate, self).setUp()
        class delegate_forcedNo(object):
            def foo(self, *a):
                return -5
        self.delegate_forcedNo = delegate_forcedNo()
        class delegate_no(object):
            def foo(self, *a):
                return -1
        self.delegate_no = delegate_no()
        class delegate_unknown(object):
            def foo(self, *a):
                return 0
        self.delegate_unknown = delegate_unknown()
        class delegate_yes(object):
            def foo(self, *a):
                return 1
        self.delegate_yes = delegate_yes()
        class delegate_forcedYes(object):
            def foo(self, *a):
                return 5
        self.delegate_forcedYes = delegate_forcedYes()
        
    def testDelegate(self):
        self.assertEqual(self.widget.delegate('foo'), True)
    def testSingleDelegationFail(self):
        self.widget.delegates.append(self.delegate_forcedNo)
        self.assertEqual(self.widget.delegate('foo'), False)
    def testSingleDelegationReject(self):
        self.widget.delegates.append(self.delegate_no)
        self.assertEqual(self.widget.delegate('foo'), False)
    def testSingleDelegationPass(self):
        self.widget.delegates.append(self.delegate_forcedYes)
        self.assertEqual(self.widget.delegate('foo'), True)
    def testSingleDelegationAccept(self):
        self.widget.delegates.append(self.delegate_yes)
        self.assertEqual(self.widget.delegate('foo'), True)

from generated import abstractTestDelegateGenerated

class abstractTestWidget(abstractTestDelegateGenerated):
    def testParenting(self):
        self.assertEqual(self.widget.parent, self.parent)

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
        skin_name  = skin.__name__.split('.')[-1]
        if skin_name == 'gtk2':
            w = self.widget._widget
            try:
                w.clicked()
            except AttributeError:
                w.activate ()
        else:
            raise NotImplementedError, 'write skin-specific test, please, mastah!'
        self.assert_(self.widget in self.messages_recieved)

    def notify(self, origin):
        self.messages_recieved.append(origin)

if __name__ == '__main__':
    unittest.main()
