#!/usr/bin/env python
import unittest
import cimarron
import sys
from Generic import Exceptions

def mk_del(meth, ans=None):
    d = {'f': cimarron.Failed,
         'r': cimarron.Reject,
         'u': cimarron.Unknown,
         'a': cimarron.Accept,
         'd': cimarron.Done}
    class c: pass
    if d.has_key(ans):
        setattr(c, meth, lambda *a: d[ans])
    return c()

class ConfigTest(unittest.TestCase):
    def testConfigBad(self):
        self.assertRaises(Exceptions.ConfigError, self.obj.getConfigAsString, '++BAD+KEY++')
    def testString(self):
        self.assertEqual(self.obj.getConfigAsString('test_string'), 'hello world!')
    def testStringMultiline(self):
        self.assertEqual(self.obj.getConfigAsString('test_string_multiline'), 'hello\nworld!')
    def testList(self):
        self.assertEqual(self.obj.getConfigAsList('test_list'), ['hello', 'world!'])
    def testListMultiline(self):
        self.assertEqual(self.obj.getConfigAsList('test_list_multiline'), ['hello', 'world!'])
    def testFloatGood(self):
        self.assertEqual(self.obj.getConfigAsFloat('test_float_good'), 3.14159)
    def testFloatBad(self):
        self.assertRaises(Exceptions.ConfigError, self.obj.getConfigAsFloat, 'test_float_bad')
    def testNumGood(self):
        self.assertEqual(self.obj.getConfigAsNum('test_num_good'), 3)
    def testNumBad(self):
        self.assertRaises(Exceptions.ConfigError, self.obj.getConfigAsNum, 'test_num_bad')
    def testBoolTrue1(self):
        self.assert_(self.obj.getConfigAsBoolean('test_bool_true_1') is True)
    def testBoolTrue2(self):
        self.assert_(self.obj.getConfigAsBoolean('test_bool_true_2') is True)
    def testBoolTrue3(self):
        self.assert_(self.obj.getConfigAsBoolean('test_bool_true_3') is True)
    def testBoolTrue4(self):
        self.assert_(self.obj.getConfigAsBoolean('test_bool_true_4') is True)
    def testBoolFalse1(self):
        self.assert_(self.obj.getConfigAsBoolean('test_bool_false_1') is False)
    def testBoolFalse2(self):
        self.assert_(self.obj.getConfigAsBoolean('test_bool_false_2') is False)
    def testBoolFalse3(self):
        self.assert_(self.obj.getConfigAsBoolean('test_bool_false_3') is False)
    def testBoolFalse4(self):
        self.assert_(self.obj.getConfigAsBoolean('test_bool_false_4') is False)
        
