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
# Debug.sections.append ('View')

from Responder import Responder, _
from Exceptions import ViewError, ViewParentingError

class View(Responder):
    """
    Everything that is a widget inherits from View.

    Constructor arguments %s are pretty obvious.
    """
    __kwargs = ('name', 'tip', 'sizeRequest', 'hidden')
    __doc__ = __doc__ % str(__kwargs)
    __obligs = {'_name': lambda:None,
                '_hidden': lambda:True,
                }

    def setName(self, name):
        """
        Set the name of the widget.

        Not used for anything much, but you can use it to tell widgets
        apart (for example).
        """
        self._name = name
    def getName(self):
        """
        Return the name of the widget.
        """
        return self._name

    def setParent(self, parent):
        """
        Set the parent of the widget.

        Called with None as parent, unparent the widget.

        If called with a non-None parent and already parent, throws a
        ViewParentingError.
        """
        if self.getParent() is not None and parent is not None:
            raise ViewParentingError, _("View %s is already parented to %s.") % (self, self.getParent ())
        super(View, self).setParent(parent)
    def getWindow(self):
        """
        Return the toplevel widget, or None if unparented.
        """
        parent = self.getParent()
        if parent is not None:
            return parent.getWindow()
        else:
            return None

    def pushStatus(self, message, timeout=0, type="ok"):
        """
        Push a message onto the status area.

        See the docs for Window.
        """
        return self.getParent().pushStatus(message, timeout, type)
    def popStatus(self):
        """
        Remove the last message pushed onto the status area.

        See the docs for Window.
        """
        return self.getParent().popStatus()
    def removeStatus(self, msgid):
        """
        Remove a specific message from the status area.

        See the docs for Window.
        """
        return self.getParent().removeStatus(msgid)

    def focus(self):
        """
        Make this widget the active one, out of all the ones in its
        window.

        This does *not* ensure the widget has keyboard focus.

        Returns the result of the delegation (i.e., True if delegates
        agreed to doing it). Raises a ViewError if anything bad
        happens.
        """
        if self.delegate('will_focus'):
            try:
                self._doFocus()
            except:
                raise ViewError, _("Unable to focus")
            return True
        return False
    def hide(self):
        """
        Make this widget invisible.

        Returns the result of the delegation (i.e., True if delegates
        agreed to doing it). Raises a ViewError if anything bad
        happens.
        """
        if self.delegate('will_hide'):
            self.debug ('hiding %s' % self)
            try:
                self._doHide()
                self._hidden = True
            except:
                raise ViewError, _("Unable to hide")
            return True
        return False
    def show(self):
        """
        Make this widget, and any subwidgets thereof, visible.

        Returns the result of the delegation (i.e., True if delegates
        agreed to doing it). Raises a ViewError if anything bad
        happens.
        """
        if self.delegate('will_show'):
            self.debug ('showing %s' % self)
            try:
                self._doShow()
                self._hidden = False
            except:
                raise ViewError, _("Unable to show")
            return True
        return False
    def isHidden(self):
        return self._hidden is True
    def isShown(self):
        return self._hidden is False
    def disable(self):
        """
        Make the widget unresponsive to user interaction.

        Returns the result of the delegation (i.e., True if delegates
        agreed to doing it). Raises a ViewError if anything bad
        happens.
        """
        if self.delegate('will_disable'):
            try:
                self._doDisable()
            except:
                raise ViewError, _("Unable to disable")
            return True
        return False
    def enable(self):
        """
        Make the widget responsive to user interaction.
        
        Returns the result of the delegation (i.e., True if delegates
        agreed to doing it). Raises a ViewError if anything bad
        happens.
        """
        if self.delegate('will_enable'):
            try:
                self._doEnable()
            except:
                raise ViewError, _("Unable to enable")
            return True
        return False
    
    def setTip(self, tip):
        """
        Sets the `tip' for this widget.
        """
        if self.delegate('will_set_tip'):
            try:
                self._doSetTip(tip)
            except:
                raise ViewError, _("Unable to set tip")
            return True
        return False
    
    def busy(self):
        """
        Make the widget look `busy'.

        This is different from `disabled': the user can still interact
        (unless the widget is also disabled). The idea is to give some
        feedback because, for example, stuff is still changeing.

        Some widgets might not support this.
        
        Returns the result of the delegation (i.e., True if delegates
        agreed to doing it). Raises a ViewError if anything bad
        happens.
        """
        if self.delegate('will_busy'):
            try:
                self._doBusy()
            except:
                raise ViewError, _("Unable to busy")
            return True
        return False

    def idle(self):
        """
        Make the widget *not* look `busy'.

        Returns the result of the delegation (i.e., True if delegates
        agreed to doing it). Raises a ViewError if anything bad
        happens.
        """
        if self.delegate('will_idle'):
            try:
                self._doIdle()
            except:
                raise ViewError, _("Unable to idle")
            return True
        return False


    def setSizeRequest(self, *sizes):
        """
        Request for a specific size (in pixels) of the widget.

        Argument is a 2-tuple of (int or None)s, or two (int or
        None)s. If int, set requested size; if None, unset.

        Returns the result of the delegation (i.e., True if delegates
        agreed to doing it). Raises a ViewError if anything bad
        happens.
        """
        try:
            x, y = sizes
        except ValueError:
            x, y = sizes[0]
        if self.delegate('will_resize', args=(x, y)):
            try:
                self._doSetSizeRequest(x, y)
            except:
                raise ViewError, _("Unable to set size request")
            return True
        return False
    def getSizeRequest(self):
        """
        Return the requested size of the widget, or None if it hasn't
        been requested.
        """
        return self._doGetSizeRequest()
