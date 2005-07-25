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
from pprint import pformat

from fvl import cimarron
from fvl.cimarron.controllers import Controller, WindowController, CRUDController, Editor, DelayedTraversal
from model.person import Person, Address
from model.country import Country, State

from testCommon import abstractTestControl, abstractTestVisibility

__all__ = ('TestFooController',
           'TestBarController',
           'TestApp',
           'TestWindowController',
           )

def visualTest():
    app = cimarron.skin.Application()
    win = cimarron.skin.Window(parent=app)
    foo = FooController(parent=win, target=dict(foo=1,bar=2,baz=3))
    app.show()
    app.run()

class TestController (abstractTestControl):
    def testFromXmlNonexistantFile(self):
        self.assertRaises(OSError, self.widget.fromXmlFile, 'xyzzy')

    def testImport (self):
        other= CRUDController.fromXmlFile ('test/import.xml')
        self.assertEqual (other.idDict.has_key ('testButton'), True)
        self.assert_ (other.idDict.has_key ('TestCheckbox'), True)

    def connection (self):
        self.connected= True

    def testConnectWithPath (self):
        self.widget.idDict= {'master': self.widget}
        self.widget.attrToConnect= 'master.connection'
        self.widget.connection= self.connection
        
        # test 1: the proper type
        self.widget._connect ({self.widget: ['attrToConnect']})
        self.assertEqual (type (self.widget.attrToConnect), DelayedTraversal)
        # test 2: the call works
        self.widget.attrToConnect ()
        self.assert_ (self.connected)

    def testConnectWithoutPath (self):
        self.widget.idDict= {'Connection': Connection}
        self.widget.attrToConnect= 'Connection'
        self.widget.connection= self.connection
        
        # test 1: the proper type
        self.widget._connect ({self.widget: ['attrToConnect']})
        self.assertEqual (self.widget.attrToConnect, Connection)
        # test 2: the call works
        obj= self.widget.attrToConnect ()
        self.assertEqual (type (obj), Connection)


class FooController(Controller):
    def __init__(self, target=None, **kw):
        super (FooController, self).__init__ (**kw)
        self.box= cimarron.skin.VBox (parent=self)
        h= cimarron.skin.HBox (parent=self.box)
        self.entry= cimarron.skin.Entry (parent=h)
        self.label= cimarron.skin.Label (parent=h, text='Nothing yet')
        self.button= cimarron.skin.Button (parent=self.box, label='Press me')
        self.daLabel= cimarron.skin.Label (parent=self.box)

        self.mainWidget = self.button
        self.newTarget(target)

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
        """
        Tries to add a new item to the target by splitting
        entry.value by ':'. in either case, call refresh().
        """
        key = self.entry.value
        try:
            (key, value)= key.split (':', 1)
            self.target[key]= value
            self.entry.value = key
            self.value= value
        except ValueError, e:
            pass
        self.refresh()

    def refresh(self):
        """
        Put the Controller's value in the labels.
        """
        super(FooController, self).refresh()
        if self.target is not None:
            self.label.text= str (self.target.get (self.entry.value, 'Not found'))
        else:
            self.label.text= ''
        self.daLabel.text = pformat(self.value)

class Connection (object):
    pass

class TestFooController(TestController):
    def setUp (self):
        super (TestController, self).setUp ()
        self.parent = self.window = cimarron.skin.Window(title='Test',
                                                      parent=self.app)
        self.widget= FooController (parent=self.window)
        self.setUpControl (dict(foo=1, bar=2, baz=3), None)
        
    def testModel (self):
        """
        Put a key in the entry, fire the action
        and test for the label contents.
        """
        self.widget.entry.value = 'foo'
        self.widget.entry.onAction (self.widget)
        self.assertEqual(self.widget.label.text, '1')

    def testChangeModel(self):
        """
        Put a new key:value pair.
        """
        self.widget.entry.value = 'quux:5'
        self.widget.entry.onAction(self.widget)
        self.assertEqual(self.widget.label.text, '5',
                         'Label was not updated')
        self.assertEqual(self.widget.entry.value, 'quux',
                         'Entry was not updated')

    def testRefresh(self):
        self.target['foo'] = '7'
        self.widget.refresh()
        self.widget.entry.value = 'foo'
        self.widget.entry.onAction()
        self.assertEqual(self.widget.label.text, '7')

    def testSetValue(self):
        """
        This assumes that setting the value re-fires refresh()
        """
        self.widget.entry.value = 'quux'
        self.widget.newTarget (dict(quux='-13'))
        self.assertEqual(self.widget.label.text, '-13')
    