class ResponderTest(ConfigTest):
    def testParentGetNone(self):
        self.assert_(self.obj.getParent() is None)
    def testParentSet(self):
        self.obj.setParent('foo')
        self.assertEqual(self.obj.getParent(), 'foo')
    def testParentDoubleSet(self):
        """
        we don't consider parenting a parented responder an error, but
        c.f. View
        """
        pass
    def testParentReset(self):
        self.obj.setParent('foo')
        self.obj.setParent(None)
        self.assert_(self.obj.getParent() is None)
    def testAddDelegation(self):
        self.assert_(self.obj.addDelegation(mk_del('u')) is None)
    def testRemoveDelegationFail(self):
        self.assertRaises(ValueError, self.obj.removeDelegation, 'no delegation')
    def testRemoveDelegation(self):
        d = mk_del('foo', 'u')
        self.obj.addDelegation(d)
        self.assert_(self.obj.removeDelegation(d) is None)
    def testDelegateEmptyDefault(self):
        """
        by default, delegates accept stuff
        """
        self.assert_(self.obj.delegate('will_test_empty_default') is True)
    def testDelegateEmptyTrue(self):
        """
        you can specify the default behaviour explicitely
        """
        self.assert_(self.obj.delegate('will_test_empty_true', null=True) is True)
    def testDelegateEmptyFalse(self):
        """
        And this is fail-by-default
        """
        self.assert_(self.obj.delegate('will_test_empty_false', null=False) is False)
    def testDelegateReturningUnknownDefault(self):
        """
        delegates returning Unknown are ignored, so all Unknown is the
        same as empty
        """
        self.obj.addDelegation(mk_del('will_test', 'u'))
        self.assert_(self.obj.delegate('will_test') is True)
    def testDelegateReturningUnknownTrue(self):
        self.obj.addDelegation(mk_del('will_test', 'u'))
        self.assert_(self.obj.delegate('will_test', unknown=True) is True)
    def testDelegateReturningUnknownFalse(self):
        self.obj.addDelegation(mk_del('will_test', 'u'))
        self.assert_(self.obj.delegate('will_test', unknown=False) is False)

    def testDelegateUnknownDefault(self):
        """
        delegates lacking a method are treated as returning Unknown
        """
        self.obj.addDelegation(mk_del('will_test'))
        self.assert_(self.obj.delegate('will_test') is True)
    def testDelegateUnknownTrue(self):
        self.obj.addDelegation(mk_del('will_test'))
        self.assert_(self.obj.delegate('will_test', unknown=True) is True)
    def testDelegateUnknownFalse(self):
        self.obj.addDelegation(mk_del('will_test'))
        self.assert_(self.obj.delegate('will_test', unknown=False) is False)


    def testDelegateReject(self):
        """
        all Reject is don't
        """
        self.obj.addDelegation(mk_del('will_test', 'r'))
        self.assert_(self.obj.delegate('will_test') is False)
    def testDelegateFailed(self):
        """
        ...as is Fail
        """
        self.obj.addDelegation(mk_del('will_test', 'f'))
        self.assert_(self.obj.delegate('will_test') is False)
    def testDelegateAccept(self):
        """
        all Accept is do
        """
        self.obj.addDelegation(mk_del('will_test', 'a'))
        self.assert_(self.obj.delegate('will_test') is True)
    def testDelegateDone(self):
        """
        ...as is Done
        """
        self.obj.addDelegation(mk_del('will_test', 'd'))
        self.assert_(self.obj.delegate('will_test') is True)
    def testDelegateRA(self):
        """
        Default composition is 'or', so (reject, accept) is go ahead
        """
        self.obj.addDelegation(mk_del('will_test', 'r'))
        self.obj.addDelegation(mk_del('will_test', 'a'))
        self.assert_(self.obj.delegate('will_test') is True)
    def testDelegateAR(self):
        """
        ...as is (accept, reject)
        """
        self.obj.addDelegation(mk_del('will_test', 'a'))
        self.obj.addDelegation(mk_del('will_test', 'r'))
        self.assert_(self.obj.delegate('will_test') is True)
    def testDelegateRU(self):
        """
        (reject, unknown) is the same as (reject)
        """
        self.obj.addDelegation(mk_del('will_test', 'r'))
        self.obj.addDelegation(mk_del('will_test', 'u'))
        self.assert_(self.obj.delegate('will_test') is False)
    def testDelegateUR(self):
        """
        ...as is (unknwon, reject)
        """
        self.obj.addDelegation(mk_del('will_test', 'u'))
        self.obj.addDelegation(mk_del('will_test', 'r'))
        self.assert_(self.obj.delegate('will_test') is False)
    def testDelegateRD(self):
        """
        (reject, done) is go ahead
        """
        self.obj.addDelegation(mk_del('will_test', 'r'))
        self.obj.addDelegation(mk_del('will_test', 'd'))
        self.assert_(self.obj.delegate('will_test') is True)
    def testDelegateAF(self):
        """
        ...while (accept, failed) is don't
        """
        self.obj.addDelegation(mk_del('will_test', 'a'))
        self.obj.addDelegation(mk_del('will_test', 'f'))
        self.assert_(self.obj.delegate('will_test') is False)
    def testDelegateFD(self):
        """
        (failed, done) is don't
        """
        self.obj.addDelegation(mk_del('will_test', 'f'))
        self.obj.addDelegation(mk_del('will_test', 'd'))
        self.assert_(self.obj.delegate('will_test') is False)
    def testDelegateDF(self):
        """
        (done, failed) is do
        """
        self.obj.addDelegation(mk_del('will_test', 'd'))
        self.obj.addDelegation(mk_del('will_test', 'f'))
        self.assert_(self.obj.delegate('will_test') is True)
        
class CompositeTest(unittest.TestCase):
    def testAddChild(self):
        self.obj.addChild(self.obj2)
    def testAddChildTwice(self):
        self.obj.addChild(self.obj2)
        self.obj.addChild(self.obj2)
    def testGetChildrenEmpty(self):
        self.assertEqual(self.obj.getChildren(), [])
    def testGetChildrenSome(self):
        self.obj.addChild(self.obj2)
        self.assertEqual(self.obj.getChildren(), [self.obj2])
    def testRemoveChild1(self):
        self.obj.addChild(self.obj2)
        self.obj.removeChild(self.obj2)
        self.assertEqual(self.obj.getChildren(), [])
    def testRemoveChild2(self):
        self.obj.addChild(self.obj2)
        self.obj.removeChild(self.obj2)
        self.obj.addChild(self.obj2)
        self.assertEqual(self.obj.getChildren(), [self.obj2])
    def testRemoveChildFail(self):
        self.assertRaises(ValueError, self.obj.removeChild, self.obj2)

class CompositeResponderTest(ResponderTest, CompositeTest):
    def testAddChildTwice(self):
        self.obj.addChild(self.obj2)
        self.assertRaises(Exceptions.CompositionError, self.obj.addChild, self.obj2)

    def testAddChildDelegateFail(self):
        self.obj.addDelegation(mk_del('will_add_child', 'f'))
        self.assert_(self.obj.addChild(self.obj2) is False)
        self.assertEqual(self.obj.getChildren(), [])

    def testAddChildDelegateSucceed(self):
        self.obj.addDelegation(mk_del('will_add_child', 'd'))
        self.assert_(self.obj.addChild(self.obj2) is True)
        self.assertEqual(self.obj.getChildren(), [self.obj2])

    def testRemoveChildDelegateFail(self):
        self.obj.addChild(self.obj2)
        self.obj.addDelegation(mk_del('will_remove_child', 'f'))
        self.assert_(self.obj.removeChild(self.obj2) is False)
        self.assertEqual(self.obj.getChildren(), [self.obj2])
    def testRemoveChildDelegateSucceed(self):
        self.obj.addChild(self.obj2)
        self.obj.addDelegation(mk_del('will_remove_child', 'd'))
        self.assert_(self.obj.removeChild(self.obj2) is True)
        self.assertEqual(self.obj.getChildren(), [])
        
class ApplicationTest(CompositeResponderTest):
    def setUp(self):
        self.ui = cimarron.getEngine()
        self.obj2 = self.obj = self.ui.Application()

    def testAddChildTwice(self):
        return CompositeTest.testAddChildTwice(self)

