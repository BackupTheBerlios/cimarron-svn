import unittest
import sys

if '..' not in sys.path:
    sys.path.append('..')

from papo import cimarron

class abstractTestBasic(unittest.TestCase, object):
    def setUp(self):
        sys.argv[1:] = ['--skin=testable']
        self.app = cimarron.App()
    def testSkinArgv(self):
        self.assertEqual(self.app.skin.__name__, 'papo.cimarron.skins.testable')

class abstractTestWidget(abstractTestBasic):
    def testParenting(self):
        self.assertEqual(self.widget.parent, self.parent)

class abstractTestContainer(abstractTestBasic):
    def testChilding(self):
        self.assert_(self.widget in self.parent.children)

class abstractTestControl(abstractTestWidget):
    def setUpAction(self):
        def action(control):
            control.flag = True

        self.widget.action = action
        self.widget.value = '123'

    def testAction(self):
        self.widget.action()
        self.assertEqual(self.widget.flag, True)

    def testValue(self):
        self.assertEqual ('123', self.widget.value)
    
    

if __name__ == '__main__':
    unittest.main()
