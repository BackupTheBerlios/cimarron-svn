# -*- coding: ISO-8859-1 -*-
# Copyright 2004 Fundacion Via Libre
#
# This file is part of PAPO.
# 
# PAPO is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
# 
# PAPO is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with PAPO; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA

from Utils import Debug
# Debug.sections.append ('Controller')

from Generic.Responder import Responder
from Generic.Exceptions import ControlError

from Modeling.FaultHandler import AccessArrayFaultHandler

class ControllerError (ControlError):
    pass

class Controller (Responder):
    """
    """
    __kwargs = ('defaultValue', 'value', 'editingContext', 'viewParent', 'view', 'model', 'rollback')
    __doc__ += "%s\n" % (__kwargs,)
    _default_value = None
    __obligs = {'_action': lambda: None,
                '_value': lambda: None,
                '_model': lambda: None,
                '_viewParent': lambda: None,
                'new' : lambda : True,
                }

    def __init__ (self, **kwargs):
        self._processArgs (Controller, kwargs)

    def setEditingContext (self, ec):
        self.debug ('setting ec %s; model-> ' % self._model)
        self.editingContext= ec
    def getEditingContext (self):
        return self.editingContext

    def setModel (self, model):
        self.debug ('setting model ->%s' % model)
        self._model= model
    def getModel (self):
        return self._model

    def setModelClass (self, klass):
        self.modelClass= klass
	    
    def aboutToSave (self):
	"""
	abstact method. please reimplement.
	"""
	pass
	
    def isDirty (self):
	"""
	abstact method. please reimplement.
	"""
	pass
	
    def newModel (self):
	"""
	abstact method. please reimplement.
	"""
	pass
	
    def holdModel (self):
        self.debug ('holding')
        try:
            self.hold= self._model.snapshot_raw ()
        except:
            self.debug ('failed holding; ignoring')

    def insertModel (self):
        self. debug ('releasing')
        if hasattr (self, 'hold'):
            ec= self.getEditingContext ()
            self.setModel (ec.faultForRawRow (self.hold, self.modelClass))
            del self.hold
        else:
            self.debug ('no hold model; creating a new one')
            self.newModel ()
