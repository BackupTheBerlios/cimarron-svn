from Utils import Debug
# Debug.sections.append ('ViewController')

from Controllers.Controller import Controller
from Generic.Control import Control

class ViewController (Controller, Control):
    """
    A Controller that builds a View, and so can be used as such.
    """
    __kwargs= ('parent', 'action', 'valueLoader')
    __obligs= {'view': lambda: None,
               }
    def __init__ (self, **kwargs):
        # trick to capture the parent and pass it thru to our view
        if kwargs.has_key ('parent'):
            self.setViewParent (kwargs['parent'])
            del kwargs['parent']
        self._processArgs (Controller, kwargs)

    def setViewParent (self, parent):
        self.debug ('setting parent to %s' % parent)
        if getattr (self, 'view', None):
            self.view.setParent (parent)
        self._viewParent= parent
    setParent= setViewParent
    def getViewParent (self):
        return self._viewParent
    getParent= getViewParent

    def _getView (self):
        ans= getattr (self, 'view', None)
        return ans

    def update (self):
        self.debug ('updating VC')
        self._getView ().update ()

    def setModel (self, model):
        super (ViewController, self).setModel (model)
        if self._getView ():
            self.update ()
