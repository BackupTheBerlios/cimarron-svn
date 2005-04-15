from unittest import TestCase

from papo.cimarron import skin

from commonTests import abstractTestWidget, abstractTestVisibility
from windowTests import TestWindow
from labelTests import TestLabel
from buttonTests import TestButton
from entryTests import TestEntry
from boxTests import TestBoxes


__all__ = ('TestGtkEntry',
           'TestGtkWindow',
           'TestGtkLabel',
           'TestGtkButton',
           'TestGtkEntry',
           'TestGtkBoxes',
           )

class testGtkParenting (abstractTestWidget):
    def testGtkParent (self):
        self.assertEqual (self.widget._widget.parent, self.parent._widget)

    def testGtkChildInChildren (self):
        self.assert_ (self.widget._widget in self.parent._widget.get_children ())

class testGtkVisibility(abstractTestVisibility):
    def testGtkShow(self):
        self.app.show()
        self.widget.hide()
        self.widget.show()
        self.assert_(self.widget._widget.window is not None and self.widget._widget.window.is_visible())

    def testGtkHide(self):
        self.app.show()
        self.widget.hide()
        self.assert_(self.widget._widget.window is None
                     or not self.widget._widget.window.is_visible(),
                     "calling hide on the widget didn't actually hide it")

class testGtkFocusable(TestCase):
    def testVisual (self):
        b1= skin.Button (
            parent= self.parent,
            label= 'this',
            onAction= self.focus1,
            )
        self.other= skin.Entry (parent=self.parent)
        b2= skin.Button (
            parent= self.parent,
            label= 'that',
            onAction= self.focus2,
            )
        print `self.parent`, `self.widget.parent`, `self.other.parent`, repr (list (self.parent.children))
        self.widget.onFocusIn= self.here

#         self.app.show ()
#         self.app.run ()

    def focus1 (self, *i):
        print 'focus1'
        self.widget._widget.grab_focus ()

    def focus2 (self, *i):
        print 'focus1'
        self.other._widget.grab_focus ()

    def here (self, *i):
        print 'here!'

    def testOnFocusIn (self):
        other= skin.Entry (parent=self.parent)
        self.widget.onFocusIn= self.focusOk
        other._widget.grab_focus ()
        self.widget._widget.grab_focus ()
        self.assert_ (self.passed)

    def focusOk (self):
        self.passed= True

class TestGtkEntry(testGtkFocusable, testGtkParenting, TestEntry):
    def testSetValue (self):
        self.widget.value= 'this is a test'
        self.assertEqual (self.widget._widget.get_text(), self.widget.value)

class TestGtkWindow(testGtkVisibility, TestWindow):
    pass

class TestGtkLabel(testGtkParenting, TestLabel):
    def testSetLabel(self):
        self.widget.text= 'This is a label'
        self.assertEqual (self.widget.text, self.widget._widget.get_text ())

class TestGtkButton(testGtkParenting, TestButton):
    def testSetLabel (self):
        self.widget.label= "Don't click me"
        self.assertEqual(self.widget.label, self.widget._widget.get_label ())

class TestGtkBoxes(testGtkParenting, TestBoxes):
    pass

