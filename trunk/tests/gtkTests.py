from commonTests import abstractTestWidget
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

class testGtkVisibility(abstractTestWidget):
    def testGtkShow(self):
        self.app.show()
        self.widget.hide()
        self.widget.show()
        self.assert_(self.widget._widget.window is not None and self.widget._widget.window.is_visible())

    def testGtkHide(self):
        self.app.show()
        self.widget.hide()
        self.assert_(self.widget._widget.window is None or not self.widget._widget.window.is_visible())

class TestGtkEntry(testGtkVisibility, TestEntry):
    def testSetValue (self):
        self.widget.value= 'this is a test'
        self.assertEqual (self.widget._widget.get_text(), self.widget.value)
    
class TestGtkWindow(testGtkVisibility, TestWindow):
    pass

class TestGtkLabel(testGtkVisibility, TestLabel):
    def testSetLabel(self):
        self.widget.text= 'This is a label'
        self.assertEqual (self.widget.text, self.widget._widget.get_text ())

class TestGtkButton(testGtkVisibility, TestButton):
    def testSetLabel (self):
        self.widget.label= "Don't click me"
        self.assertEqual(self.widget.label, self.widget._widget.get_label ())

class TestGtkBoxes(testGtkVisibility, TestBoxes):
    pass
