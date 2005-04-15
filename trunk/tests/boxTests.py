import unittest
import sys
from cStringIO import StringIO

if '..' not in sys.path:
    sys.path.append('..')

from papo import cimarron
from commonTests import abstractTestContainer

__all__ = ('TestBoxes',
           )

class TestBoxes (abstractTestContainer):
    def setUp (self):
        super (TestBoxes, self).setUp ()
        self.parent= self.window= cimarron.skin.Window (parent=self.app)
        self.widget= self.vbox= cimarron.skin.VBox (parent=self.parent)

    def testVisual (self):
        d= cimarron.skin.Button (parent=self.widget, label='Looking good')
        self.assertEqual (d.parent, self.widget)
        self.other= cimarron.skin.HBox (parent= self.widget)

        b= cimarron.skin.Button (label='Looking so-so')
        b.parent= self.other
        # self.app.Button (parent= self.other, label='Looking so-so')
        cimarron.skin.Button (parent= self.other, label='Looking bad')

        # self.app.show ()
        # self.app.run ()

    def testReparenting1 (self):
        b= cimarron.skin.Button (parent= self.widget, label='reparented 1')
        def test():
            b.parent= self.widget

        self.assertRaises(ValueError, test)

    def testReparenting2 (self):
        b= cimarron.skin.Button (label='reparented 2')
        b.parent= None

    def testReparenting3 (self):
        b= cimarron.skin.Button (parent= self.widget, label='reparented 3')

        def test():
            b.parent = None
        self.assertRaises (NotImplementedError, test)


    def testReparenting4 (self):
        b= cimarron.skin.Button (label='reparented 4')
        b.parent= self.widget
        self.assertEqual (b.parent, self.widget)

    def testReparenting5 (self):
        b= cimarron.skin.Button (parent= self.widget, label='reparented 5')

        def test ():
            b.parent= self.window

        self.assertRaises (NotImplementedError, test)
