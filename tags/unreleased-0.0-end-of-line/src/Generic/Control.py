# -*- python -*- coding: ISO-8859-1 -*-
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
# Debug.sections.append ('Control')

from View import View, _
from Exceptions import ControlError

class Control(View):
    """
    A Control is a View through which the user can tell the controller
    stuff.

    Controls have a value, which is set via a valueLoader provided
    by the conroller, and an action, which is called from the control
    when the user requests the controller to do stuff.

    For example, the action of a button is called when the user presses it.

    @newfield conf: Configuration option, Configuration options

    Additional keyword arguments:
    """
    # value stops being a public attr
    # __kwargs = ('defaultValue', 'value', 'valueLoader', 'action')
    __kwargs = ('defaultValue', 'valueLoader', 'action')
    __doc__ += "%s\n" % (__kwargs,)
    _default_value = None
    __obligs = {'_action': lambda: None,
                '_valueLoader': lambda: None,
                # '_value': lambda: None,
                }

    def __init__ (self, **kwargs):
        """
        Constructor
        
        TODO: put real pre
        pre::
            True
            
        @newfield maparam: MagicArgs parameter, MagicArgs parameters

        @maparam: action - The action to be executed on user interaction.

        @maparam: valueLoader - The callable that can retrieve the value for the Control.

        """
        self._processArgs(Control, kwargs)

    # Q: do we still support this? (mdione)
    def setDefaultValue(self, value):
        """
        Set the default value of the control.

        The default value is the one the control starts out with, and
        is the one you go back to with reset().

        @param value: the default value.
            
        """
        # no pre means pre:: True
        if self.delegate('will_set_default_value', args=value):
            self._default_value = value
            return True
        return False
    def getDefaultValue(self):
        """
        Return the current default value.
        """
        # no pre means pre:: True
        return self._default_value

    def setAction(self, action):
        """
        The action is a callback that is called with the Control as
        sole argument when the user activates the Control and the
        delegates agree it would be a good idea.

        @param action: the callable or value.
        """
        self._action = action
        return True
    def getAction (self):
        return self._action
    def doAction(self, *args, **kwargs):
        """
        Call the action.

        If the action is callable, call it, and return whatever it
        returns. If the action is *not* callable, return the action
        itself.

        Don't call directly unless you know what you're doing.
        """
        self.debug ('calling action w/ %s and %s' % (args, kwargs))
        self.setValue 
        if callable(self._action):
            return self._action(self, *args, **kwargs)
        else:
            return self._action

    def setValueLoader(self, valueLoader):
        """
        The valueLoader is a callback that is called when the Control wants
        the value from the Model. It should return that value, or fail.
        """
        self._valueLoader = valueLoader
    # def getValueLoader(self):
        # return self._valueLoader
    def loadValue(self, *args, **kwargs):
        """
        Call the getter.

        If the getter is callable, call it, and return whatever it
        returns. If the getter is *not* callable, return the getter
        itself.

        Don't call directly; use update() instead.
        """
        if callable(self._valueLoader):
            return self._valueLoader(self, *args, **kwargs)
        else:
            return self._valueLoader

    def getValue(self):
        """
        Returns the (internal) value of a Control.
        """
        return self._value
    def setValue(self, value):
        """
        setValue sets the value (or values) of the Control to the
        given value.  (delegates willing)

        Returns True if able to set, False otherwise.

        Don't call directly; use update() instead.
        """
        if self.delegate ('will_set_value', args=value):
            self.debug ('setting value to %s' % value, parents=5)
            self._value = value
            return True
        else:
            return False


    def update(self):
        """
        Reloads the Control's value from the Model.

        Returns the result of the delegation (i.e., True if delegates
        agreed to doing it). Raises a ControlError if anything bad
        happens.
        """
        if self.delegate('will_update'):
            try:
                value = self.loadValue()
            except:
                raise ControlError, _("Unable to reload the value from the Model")
            self.setValue(value)
            return True
        return False

    def submit(self):
        """
        Saves the Control's value in the Model.

        Returns the result of the delegation (i.e., True if delegates
        agreed to doing it). Raises a ControlError if anything bad
        happens.
        """
        if self.delegate('will_submit'):
            try:
                self.doAction()
            except:
                raise ControlError, _("Unable to save the value in the Model")
            return True
        return False

    def reset(self):
        """
        Resets the StatefulControl's value to its initial value.

        Returns the result of the delegation (i.e., True if delegates
        agreed to doing it). Raises a ControlError if anything bad
        happens.
        """
        if self.delegate('will_reset'):
            try:
                self.setValue(self.getDefaultValue())
            except:
                raise ControlError, _("Unable to reset the value")
            return True
        return False