class ViewTest(ResponderTest):
    def setUp(self):
        self.ui = cimarron.getEngine()
        self.app = self.ui.Application()
        self.win = self.ui.Window(parent=self.app)
        self.box = self.ui.HBox(parent=self.win)
    def testSetName(self):
        self.obj.setName('foo')
    def testGetName(self):
        self.assert_(self.obj.getName() is None)
    def testInvarName(self):
        name = 'foo'
        self.obj.setName(name)
        self.assert_(self.obj.getName() is name)
    def testParentSet(self):
        self.box.removeChild(self.obj)
        super(ViewTest, self).testParentSet()
    def testParentGetNone(self):
        self.box.removeChild(self.obj)
        super(ViewTest, self).testParentGetNone()
    def testParentReset(self):
        self.box.removeChild(self.obj)
        super(ViewTest, self).testParentReset()
    def testParentDoubleSet(self):
        self.assertRaises(Exceptions.ViewParentingError, self.obj.setParent, self.box)
    def testGetWindow(self):
        self.assert_(self.obj.getWindow() is self.win)
    def testPushStatus(self):
        self.assert_(self.obj.pushStatus('foo') is 1)
    def testPopStatus(self):
        self.obj.pushStatus('foo')
        self.assert_(self.obj.popStatus() is True)
    def testPopStatusEmpty(self):
        self.assertRaises(Exceptions.WindowError, self.obj.popStatus)
    def testRemoveStatus1(self):
        n = self.obj.pushStatus('foo')
        self.assert_(self.obj.removeStatus(n) is True)
    def testRemoveStatus2(self):
        n = self.obj.pushStatus('foo')
        self.obj.pushStatus('bar')
        self.obj.pushStatus('baz')
        self.assert_(self.obj.removeStatus(n) is True)
    def testRemoveStatusEmpty(self):
        self.assertRaises(Exceptions.WindowError, self.obj.removeStatus, 1)
    def testFocus(self):
        self.assert_(self.obj.focus() is True)
    def testFocusDelegateF(self):
        self.obj.addDelegation(mk_del('will_focus', 'f'))
        self.assert_(self.obj.focus() is False)
    def testFocusDelegateD(self):
        self.obj.addDelegation(mk_del('will_focus', 'd'))
        self.assert_(self.obj.focus() is True)
    def testHide(self):
        self.assert_(self.obj.hide() is True)
    def testHideDelegateF(self):
        self.obj.addDelegation(mk_del('will_hide', 'f'))
        self.assert_(self.obj.hide() is False)
    def testHideDelegateD(self):
        self.obj.addDelegation(mk_del('will_hide', 'd'))
        self.assert_(self.obj.hide() is True)
    def testShow(self):
        self.assert_(self.obj.show() is True)
    def testShowDelegateF(self):
        self.obj.addDelegation(mk_del('will_show', 'f'))
        self.assert_(self.obj.show() is False)
    def testShowDelegateD(self):
        self.obj.addDelegation(mk_del('will_show', 'd'))
        self.assert_(self.obj.show() is True)
    def testDisable(self):
        self.assert_(self.obj.disable() is True)
    def testDisableDelegateF(self):
        self.obj.addDelegation(mk_del('will_disable', 'f'))
        self.assert_(self.obj.disable() is False)
    def testDisableDelegateD(self):
        self.obj.addDelegation(mk_del('will_disable', 'd'))
        self.assert_(self.obj.disable() is True)
    def testEnable(self):
        self.assert_(self.obj.enable() is True)
    def testEnableDelegateF(self):
        self.obj.addDelegation(mk_del('will_enable', 'f'))
        self.assert_(self.obj.enable() is False)
    def testEnableDelegateD(self):
        self.obj.addDelegation(mk_del('will_enable', 'd'))
        self.assert_(self.obj.enable() is True)
    def testSetTip(self):
        self.assert_(self.obj.setTip('foo') is True)
    def testSetTipFail(self):
        self.assertRaises(Exceptions.ViewError, self.obj.setTip, 0)
    def testSetTipDelegateF(self):
        self.obj.addDelegation(mk_del('will_set_tip', 'f'))
        self.assert_(self.obj.setTip('foo') is False)
    def testSetTipDelegateD(self):
        self.obj.addDelegation(mk_del('will_set_tip', 'd'))
        self.assert_(self.obj.setTip('foo') is True)
    def testBusy(self):
        self.assert_(self.obj.busy() is True)
    def testBusyDelegateF(self):
        self.obj.addDelegation(mk_del('will_busy', 'f'))
        self.assert_(self.obj.busy() is False)
    def testBusyDelegateD(self):
        self.obj.addDelegation(mk_del('will_busy', 'd'))
        self.assert_(self.obj.busy() is True)
    def testIdle(self):
        self.assert_(self.obj.idle() is True)
    def testIdleDelegateF(self):
        self.obj.addDelegation(mk_del('will_idle', 'f'))
        self.assert_(self.obj.idle() is False)
    def testIdleDelegateD(self):
        self.obj.addDelegation(mk_del('will_idle', 'd'))
        self.assert_(self.obj.idle() is True)
    def testSetSizeRequest(self):
        self.assert_(self.obj.setSizeRequest(100, 100) is True)
    def testSetSizeRequestTuple(self):
        self.assert_(self.obj.setSizeRequest((100, 100)) is True)
    def testSetSizeRequestDelegateF(self):
        self.obj.addDelegation(mk_del('will_resize', 'f'))
        self.assert_(self.obj.setSizeRequest(100, 100) is False)
    def testSetSizeRequestDelegateD(self):
        self.obj.addDelegation(mk_del('will_resize', 'd'))
        self.assert_(self.obj.setSizeRequest(100, 100) is True)
    def testGetSizeRequest(self):
        self.obj.setSizeRequest(100, 100)
        self.assertEqual(self.obj.getSizeRequest(), (100, 100))
        
