# -*- coding: ISO-8859-1 -*-
from Generic.Composite import Composite
from ViewController import ViewController

from Modeling.EditingContext import EditingContext

from cimarron import getEngine, Failed
# get the engine
ui= getEngine ()
from Utils import Debug
# Debug.sections.append ('ConsistencyController')

class ConsistencyController (ViewController, Composite):
    """
    Controller that warns the user that is trying to close the window
    when the data is dirty. It also has a NoteBook.
    """
    __kwargs= ('windowTitle', 'model', 'modelClass')
    def __init__ (self, *args, **kwargs):
        # already takes care of model and modelClass params via setModel{,Class}()
        # self.editingContext= NewEditingContext ()
        self.editingContext= EditingContext ()
        self._processArgs(ConsistencyController, kwargs)

    def buildView (self):
        self.win= ui.Window (parent=self.getParent(),
                             title=self.getWindowTitle ())
        self.win.addDelegation (self)

        v= ui.VBox (parent=self.win)
        self.tabbook= ui.Notebook (parent=v)

        # the save button is connected to the action thru save()
        h= ui.HBox (parent=v)
        okButton= ui.Button (parent=h,
                             action=lambda *ignore: self.save (),
                             label=u'_Guardar')
        resetButton= ui.Button (parent=h,
                                action=lambda *ignore: self.reset (),
                                label=u'_Reestablecer valores anteriores')
    def show (self):
	self.update ()
        self.win.show ()
    def hide (self):
        self.win.hide ()
    def _getView (self):
        return getattr (self, 'win', None)
	
    def addChild (self, child, label):
	self.tabbook.appendPage (child, label)
        super (ConsistencyController, self).addChild (child)

    def setWindowTitle (self, windowTitle):
        self.windowTitle= windowTitle
    def getWindowTitle (self):
        return self.windowTitle

    def save (self):
        model= self.getModel ()
        try:
            self.debug ('saving %s[%s]' % (model, str (model.globalID ().keyValues ())))
        except:
            self.debug ('saving %s' % model)
        for child in self.getChildren ():
            # so children can add new objects
	    child.aboutToSave ()
            self.debug ("save: child's ec: %s" % child.getEditingContext ())
        self.debug ("save: our ec: %s" % self.editingContext)
        self.editingContext.saveChanges ()
        self.debug ('saving %s[%s]' % (model, str (model.globalID ())))
        if model.globalID ().isTemporary ():
            # is a new inserted and now saved model
            # gotta refetch.
            self.debug ('refetching')
    # alias
    commit= save
    def reset (self):
        # BUG: does this leak mem?
        self.holdModel ()
        self.setEditingContext (EditingContext ())
        # here there is no model!
        self.insertModel ()
        # tell the children a new model has born
        self.changeModel ()
    # alias
    rollback= reset
    def isDirty (self):
	dirty= False
	for child in self.getChildren ():
	    dirty|= bool (child.isDirty ())
	return dirty
	
    def updateView (self):
	# """
	# abstact method. please reimplement.
	# """
	self.win.update ()
    # alias
    update= updateView

    def updateModel (self, model=None):
        if model:
            self.setModel (model)
        else:
            model= self.getModel ()
        return model

    def will_delete (self, *ignore):
        """
        delegate for the window destroy action.
        doesn't allow destroying it, just hides it
        """
        if self.isDirty ():
            # tis dirty, ask the user
            if ui.WarningDialog (message=u'Los cambios no han sido guardados. Qué desea hacer con ellos?', yea=u'_Guardar', nay= u'_Descartar').run ():
                self.save ()
            else:
                self.reset ()
        self.win.hide ()
        return Failed
