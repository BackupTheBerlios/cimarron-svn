# -*- coding: utf-8 -*-
#
# Copyright 2003 Fundación Via Libre
#
# This file is part of PAPO.
#
# PAPO is free software; you can redistribute it and/or modify it under the
# terms of the GNU General Public License as published by the Free Software
# Foundation; either version 2 of the License, or (at your option) any later
# version.
#
# PAPO is distributed in the hope that it will be useful, but WITHOUT ANY
# WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
# FOR A PARTICULAR PURPOSE.  See the GNU General Public License for more
# details.
#
# You should have received a copy of the GNU General Public License along with
# PAPO; if not, write to the Free Software Foundation, Inc., 59 Temple Place,
# Suite 330, Boston, MA 02111-1307 USA

import unittest
from run import test_options
from papo import cimarron

class abstractTestBasic(unittest.TestCase, object):
    def setUp(self):
        cimarron.config()
        self.app = cimarron.skin.App()
        super (abstractTestBasic, self).setUp ()
    def testSkinArgv(self):
        self.assertEqual(cimarron.skin.__name__, 'papo.cimarron.skins.gtk2')
    def tearDown(self):
        self.app.hide()
        self.app.quit()

class abstractTestDelegate(abstractTestBasic):
    def setUp(self):
        super(abstractTestDelegate, self).setUp()
        class delegate_forcedNo(object):
            def foo(self, *a):
                return cimarron.skin.ForcedNo
        self.delegate_forcedNo = delegate_forcedNo()
        class delegate_no(object):
            def foo(self, *a):
                return cimarron.skin.No
        self.delegate_no = delegate_no()
        class delegate_unknown(object):
            def foo(self, *a):
                return cimarron.skin.Unknown
        self.delegate_unknown = delegate_unknown()
        class delegate_yes(object):
            def foo(self, *a):
                return cimarron.skin.Yes
        self.delegate_yes = delegate_yes()
        class delegate_forcedYes(object):
            def foo(self, *a):
                return cimarron.skin.ForcedYes
        self.delegate_forcedYes = delegate_forcedYes()
        class delegate_broken(object):
            def foo(*a):
                raise AttributeError
        self.delegate_broken = delegate_broken()
        
    def testDelegate(self):
        self.assertEqual(self.widget.delegate('foo'), True)
    def testDelegateArgs(self):
        self.assertEqual(self.widget.delegate('foo', self), True)
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
    def testBrokenDelegateRaisesException(self):
        self.widget.delegates.append(self.delegate_broken)
        self.assertRaises(AttributeError, lambda *a: self.widget.delegate('foo'))

if test_options.delegations:
    from generated import abstractTestDelegateGenerated
else:
    class abstractTestDelegateGenerated(abstractTestDelegate): pass

class abstractTestWidget(abstractTestDelegateGenerated):
    def testParenting(self):
        self.assertEqual(self.widget.parent, self.parent)

class abstractTestVisibility(unittest.TestCase):
    def testShow(self):
        self.app.show()
        self.widget.hide()
        self.widget.show()
        self.assertEqual(self.widget.visible, True)

    def testHide(self):
        self.app.show()
        self.widget.hide()
        self.assertEqual(self.widget.visible, False)

    def testUnableToHide(self):
        self.widget.delegates.append(self)
        self.app.show()
        self.assertEqual(self.widget.visible, True,
                         'widget visible before hiding')
        self.widget.hide()
        self.assertEqual(self.widget.visible, True,
                         'widget not visible after attempted hiding')
        self.widget.delegates.remove(self)

    def will_hide(self, target):
        return cimarron.skin.ForcedNo

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
        skin_name  = cimarron.skin.__name__.split('.')[-1]
        if skin_name == 'gtk2':
            w = self.widget
            try:
                while True:
                    w = w.mainWidget
            except AttributeError:
                pass
            w = w._widget
            try:
                c=w.clicked
            except AttributeError:
                c=w.activate
            c()
        else:
            raise NotImplementedError, \
                  'write skin-specific test, please, mastah!'
        self.assert_(self.widget in self.messages_recieved)

    def notify(self, origin):
        self.messages_recieved.append(origin)