class MiscTest(ViewTest):
    def testSetAlign(self):
        self.assert_(self.obj.setAlign(0.5, 0.5) is True)
    def testSetAlignTuple(self):
        self.assert_(self.obj.setAlign((0.5, 0.5)) is True)
    def testSetAlignFail(self):
        self.assertRaises(Exceptions.MiscError,
                          self.obj.setAlign,
                          'x', 'y')
    def testSetAlignDelegateF(self):
        self.obj.addDelegation(mk_del('will_align', 'f'))
        self.assert_(self.obj.setAlign(0.5, 0.5) is False)
    def testSetAlignDelegateD(self):
        self.obj.addDelegation(mk_del('will_align', 'd'))
        self.assert_(self.obj.setAlign(0.5, 0.5) is True)
    def testGetAlign(self):
        self.obj.setAlign(0.5, 0.5)
        self.assertEqual(self.obj.getAlign(), (0.5, 0.5))
    def testSetPadding(self):
        self.assert_(self.obj.setPadding(15, 15) is True)
    def testSetPaddingTuple(self):
        self.assert_(self.obj.setPadding((15, 15)) is True)
    def testSetPaddingFail(self):
        self.assertRaises(Exceptions.MiscError,
                          self.obj.setPadding,
                          'x', 'y')
    def testSetPaddingDelegateF(self):
        self.obj.addDelegation(mk_del('will_pad', 'f'))
        self.assert_(self.obj.setPadding(15, 15) is False)
    def testSetPaddingDelegateD(self):
        self.obj.addDelegation(mk_del('will_pad', 'd'))
        self.assert_(self.obj.setPadding(15, 15) is True)
    def testGetPadding(self):
        self.obj.setPadding(15, 15)
        self.assertEqual(self.obj.getPadding(), (15, 15))
    

