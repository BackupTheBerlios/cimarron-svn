# -*- coding: utf-8 -*-
#
# Copyright 2005 Fundación Via Libre
#
# This file is part of PAPO.
#
# PAPO is free software; you can redistribute it and/or modify it under the
# terms of the GNU General Public License as published by the Free Software
# Foundation; either version 2 of the License, or (at your option) any later
# version.
#
# PAPO is distributed in the hope that it will be useful, but WITHOUT ANY
# WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
# FOR A PARTICULAR PURPOSE.  See the GNU General Public License for more
# details.
#
# You should have received a copy of the GNU General Public License along with
# PAPO; if not, write to the Free Software Foundation, Inc., 59 Temple Place,
# Suite 330, Boston, MA 02111-1307 USA

from zope.interface import Attribute, Interface
from zope.schema import Object

from fvl.cimarron.tools import Null

class IModel(Interface):
    def getattr(attr):
        """
        return the value of attribute 'attr'.
        """
    def setattr(attr, value):
        """
        set the value of attribute 'attr'  to 'value'.
        """

class ISelectionModel(IModel):
    def fetch(**qualifier):
        """
        return a generator of objects, filtered by 'qualifier'
        (e.g. {'name': 'foo*'})
        """

class IWidget(Interface):
    expand = Attribute("Whether the widget is given extra space")
    fill = Attribute("Whether the widget grows to occupy all the extra space")
    border = Attribute("The extra space around the widget")
    parent = Attribute("The parent of the widget")

    def delegate(message, *args):
        """
        Request delegates' consensus over whether a certain action should be
        performed.

        L{Control}s (L{Button <skins.gtk2.Button>}, L{Entry
        <skins.gtk2.Entry>}, L{Controller <controllers.Controller>} itself,
        etc.)  have a purpose in life, and that purpose is to react to a given
        action when acted on. You press a button, and bam! the action is shot
        out (for example, 'Close'). The connection is direct and unequivocal;
        if the button is enabled the action will be carried out.

        However, other kinds of interaction are possible as is the example of
        closing a window: in these cases the manipulation is more direct,
        while the process of deciding if the action should be carried out is
        more subtle, and the actors involved might be spread out over the
        L{Controller <controllers.Controller>} hierarchy. Delegation is a
        means of permitting these concensus-like desicions processes to occur,
        while leaving the logic for the decisions themselves next to the
        decision makers.

        Every object that delegates actions has a list of delegates. When an
        action occurs the C{delegates} list is traversed, asking each delegate
        what they think of the action. Based on the opinion of the delegates,
        the action is carried out or vetoed.

        The delegates that care about an action must have a method named after
        the action (for example, if a delegate cares about 'hide' events it
        would have a 'will_hide' method). The method will be called to querie
        the delegate about the action, and the delegate must return one of the
        following:

          - L{ForcedNo}: halt traversal, do not perform the action.
          - L{No}: 'I vote no'; traversal continues.
          - L{Unknown}: same as not having the method: ignore this vote.
          - L{Yes}: 'I vote yes'; traversal continues.
          - L{ForcedYes}: halt traversal, perform the action.

        a single 'Yes' in a chain full of 'No's is a 'Yes' (in other
        words, a list of non-forced results is ORed).

        """

    def _concreteParenter(child):
        """
        Does the skin-specific magic that `glues' a child with its parent.
        Do not call directly.
        """
    def _connectWith (other):
        """
        Connects the widget with someone else. This is used for loading
        from XML files/objects.
        """

    mainWidget = Null
    _concreteWidget = Null
    _focusWidget = Null
    _outerWidget = Null
        

class IContainer(IWidget):
    children = Attribute("The list of children. It contains both"
                                   " graphical and non-grafical objects.")

    def show(): pass
    def hide(): pass
    def skeleton(parent=None): pass
    def dirty(): pass

class IWindow(IContainer):
    title = Attribute('')
    size = Attribute('')

    def screenshot(filename=None, frame=True):
        """
        Take a screenshot of the window.

        Store the image in file <filename>.

        If <filename> isn't given, use the filename of the caller
        with '.png' appended.

        If <frame> is true, include the windowmanager frames.

        """
    

class ISkin(Interface):
    def _run():
        """
        _run() is called from Application.run, to set in motion whatever
        mechanism the concrete backend uses to display widgets.
        """

    def _quit():
        """
        _quit() is called from Application.quit to terminate the application;
        it might never return (or leave the backend in an unspecified
        state)
        """

    def _schedule(timeout, callback, repeat=False):
        """
        _schedule is called from Application.schedule to actually do the
        scheduling of the delayed action.
        """

    def _concreteParenter(parent, child):
        """
        _concreteParenter dos the skin-specific magic that `glues' a
        child with its parent.
        """

    # thanks to Stephan Richter <srichter@cosmos.phy.tufts.edu>
    Window = Object(
        schema = IWindow,
        title = u'Window',
        required = True,
        )


class IStore(Interface):
    """
    blah.
    """
    def save():
        """
        Saves the object(s) to permanent storage.
        """
    def discard():
        """
        Discards changes performed to the object(s).
        """
