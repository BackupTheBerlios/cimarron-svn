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
# Debug.sections.append ('StatefulControl')

from Control import Control, _

class StatefulControl(Control):
    """
    `StatefulControl's are `Control's that keep both an `internal'
    representation, that the controller wants, and a `displayed'
    representation, that the user sees. They (can) have special
    purpose delegates (printers and parsers) to do the conversion
    between these representations.

    Additional keyword args:
    """
    __kwargs = ('parsers', 'printers')
    __obligs = {'_parsers': list,
                '_printers': list}
    __doc__ += "%s\n" % (__kwargs,)

    def setValue(self, value):
        """
        StatefulControls have two values, an internal one and a displayed one.
        So setValue has to set both to the given value, as per its docs in Control.
        Additionally, if the delegates don't want us to, we shouldn't do it.

        returns True if able to set, False otherwise.
        """
        self.debug ("setting value to %s" % value)
        return super(StatefulControl, self).setValue(value) \
               and self._doSetValue(self.string())

    def acceptInput (self):
        """
        Sets the internal value to the displayed value.
        """
        value = self.parse()
        if not value is None:
            self.debug ('accepting %s' % value, parent=5)
            self.setValue (value)
    def rejectInput(self, value=None):
        """
        Conversely to acceptInput, this sets the displayed value
        to the internal value.
        """
        value = self.string()
        self.debug ('input rejected %s' % value)
        self._doSetValue(value)

    def submit(self):
        """
        Only does it if the value is different from the model.
        """
        self.acceptInput()
        if self.loadValue()!=self.getValue():
            super(StatefulControl, self).submit()
        self.debug ('submitted')

    def setParsers(self, parsers):
        self._parsers = list(parsers)
    def appendParser(self, parser):
        self._parsers.append(parser)
    def prependParser(self, parser):
        self._parsers.insert(0, parser)
    def setPrinters(self, printers):
        self._printers = list(printers)
    def appendPrinter(self, printer):
        self._printers.append(printer)
    def prependPrinter(self, printer):
        self._printers.insert(0, printer)

    def parse(self):
        value = v = self._doGetValue()
        self.debug ('got value %s' % value)
        for i in self._parsers:
            v = i(value)
            if v is not None:
                break
        if v is None and value is not None:
            self.pushStatus(_('Unable to parse "%s"') % (`value`,), timeout=10, type='warn')
            value = None
        else:
            value = v
        return value

    def string(self):
        value = v = self.getValue()
        for i in self._printers:
            v = i(value)
            if v is not None:
                break
        if v is None and value is not None:
            self.pushStatus(_('Unable to represent "%s"') % (`value`,), timeout=10, type='warn')
            value = None
        else:
            value = v
        return value