class LabelTest(MiscTest):
    def setUp(self):
        super(LabelTest, self).setUp()
        self.obj = self.ui.Label(parent=self.box)
    def testSetLabel(self):
        self.assert_(self.obj.setLabel('foo') is True)
    def testSetLabelFail(self):
        self.assertRaises(Exceptions.LabelError,
                          self.obj.setLabel, '\xe1')
    def testSetLabelDelegateF(self):
        self.obj.addDelegation(mk_del('will_set_label', 'f'))
        self.assert_(self.obj.setLabel('foo') is False)
    def testSetLabelDelegateD(self):
        self.obj.addDelegation(mk_del('will_set_label', 'd'))
        self.assert_(self.obj.setLabel('foo') is True)
    def testGetLabel(self):
        self.obj.setLabel('foo')
        self.assertEqual(self.obj.getLabel(), 'foo')
    def testSetJustify(self):
        self.assert_(self.obj.setJustify('left') is True)
    def testSetJustifyFail(self):
        self.assertRaises(Exceptions.LabelError,
                          self.obj.setJustify, 'x')
    def testSetJustifyDelegateF(self):
        self.obj.addDelegation(mk_del('will_justify', 'f'))
        self.assert_(self.obj.setJustify('left') is False)
    def testSetJustifyDelegateD(self):
        self.obj.addDelegation(mk_del('will_justify', 'd'))
        self.assert_(self.obj.setJustify('left') is True)
    def testGetJustify(self):
        self.obj.setJustify('left')
        self.assertEqual(self.obj.getJustify(), 'left')

    def testSetMnemonicWidget(self):
        self.assert_(self.obj.setMnemonicWidget(self.box) is True)
    def testSetMnemonicWidgetFail(self):
        self.assertRaises(Exceptions.LabelError,
                          self.obj.setMnemonicWidget, 'foo')
    def testSetMnemonicWidgetDelegateF(self):
        self.obj.addDelegation(mk_del('will_set_mnemonic_widget', 'f'))
        self.assert_(self.obj.setMnemonicWidget(self.box) is False)
    def testSetMnemonicWidgetDelegateD(self):
        self.obj.addDelegation(mk_del('will_set_mnemonic_widget', 'd'))
        self.assert_(self.obj.setMnemonicWidget(self.box) is True)
    def testGetMnemonicWidget(self):
        self.obj.setMnemonicWidget(self.box)
        self.assertEqual(self.obj.getMnemonicWidget(), self.box)

    def testSetUseMarkup(self):
        self.assert_(self.obj.setUseMarkup(True) is True)
        self.assert_(self.obj.setUseMarkup(False) is True)
    def testSetUseMarkupFail(self):
        self.assertRaises(Exceptions.LabelError,
                          self.obj.setUseMarkup, 'x')
    def testSetUseMarkupDelegateF(self):
        self.obj.addDelegation(mk_del('will_use_markup', 'f'))
        self.assert_(self.obj.setUseMarkup(True) is False)
        self.assert_(self.obj.setUseMarkup(False) is False)
    def testSetUseMarkupDelegateD(self):
        self.obj.addDelegation(mk_del('will_use_markup', 'd'))
        self.assert_(self.obj.setUseMarkup(True) is True)
        self.assert_(self.obj.setUseMarkup(False) is True)
    def testGetUseMarkup(self):
        self.obj.setUseMarkup(True)
        self.assertEqual(self.obj.getUseMarkup(), True)
        self.obj.setUseMarkup(False)
        self.assertEqual(self.obj.getUseMarkup(), False)

    def testSetUseUnderline(self):
        self.assert_(self.obj.setUseUnderline(True) is True)
        self.assert_(self.obj.setUseUnderline(False) is True)
    def testSetUseUnderlineFail(self):
        self.assertRaises(Exceptions.LabelError,
                          self.obj.setUseUnderline, 'x')
    def testSetUseUnderlineDelegateF(self):
        self.obj.addDelegation(mk_del('will_use_underline', 'f'))
        self.assert_(self.obj.setUseUnderline(True) is False)
        self.assert_(self.obj.setUseUnderline(False) is False)
    def testSetUseUnderlineDelegateD(self):
        self.obj.addDelegation(mk_del('will_use_underline', 'd'))
        self.assert_(self.obj.setUseUnderline(True) is True)
        self.assert_(self.obj.setUseUnderline(False) is True)
    def testGetUseUnderline(self):
        self.obj.setUseUnderline(True)
        self.assertEqual(self.obj.getUseUnderline(), True)
        self.obj.setUseUnderline(False)
        self.assertEqual(self.obj.getUseUnderline(), False)

    def testSetSelectable(self):
        self.assert_(self.obj.setSelectable(True) is True)
        self.assert_(self.obj.setSelectable(False) is True)
    def testSetSelectableFail(self):
        self.assertRaises(Exceptions.LabelError,
                          self.obj.setSelectable, 'x')
    def testSetSelectableDelegateF(self):
        self.obj.addDelegation(mk_del('will_set_selectable', 'f'))
        self.assert_(self.obj.setSelectable(True) is False)
        self.assert_(self.obj.setSelectable(False) is False)
    def testSetSelectableDelegateD(self):
        self.obj.addDelegation(mk_del('will_set_selectable', 'd'))
        self.assert_(self.obj.setSelectable(True) is True)
        self.assert_(self.obj.setSelectable(False) is True)
    def testGetSelectable(self):
        self.obj.setSelectable(True)
        self.assertEqual(self.obj.getSelectable(), True)
        self.obj.setSelectable(False)
        self.assertEqual(self.obj.getSelectable(), False)

    def testSetLineWrap(self):
        self.assert_(self.obj.setLineWrap(True) is True)
        self.assert_(self.obj.setLineWrap(False) is True)
    def testSetLineWrapFail(self):
        self.assertRaises(Exceptions.LabelError,
                          self.obj.setLineWrap, 'x')
    def testSetLineWrapDelegateF(self):
        self.obj.addDelegation(mk_del('will_set_line_wrap', 'f'))
        self.assert_(self.obj.setLineWrap(True) is False)
        self.assert_(self.obj.setLineWrap(False) is False)
    def testSetLineWrapDelegateD(self):
        self.obj.addDelegation(mk_del('will_set_line_wrap', 'd'))
        self.assert_(self.obj.setLineWrap(True) is True)
        self.assert_(self.obj.setLineWrap(False) is True)
    def testGetLineWrap(self):
        self.obj.setLineWrap(True)
        self.assertEqual(self.obj.getLineWrap(), True)
        self.obj.setLineWrap(False)
        self.assertEqual(self.obj.getLineWrap(), False)

class ImageTest(MiscTest):
    def setUp(self):
        super(ImageTest, self).setUp()
        self.obj = self.ui.Image(parent=self.box)
    def testSetFromFile(self):
        self.assert_(self.obj.setFromFile('blah.png') is True)
    def testSetFromFileFail(self):
        self.assertRaises(Exceptions.ImageError, self.obj.setFromFile, 42)
    def testSetFromFileDelegateF(self):
        self.obj.addDelegation(mk_del('will_set_from_file', 'f'))
        self.assert_(self.obj.setFromFile('blah.png') is False)
    def testSetFromFileDelegateD(self):
        self.obj.addDelegation(mk_del('will_set_from_file', 'd'))
        self.assert_(self.obj.setFromFile('blah.png') is True)
    def testSetFromStock(self):
        self.assert_(self.obj.setFromStock('open', 'menu') is True)
    def testSetFromStockTuple(self):
        self.assert_(self.obj.setFromStock(('open', 'menu')) is True)
    def testSetFromStockFail(self):
        self.assertRaises(Exceptions.ImageError, self.obj.setFromStock, 'foo', 'bar')
    def testSetFromStockDelegateF(self):
        self.obj.addDelegation(mk_del('will_set_from_stock', 'f'))
        self.assert_(self.obj.setFromStock('open', 'menu') is False)
    def testSetFromStockDelegateD(self):
        self.obj.addDelegation(mk_del('will_set_from_stock', 'd'))
        self.assert_(self.obj.setFromStock('open', 'menu') is True)

