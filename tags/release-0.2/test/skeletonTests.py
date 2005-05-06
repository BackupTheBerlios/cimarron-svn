import unittest

import papo.cimarron
papo.cimarron.config()
from papo.cimarron import skin

__all__ = ('TestSkeleton',)

class TestSkeleton(unittest.TestCase):
    def setUp(self):
        self.app = skin.App()
        self.window = skin.Window(parent=self.app)
        self.vbox = skin.VBox(parent=self.window)
        self.button = skin.Button(parent=self.vbox,
                                  label='click my clicker',
                                  value=5)
        self.entry = skin.Entry(parent=self.vbox)

    def testLeafSkeleton(self):
        skel = self.button.skeleton()
        self.assertEqual(skel.serialize(), 
                         '<Button value="5" label="\'click my clicker\'"/>')

    def testInteriorNodeSkeleton(self):
        skel = self.vbox.skeleton()
        self.assertEqual(skel.serialize(),
                         '<VBox>'
                           '<Button value="5" label="\'click my clicker\'"/>'
                           '<Entry value="\'\'"/>'
                         '</VBox>')

    def testWindowSkeleton(self):
        skel = self.window.skeleton()
        self.assertEqual(skel.serialize(),
                         '<Window>'
                           '<VBox>'
                             '<Button value="5" label="\'click my clicker\'"/>'
                             '<Entry value="\'\'"/>'
                           '</VBox>'
                         '</Window>')

    def testAppSkeleton(self):
        skel = self.app.skeleton()
        self.assertEqual(skel.serialize(),
                         '<App value="\'\'">'
                           '<Window>'
                             '<VBox>'
                               '<Button value="5" label="\'click my clicker\'"/>'
                               '<Entry value="\'\'"/>'
                             '</VBox>'
                           '</Window>'
                         '</App>')

    def testRoundTrip(self):
        sk = self.app.skeleton()
        app = papo.cimarron.fromXmlObj(sk.doc)
        self.assertEqual(app.skeleton().serialize(), sk.serialize())
