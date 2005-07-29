# -*- coding: utf-8 -*-
#
# Copyright 2005 Fundación Via Libre
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
from fvl import cimarron

from model.person import Person
from model.country import Country

class abstractTestBasic(unittest.TestCase, object):
    def setUp(self):
        self.app = cimarron.skin.Application()
        super (abstractTestBasic, self).setUp ()
    def testSkinArgv(self):
        self.assertEqual(cimarron.skin.__name__, 'fvl.cimarron.skins.gtk2')
    def testWeakestLiskov(self):
        """
        Test that we can actually create (instances of) subclasses of
        our widgets.
        """
        widgetClass = type(self.widget)
        subclass = type('Subclass', (widgetClass, ), {})
        subclass()
    def testWeakLiskov(self):
        """
        Test that we can create subclasses of our widgets, whose
        concrete widgets are themselves subclasses of the original.
        """
        oldClass = type(self.widget._concreteWidget)
        prefix = 'ConcreteSublassOf'
        concreteClass = type(prefix + oldClass.__name__,
                             (oldClass, ), {})
        class Subclass(type(self.widget)):
            def __init__(s, *a, **kw):
                s._concreteWidget = concreteClass()
                super(Subclass, s).__init__(*a, **kw)
        other = Subclass()
        self.assert_(type(other._concreteWidget).__name__.startswith(prefix))
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
        self.assertEqual(bool(self.widget.delegate('foo')), True)
    def testDelegateArgs(self):
        self.assertEqual(bool(self.widget.delegate('foo', self)), True)
    def testSingleDelegationFail(self):
        self.widget.delegates.append(self.delegate_forcedNo)
        self.assertEqual(bool(self.widget.delegate('foo')), False)
    def testSingleDelegationReject(self):
        self.widget.delegates.append(self.delegate_no)
        self.assertEqual(bool(self.widget.delegate('foo')), False)
    def testSingleDelegationPass(self):
        self.widget.delegates.append(self.delegate_forcedYes)
        self.assertEqual(bool(self.widget.delegate('foo')), True)
    def testSingleDelegationAccept(self):
        self.widget.delegates.append(self.delegate_yes)
        self.assertEqual(bool(self.widget.delegate('foo')), True)
    def testBrokenDelegateRaisesException(self):
        self.widget.delegates.append(self.delegate_broken)
        self.assertRaises(AttributeError,
                          lambda *a: self.widget.delegate('foo'))

if test_options.delegations:
    from generated import abstractTestDelegateGenerated
else:
    class abstractTestDelegateGenerated(abstractTestDelegate): pass

class abstractTestWidget(abstractTestDelegateGenerated):
    def testParenting(self):
        self.assertEqual(self.widget.parent, self.parent)
    def testWindowing(self):
        self.assertEqual(self.widget.window, self.window)

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
        self.widget.delegates.insert(0, self)
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
    def setUpControl(self, target=Country (name='Elbonia'), attr='name'):
        self.widget.attribute = self.attribute = attr
        self.target = target
        self.widget.newTarget(self.target)
        if attr is not None:
            self.value = getattr(target, attr)
        else:
            self.value = target

    def testValue(self):
        self.widget.value = self.value

        self.assertEqual (self.widget.value, self.value)

    def testValueFromNone (self):
        self.widget.newTarget (None)

        self.assert_(self.widget.value is None, repr(self.widget.value))

    def testValueIsTargetWhenNoAttr (self):
        self.widget.attribute= None
        self.widget.newTarget (self.target)
        self.assertEqual (self.widget.value, self.widget.target)

    def testValueWithAttribute (self):
        self.widget.attribute= self.attribute
        self.widget.newTarget (self.target)
        
        self.assertEqual (self.widget.value, self.value)

    def testWriteValueAttribute (self):
        self.testValueWithAttribute ()
        
        self.widget.value = None
        self.widget.value = self.value

    def testOnAction (self):
        self.widget.onAction= self.notify
        skin_name  = cimarron.skin.__name__.split('.')[-1]
        if skin_name == 'gtk2':
            w = self.widget
            try:
                while True:
                    assert w!=w.mainWidget, w
                    w = w.mainWidget
            except AttributeError:
                pass
            w = w._activableWidget
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

    def testMainWidgetNotItself (self):
        try:
            self.assertNotEqual (self.widget.mainWidget, self.widget)
        except AttributeError:
            # the widget has no mainWidget
            pass

    def testControlKnowsDirtyness(self):
        # something that might actually fail (instead of passing xor
        # erroring) would be cool
        self.widget.dirty()

    def testForBugA(self):
        self.widget.attribute = 'foo'
        self.widget.newTarget(None)
        # this is sneaky: we use a list so that multivalued Controls
        # (that using IModel) skip the value, but single-valued
        # Controls will try to getattr on the list and fail.  Of
        # course, then we fix the bug so they *don't* try to do that
        # :)
        self.widget.commitValue([])
        self.widget.refresh()

    def testForBugB(self):
        self.widget.attribute = 'foo'
        self.widget.newTarget(None)
        # sneaky (see testForBugA)
        self.widget.commitValue([])
        self.widget.commitValue([])