class CompositeViewTest(CompositeResponderTest, ViewTest):
    def setUp(self):
        super(CompositeViewTest, self).setUp()
        self.obj2 = self.ui.Label(label='testing')
    def testUpdate(self):
        self.assert_(self.obj.update() is None)
    def testSetBorderWidth(self):
        self.assert_(self.obj.setBorderWidth(4) is True)
    def testSetBorderWidthFail(self):
        self.assertRaises(Exceptions.CompositeViewError, self.obj.setBorderWidth, 'blah')
    def testSetBorderWidthDelegateF(self):
        self.obj.addDelegation(mk_del('will_set_border_width', 'f'))
        self.assert_(self.obj.setBorderWidth(4) is False)
    def testSetBorderWidthDelegateD(self):
        self.obj.addDelegation(mk_del('will_set_border_width', 'd'))
        self.assert_(self.obj.setBorderWidth(4) is True)
    def testRemoveChildFail(self):
        self.assertRaises(Exceptions.CompositionError, self.obj.removeChild, self.obj2)

class FrameTest(CompositeViewTest):
    def setUp(self):
        super(FrameTest, self).setUp()
        self.obj = self.ui.Frame(parent=self.box)
    def testSetLabel(self):
        self.assert_(self.obj.setLabel('foo') is True)
    def testSetLabelFail(self):
        self.assertRaises(Exceptions.FrameError,
                          self.obj.setLabel, '\xe1')
    def testSetLabelDelegateF(self):
        self.obj.addDelegation(mk_del('will_set_label', 'f'))
        self.assert_(self.obj.setLabel('foo') is False)
    def testSetLabelDelegateD(self):
        self.obj.addDelegation(mk_del('will_set_label', 'd'))
        self.assert_(self.obj.setLabel('foo') is True)
    def testGetLabel(self):
        self.obj.setLabel('foo')
        self.assertEqual(self.obj.getLabel(), 'foo')

class BoxTest(CompositeViewTest):
    def testSetSpacing(self):
        self.assert_(self.obj.setSpacing(4) is True)
    def testSetSpacingFail(self):
        self.assertRaises(Exceptions.BoxError,
                          self.obj.setSpacing, 'blah')
    def testSetSpacingDelegateF(self):
        self.obj.addDelegation(mk_del('will_set_spacing', 'f'))
        self.assert_(self.obj.setSpacing(4) is False)
    def testSetSpacingDelegateD(self):
        self.obj.addDelegation(mk_del('will_set_spacing', 'd'))
        self.assert_(self.obj.setSpacing(4) is True)
    def testGetSpacing(self):
        self.obj.setSpacing(4)
        self.assertEqual(self.obj.getSpacing(), 4)
    def testSetHomogeneous(self):
        self.assert_(self.obj.setHomogeneous(True) is True)
        self.assert_(self.obj.setHomogeneous(False) is True)
    def testSetHomogeneousFail(self):
        self.assertRaises(Exceptions.BoxError,
                          self.obj.setHomogeneous, 'x')
    def testSetHomogeneousDelegateF(self):
        self.obj.addDelegation(mk_del('will_set_homogeneous', 'f'))
        self.assert_(self.obj.setHomogeneous(True) is False)
        self.assert_(self.obj.setHomogeneous(False) is False)
    def testSetHomogeneousDelegateD(self):
        self.obj.addDelegation(mk_del('will_set_homogeneous', 'd'))
        self.assert_(self.obj.setHomogeneous(True) is True)
        self.assert_(self.obj.setHomogeneous(False) is True)
    def testGetHomogeneous(self):
        self.obj.setHomogeneous(True)
        self.assertEqual(self.obj.getHomogeneous(), True)
        self.obj.setHomogeneous(False)
        self.assertEqual(self.obj.getHomogeneous(), False)


class VBoxTest(BoxTest):
    def setUp(self):
        super(VBoxTest, self).setUp()
        self.obj = self.ui.VBox(parent=self.box)
class HBoxTest(BoxTest):
    def setUp(self):
        super(HBoxTest, self).setUp()
        self.obj = self.ui.HBox(parent=self.box)
class ButtonBoxTest(BoxTest):
    def testSetLayout(self):
        self.assert_(self.obj.setLayout('default') is True)
    def testSetLayoutFail(self):
        self.assertRaises(Exceptions.ButtonBoxError,
                          self.obj.setLayout, 'blah')
    def testSetLayoutDelegateF(self):
        self.obj.addDelegation(mk_del('will_set_layout', 'f'))
        self.assert_(self.obj.setLayout('default') is False)
    def testSetLayoutDelegateD(self):
        self.obj.addDelegation(mk_del('will_set_layout', 'd'))
        self.assert_(self.obj.setLayout('default') is True)
    def testGetLayout(self):
        self.obj.setLayout('default')
        self.assertEqual(self.obj.getLayout(), 'default')
class HButtonBoxTest(ButtonBoxTest):
    def setUp(self):
        super(HButtonBoxTest, self).setUp()
        self.obj = self.ui.HButtonBox(parent=self.box)
class VButtonBoxTest(ButtonBoxTest):
    def setUp(self):
        super(VButtonBoxTest, self).setUp()
        self.obj = self.ui.VButtonBox(parent=self.box)
    
