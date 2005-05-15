# -*- coding: utf-8 -*-
#
# Copyright 2003 Fundación Via Libre
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

"""

L{common} is a set of abstract classes that
are the foundation of Cimarron's class hierarchy.

"""

from new import instancemethod
import operator
import libxml2

__all__ = ('Widget', 'Container', 'Control',
           'ForcedNo', 'No', 'Unknown', 'Yes', 'ForcedYes',)

from papo.cimarron.tools import is_simple

def nullAction(*a, **k): pass

ForcedNo, No, Unknown, Yes, ForcedYes = -5, -1, 0, 1, 5

from papo import cimarron

class Widget(object):
    """
    L{Widget} is ...
    """

    def __init__(self, parent=None, **kw):
        """
        @param parent: the parent of the widget (you don't say!)
        @type parent: L{Widget}
        """
        super (Widget, self).__init__ (**kw)
        self.delegates = []
        self.parent = parent
        for k, v in kw.items ():
            setattr (self, k, v)

    def skelargs(self):
        """
        skelargs returns the dictionary of serialized attributes of an
        instance of L{Widget}. No promise of completeness is made:
        unserializable attributes can be dropped on the floor unless a
        promise is made to the contrary.
        """
        return {}

    def skeleton(self, parent=None):
        """
        Returns the XML representation of the L{Widget}.
        """
        if parent is None:
            parent = libxml2.newDoc("1.0")
        this = parent.newChild(None, self.__class__.__name__, None)
        for prop, value in self.skelargs().items():
            this.setProp(prop, repr(value))
        return this

    def _set_parent(self, parent):
        if parent is not None and self.parent is parent:
            raise ValueError, 'Child already in parent'
        if self.parent is not None:
            if parent is None:
                raise NotImplementedError, 'Cannot deparent'
            else:
                raise NotImplementedError, 'Cannot reparent'
        if parent is not None:
            parent.concreteParenter(self)
            parent._children.append(self)
            self.__parent = parent
    def _get_parent(self):
        try:
            return self.__parent
        except AttributeError:
            # only happens during init
            return None
    parent = property(_get_parent, _set_parent,
                      doc="parent is either the containing L{Widget}, or None")

    def _get_skin (self):
        try:
            return self.__skin
        except AttributeError:
            from papo.cimarron import skin
            self.__skin = skin
            return skin
    skin = property(_get_skin,
                    doc="the skin")

    def delegate(self, message, *args):
        """
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

          - L{ForcedNo}: halt traversal, do not perform the action
          - L{No}: 'I vote no'; traversal continues
          - L{Unknown}: same as not having the method: ignore this vote.
          - L{Yes}: 'I vote yes'; traversal continues
          - L{ForcedYes}: halt traversal, perform the action

        a single 'Yes' in a chain full of 'No's is a 'Yes'.

        """
        if self.delegates:
            truthTable = ((Unknown, Yes, No), (Yes, Yes, Yes), (No, Yes, No))
            av= Unknown
            for i in self.delegates:
                try:
                    rv= getattr(i, message, lambda *a: Unknown)(self, *args) or Unknown
                    av= truthTable[av][rv]
                except IndexError:
                    av= rv
                    break
            return av>=0
        return True

    def concreteParenter (self, child):
        """
        Does the skin-specific magic that `glues' a child with its parent.
        Do not call directly.
        """
        cimarron.skin.concreteParenter (self, child)

class Container(Widget):
    """
    An object that can contain (a list of) other objects
    (called its `children').
    """
    def __init__(self, **kw):
        super(Container, self).__init__(**kw)
        self._children = []

    def show(self):
        for i in self.children:
            i.show()

    def hide(self):
        for i in self.children:
            i.hide()

    def _get_children(self):
        return tuple(self._children)
    children = property(_get_children, None, None,
        """The list of children. It contains both graphical and
        non-grafical objects.""")

    def skeleton(self, parent=None):
        skel = super(Container, self).skeleton(parent)
        for child in self.children:
            child.skeleton(skel)
        return skel

class Control(Widget):
    """
    L{Control} is...
    """
    def __init__(self, onAction=None, value=None, **kw):
        super(Control, self).__init__(**kw)
        self.value = value
        self.onAction= onAction

    def _get_on_action (self):
        return self.__on_action
    def _set_on_action (self, onAction):
        if onAction is None:
            onAction = nullAction
        self.__on_action= instancemethod (onAction, self, Control)
    onAction= property (_get_on_action, _set_on_action, None,
        """A callable that is called when the action (whatever that means
        for the particluar Control) is issued.""")

    def _activate(self, *ignore):
        if self.onAction is not None:
            self.onAction()

    def skelargs(self):
        skelargs = super(Control, self).skelargs()
        value = self.value
        if is_simple(value):
            skelargs['value'] = value
        return skelargs