class BarController (Controller):
    def __init__ (self, data=None, **kw):
        super (BarController, self).__init__ (**kw)
        v= cimarron.skin.VBox (parent=self)
        h= cimarron.skin.HBox (parent= v)
        self.prev= cimarron.skin.Button (parent= h, label='<<', value=-1)
        self.next= cimarron.skin.Button (parent= h, label='>>', value=1)
        self.index= 0
        self.data= data

        def onFooAction(foo, *a):
            self.onAction(*a)
        self.foo= FooController (parent=v, target=self.data[self.index],
                                 onAction=onFooAction)

        def onOkAction(ok, *a):
            print 'here'
            self.onAction (self.foo.value)
        self.ok= cimarron.skin.Button (parent= v, label='Ok',
                                       onAction=onOkAction)

        def roll(button, *a):
            try:
                self.index+= button.value
                self.foo.value= self.value
            except IndexError:
                self.index-= button.value

        self.prev.onAction= roll
        self.next.onAction= roll
        self.mainWidget = self.foo
        self.refresh ()

#     def _get_value (self):
#         try:
#             return self.data[self.index]
#         except:
#             return None
#     def _set_value (self, value):
#         try:
#             self.index= self.data.index (value)
#         except:
#             self.index= None
#     value= property (_get_value, _set_value)

    def refresh (self):
        super(BarController, self).refresh()
        self.foo.refresh ()

class FooList(list):
    def getattr(self, attr):
        return self[attr]

class TestBarController(TestController):
    def setUp(self):
        self.list= [dict(foo=1, bar=2, baz=3),
            dict(a=1, b= 2, c=3),
            ]
        self.target = FooList(self.list)
        self.attribute = 0
        self.value = self.target.getattr(self.attribute)
        super(TestBarController, self).setUp()
        self.parent = self.window = cimarron.skin.Window(title='Test 2',
                                                      parent=self.app)
        def here (*a):
            print 'here!'
        self.widget= BarController (parent=self.window, data=self.list,
                                    attribute=self.attribute, onAction=here)
        # self.value= self.list[0]
        self.widget.refresh()

    def testRoll (self):
        self.widget.next.onAction()

class TestApp(unittest.TestCase):
    def setUp(self):
        self.app = cimarron.skin.Application()
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

    def testNoWindow (self):
        # should test that running w/ no shown win it should just quit.
        pass
    

class TestWindowController (abstractTestVisibility):
    def setUp (self):
        super (TestWindowController, self).setUp ()
        self.app = cimarron.skin.Application()
        self.window= self.widget= WindowController (parent= self.app)

    def testVisible (self):
        self.widget.show ()
        self.assertEqual (self.widget.visible, self.widget.win.visible)
        self.widget.hide ()
        self.assertEqual (self.widget.visible, self.widget.win.visible)

    def testWindowCloseGetsProperlyDelegated (self):
        # this way abstractTestVisibility.will_hide won't get overrided
        # unless needed
        self.will_hide= self.will_hide_2
        self.widget.delegates.insert (0, self)
        self.widget.show ()
        self.widget.hide ()
        self.assertEqual (self.will_hide_passed, True)

    def will_hide_2 (self, *ignore):
        self.will_hide_passed= True