class NotebookTest(CompositeViewTest):
    def setUp(self):
        super(NotebookTest, self).setUp()
        self.obj = self.ui.Notebook(parent=self.box)
    def testInsertPage(self):
        self.assert_(self.obj.insertPage(0, self.obj2, 'Foo', 'foo') is True)
    def testAppendPage(self):
        self.assert_(self.obj.appendPage(self.obj2, 'Foo', 'foo') is True)
    def testPrependPage(self):
        self.assert_(self.obj.appendPage(self.obj2, 'Foo', 'foo') is True)
    def testInsertPage(self):
        self.assert_(self.obj.insertPage(0, self.obj2, 'Foo', 'foo') is True)
    def testInsertPageNoMenu(self):
        self.assert_(self.obj.insertPage(0, self.obj2, 'Foo') is True)
    def testInsertPageBadChild(self):
        self.assertRaises(Exceptions.NotebookError,
                          self.obj.insertPage,
                          0, 'blah', 'Foo')
    def testInsertPageDelegateF(self):
        self.obj.addDelegation(mk_del('will_insert_page', 'f'))
        self.assert_(self.obj.insertPage(0, self.obj2, 'Foo', 'foo') is False)
    def testInsertPageDelegateD(self):
        self.obj.addDelegation(mk_del('will_insert_page', 'd'))
        self.assert_(self.obj.insertPage(0, self.obj2, 'Foo', 'foo') is True)
    def testNextPage(self):
        self.assert_(self.obj.nextPage() is True)
    def testNextPageDelegateF(self):
        self.obj.addDelegation(mk_del('will_change_to_next_page', 'f'))
        self.assert_(self.obj.nextPage() is False)
    def testNextPageDelegated(self):
        self.obj.addDelegation(mk_del('will_change_to_next_page', 'd'))
        self.assert_(self.obj.nextPage() is True)
    def testPrevPage(self):
        self.assert_(self.obj.prevPage() is True)
    def testPrevPageDelegateF(self):
        self.obj.addDelegation(mk_del('will_change_to_prev_page', 'f'))
        self.assert_(self.obj.prevPage() is False)
    def testPrevPageDelegated(self):
        self.obj.addDelegation(mk_del('will_change_to_prev_page', 'd'))
        self.assert_(self.obj.prevPage() is True)
    def testChangePage(self):
        self.assert_(self.obj.changePage(0) is True)
    def testChangePageDelegateF(self):
        self.obj.addDelegation(mk_del('will_change_to_page', 'f'))
        self.assert_(self.obj.changePage(0) is False)
    def testChangePageDelegated(self):
        self.obj.addDelegation(mk_del('will_change_to_page', 'd'))
        self.assert_(self.obj.changePage(0) is True)

