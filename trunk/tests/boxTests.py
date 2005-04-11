import unittest
import sys
from cStringIO import StringIO

if '..' not in sys.path:
    sys.path.append('..')

from papo import cimarron
from papo.cimarron import skin
from commonTests import abstractTestContainer

__all__ = ('TestBoxes',
           )

class TestBoxes (abstractTestContainer):
    def setUp (self):
        super (TestBoxes, self).setUp ()
        self.parent= self.window= skin.Window (parent=self.app)
        self.widget= self.vbox= skin.VBox (parent=self.parent)

    def testVisual (self):
        d= skin.Button (parent=self.widget, label='Looking good')
        self.assertEqual (d.parent, self.widget)
        self.other= skin.HBox (parent= self.widget)

        b= skin.Button (label='Looking so-so')
        b.parent= self.other
        # self.app.Button (parent= self.other, label='Looking so-so')
        skin.Button (parent= self.other, label='Looking bad')

        # self.app.show ()
        # self.app.run ()

    def testReparenting1 (self):
        b= skin.Button (parent= self.widget, label='reparented 1')
        def test():
            b.parent= self.widget

        self.assertRaises(ValueError, test)

    def testReparenting2 (self):
        b= skin.Button (label='reparented 2')
        b.parent= None

    def testReparenting3 (self):
        b= skin.Button (parent= self.widget, label='reparented 3')

        def test():
            b.parent = None
        self.assertRaises (NotImplementedError, test)


    def testReparenting4 (self):
        b= skin.Button (label='reparented 4')
        b.parent= self.widget
        self.assertEqual (b.parent, self.widget)

    def testReparenting5 (self):
        b= skin.Button (parent= self.widget, label='reparented 5')

        def test ():
            b.parent= self.window

        self.assertRaises (NotImplementedError, test)
