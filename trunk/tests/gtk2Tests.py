from unittest import TestCase
import pygtk
pygtk.require ('2.0')
import gtk
import gobject

from run import test_options

from papo import cimarron
from papo.cimarron.skins.common import Unknown

from commonTests import abstractTestWidget, abstractTestVisibility
from windowTests import TestWindow
from labelTests import TestLabel
from buttonTests import TestButton
from entryTests import TestEntry
from boxTests import TestBoxes
from notebookTests import TestNotebook


__all__ = ('TestGtkEntry',
           'TestGtkWindow',
           'TestGtkLabel',
           'TestGtkButton',
           'TestGtkEntry',
           'TestGtkBoxes',
           'TestGtkNotebook',
           )

class testGtkParenting (abstractTestWidget):
    def testGtkParent (self):
        self.assertEqual (self.widget._widget.parent, self.parent._widget)

    def testGtkChildInChildren (self):
        self.assert_ (self.widget._widget
                      in self.parent._widget.get_children ())

class testGtkVisibility(abstractTestVisibility):
    def testGtkShow(self):
        self.app.show()
        self.widget.hide()
        self.widget.show()
        self.assert_(self.widget._widget.window is not None
                     and self.widget._widget.window.is_visible())

    def testGtkHide(self):
        self.app.show()
        self.widget.hide()
        self.assert_(self.widget._widget.window is None
                     or not self.widget._widget.window.is_visible(),
                     "calling hide on the widget didn't actually hide it")

class testGtkFocusable(TestCase):
    def setUp (self):
        super (testGtkFocusable, self).setUp ()
        self.other= cimarron.skin.Entry (parent=self.parent)
        self.widget.delegates.append (self)

    if test_options.focus_events:
        def testOnFocusIn (self):
            import gtk

            self.app.show ()
            while gtk.events_pending():
                gtk.main_iteration ()
            self.passed = 0
            self.other._widget.grab_focus ()
            while not self.other._widget.is_focus():
                gtk.main_iteration()
            self.widget._widget.grab_focus ()
            while not self.widget._widget.is_focus():
                gtk.main_iteration ()
            while not self.passed is 'in':
                gtk.main_iteration ()
            self.assertEqual(self.passed, 'in')

        def testOnFocusOut (self):
            import gtk

            self.app.show ()
            while gtk.events_pending():
                gtk.main_iteration ()
            self.passed = 0
            self.widget._widget.grab_focus ()
            while not self.widget._widget.is_focus():
                gtk.main_iteration()
            while not self.passed is 'in':
                gtk.main_iteration ()
            self.other._widget.grab_focus ()
            while not self.other._widget.is_focus():
                gtk.main_iteration ()
            while not self.passed is 'out':
                gtk.main_iteration ()
            self.assertEqual(self.passed, 'out')

        def will_focus_in (self, widget):
            self.passed = 'in'
            return 0

        def will_focus_out(self, widget):
            self.passed = 'out'
            return 0

    def testFocus (self):
        self.other._widget.grab_focus ()

        self.app.show ()
        gobject.timeout_add (100, self.doTestFocus)
        gobject.timeout_add (500, gtk.main_quit)
        self.app.run ()
        self.assert_ (self.widget._widget.is_focus ())

    def doTestFocus (self, *ignore):
        self.widget.focus ()

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

class TestGtkButton(testGtkFocusable, testGtkParenting, TestButton):
    def testSetLabel (self):
        self.widget.label= "Don't click me"
        self.assertEqual(self.widget.label, self.widget._widget.get_label ())

class TestGtkBoxes(testGtkParenting, TestBoxes):
    pass

class TestGtkNotebook (testGtkParenting, TestNotebook):
    def testActivate (self):
        for i in xrange (10):
            other= cimarron.skin.Entry ()
            other.label= "label"+str (i)
            other.parent= self.widget
        self.app.show ()

        for i in xrange (10):
            self.widget.activate (i)
            while gtk.events_pending (): gtk.main_iteration ()
            self.assertEqual (i, self.widget._widget.get_current_page ())
            
        for i in xrange (10):
            self.widget.activate (self.widget._children[i])
            while gtk.events_pending (): gtk.main_iteration ()
            self.assertEqual (i, self.widget._widget.get_current_page ())