class TableTest(CompositeViewTest):
    def setUp(self):
        super(TableTest, self).setUp()
        self.obj = self.ui.Table(parent=self.box, size=(2,2))
    def testAttach(self):
        self.assert_(self.obj.attach(self.obj2, 0, 1, 0, 1) is True)
    def testAttachBadWidget(self):
        self.assertRaises(Exceptions.TableError,
                          self.obj.attach,
                          'blah', 0, 1, 0, 1)
    def testAttachBadLeft(self):
        self.assertRaises(Exceptions.TableError,
                          self.obj.attach,
                          self.obj2, 'blah', 1, 0, 1)
    def testAttachRight(self):
        self.assertRaises(Exceptions.TableError,
                          self.obj.attach,
                          self.obj2, 0, 'blah', 0, 1)
    def testAttachTop(self):
        self.assertRaises(Exceptions.TableError,
                          self.obj.attach,
                          self.obj2, 0, 1, 'blah', 1)
    def testAttachBadBottom(self):
        self.assertRaises(Exceptions.TableError,
                          self.obj.attach,
                          self.obj2, 0, 1, 0, 'blah')
    def testAttachDelegateF(self):
        self.obj.addDelegation(mk_del('will_attach', 'f'))
        self.assert_(self.obj.attach(self.obj2, 0, 1, 0, 1) is False)
    def testAttachDelegateD(self):
        self.obj.addDelegation(mk_del('will_attach', 'd'))
        self.assert_(self.obj.attach(self.obj2, 0, 1, 0, 1) is True)
                               
    def testSetColSpacings(self):
        self.assert_(self.obj.setColSpacings(20) is True)
    def testSetColSpacingsFail(self):
        self.assertRaises(Exceptions.TableError,
                          self.obj.setColSpacings, 'foo')
    def testSetColSpacingsDelegateF(self):
        self.obj.addDelegation(mk_del('will_set_col_spacings', 'f'))
        self.assert_(self.obj.setColSpacings(20) is False)
    def testSetColSpacingsDelegateD(self):
        self.obj.addDelegation(mk_del('will_set_col_spacings', 'd'))
        self.assert_(self.obj.setColSpacings(20) is True)
    def testSetColSpacing(self):
        self.assert_(self.obj.setColSpacing(0, 20) is True)
    def testSetColSpacingBadCol(self):
        self.assertRaises(Exceptions.TableError,
                          self.obj.setColSpacing, 'foo', 0)
    def testSetColSpacingBadSpacing(self):
        self.assertRaises(Exceptions.TableError,
                          self.obj.setColSpacing, 0, 'foo')
    def testSetColSpacingDelegateF(self):
        self.obj.addDelegation(mk_del('will_set_col_spacing', 'f'))
        self.assert_(self.obj.setColSpacing(0, 20) is False)
    def testSetColSpacingsDelegateD(self):
        self.obj.addDelegation(mk_del('will_set_col_spacing', 'd'))
        self.assert_(self.obj.setColSpacing(0, 20) is True)
    def testGetColSpacing1(self):
        self.obj.setColSpacing(0, 20)
        self.assertEqual(self.obj.getColSpacing(0), 20)
    def testGetColSpacing2(self):
        self.obj.setColSpacings(20)
        self.assertEqual(self.obj.getColSpacing(0), 20)
    def testGetDefaultColSpacing(self):
        self.obj.setColSpacings(20)
        self.assertEqual(self.obj.getDefaultColSpacing(), 20)

    def testSetRowSpacings(self):
        self.assert_(self.obj.setRowSpacings(20) is True)
    def testSetRowSpacingsFail(self):
        self.assertRaises(Exceptions.TableError,
                          self.obj.setRowSpacings, 'foo')
    def testSetRowSpacingsDelegateF(self):
        self.obj.addDelegation(mk_del('will_set_row_spacings', 'f'))
        self.assert_(self.obj.setRowSpacings(20) is False)
    def testSetRowSpacingsDelegateD(self):
        self.obj.addDelegation(mk_del('will_set_row_spacings', 'd'))
        self.assert_(self.obj.setRowSpacings(20) is True)
    def testSetRowSpacing(self):
        self.assert_(self.obj.setRowSpacing(0, 20) is True)
    def testSetRowSpacingBadRow(self):
        self.assertRaises(Exceptions.TableError,
                          self.obj.setRowSpacing, 'foo', 0)
    def testSetRowSpacingBadSpacing(self):
        self.assertRaises(Exceptions.TableError,
                          self.obj.setRowSpacing, 0, 'foo')
    def testSetRowSpacingDelegateF(self):
        self.obj.addDelegation(mk_del('will_set_row_spacing', 'f'))
        self.assert_(self.obj.setRowSpacing(0, 20) is False)
    def testSetRowSpacingsDelegateD(self):
        self.obj.addDelegation(mk_del('will_set_row_spacing', 'd'))
        self.assert_(self.obj.setRowSpacing(0, 20) is True)
    def testGetRowSpacing1(self):
        self.obj.setRowSpacing(0, 20)
        self.assertEqual(self.obj.getRowSpacing(0), 20)
    def testGetRowSpacing2(self):
        self.obj.setRowSpacings(20)
        self.assertEqual(self.obj.getRowSpacing(0), 20)
    def testGetDefaultRowSpacing(self):
        self.obj.setRowSpacings(20)
        self.assertEqual(self.obj.getDefaultRowSpacing(), 20)

    def testSetHomogeneous(self):
        self.assert_(self.obj.setHomogeneous(True) is True)
        self.assert_(self.obj.setHomogeneous(False) is True)
    def testSetHomogeneousFail(self):
        self.assertRaises(Exceptions.TableError,
                          self.obj.setHomogeneous, 'x')
    def testSetHomogeneousDelegateF(self):
        self.obj.addDelegation(mk_del('will_set_homogeneous', 'f'))
        self.assert_(self.obj.setHomogeneous(True) is False)
        self.assert_(self.obj.setHomogeneous(False) is False)
    def testSetHomogeneousDelegateD(self):
        self.obj.addDelegation(mk_del('will_set_homogeneous', 'd'))
        self.assert_(self.obj.setHomogeneous(True) is True)
        self.assert_(self.obj.setHomogeneous(False) is True)
    def testGetHomogeneous(self):
        self.obj.setHomogeneous(True)
        self.assertEqual(self.obj.getHomogeneous(), True)
        self.obj.setHomogeneous(False)
        self.assertEqual(self.obj.getHomogeneous(), False)

    def testResize(self):
        self.assert_(self.obj.resize(20,20) is True)
    def testResizeHuge(self):
        self.assert_(self.obj.resize(65535,65535) is True)
    def testResizeSizeNotInt(self):
        self.assertRaises(Exceptions.TableError,
                          self.obj.resize,
                          'foo', 'bar')

class ControlTest(ViewTest):
    def testSetDefaultValue(self):
        self.assert_(self.obj.setDefaultValue('foo') is True)
    def testSetDefaultValueDelegateF(self):
        self.obj.addDelegation(mk_del('will_set_default_value', 'f'))
        self.assert_(self.obj.setDefaultValue('foo') is False)
    def testSetDefaultValueDelegateD(self):
        self.obj.addDelegation(mk_del('will_set_default_value', 'd'))
        self.assert_(self.obj.setDefaultValue('foo') is True)
    def testGetDefaultValue(self):
        self.obj.setDefaultValue('foo')
        self.assertEqual(self.obj.getDefaultValue(), 'foo')
    def testSetAction(self):
        self.assert_(self.obj.setAction('blah') is True)
    def testDoActionCallable(self):
        self.obj.setAction(lambda x:'foo')
        self.assert_(self.obj.doAction() is 'foo')
    def testDoActionNotCallable(self):
        self.obj.setAction('foo')
        self.assert_(self.obj.doAction() is 'foo')
    

class ButtonTest(ControlTest):
    def setUp(self):
        super(ButtonTest, self).setUp()
        self.obj = self.ui.Button(parent=self.box)

def main():
    suite = unittest.TestSuite()
    for test in (ApplicationTest,
                 #LabelTest,
                 #ImageTest,
                 #FrameTest,
                 #VBoxTest,
                 #HBoxTest,
                 #VButtonBoxTest,
                 #HButtonBoxTest,
                 #NotebookTest,
                 #TableTest,
                 ButtonTest
                 ):
        suite.addTest(unittest.makeSuite(test))
    
    unittest.TextTestRunner(verbosity=1).run(suite)

if __name__ == '__main__':
    import pygtk
    pygtk.require('2.0')
    import gtk
    cimarron.setEngine('Gtk2')
    gtk.idle_add(main)
    gtk.main()
