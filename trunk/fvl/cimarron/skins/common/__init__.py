# -*- coding: utf-8 -*-
#
# Copyright 2003, 2004, 2005 Fundación Via Libre
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

L{skins.common} is a set of abstract classes that
are the foundation of Cimarrón's class hierarchy.

"""

__revision__ = int('$Rev$'[5:-1])

from new import instancemethod
import operator
import logging

import libxml2
from zope import interface

from fvl.cimarron.tools import traverse
from fvl.cimarron.interfaces import IModel
from fvl import cimarron

__all__ = ('XmlMixin', 'Widget', 'Container', 'Control',
           'ForcedNo', 'No', 'Unknown', 'Yes', 'ForcedYes')

logger = logging.getLogger('fvl.cimarron.skins.common')

def nullAction(*dummy, **ignore):
    """
    An action that does nothing. Kinda like 'C{pass}'.
    """

class DelegationAnswer(int):
    """
    Singleton-like class of the possible answers from a delegation query.

    It's singleton-like because it has five possible values, and is a singleton
    on each of those. Call it a pentalton if you will.

    The five possible values are: Unknown, Yes, No, ForcedYes, ForcedNo.

    You can operate on L{DelegationAnswer}s, according to their own rules:

    FIXME: show the result of addition

    Also,

    FIXME: show the effect of __nonzero__.

    """
    truthTable = (('Unknown', 'Yes', 'No'),
                  ('Yes', 'Yes', 'Yes'),
                  ('No', 'Yes', 'No'))
    def __new__(cls, name):
        try:
            try:
                return cls.__instances[name]
            except AttributeError:
                instances = {}
                for key, value in dict(ForcedNo=-5, No=-1,
                                       Unknown=0, Yes=1, ForcedYes=5).items():
                    value = super(DelegationAnswer, cls).__new__(cls, value)
                    value.name = key
                    instances[key] = value
                cls.__instances = instances
                return instances[name]
        except KeyError:
            raise ValueError, \
                  'invalid literal for DelegationAnswer(): %s' % name
    def __add__(self, other):
        return DelegationAnswer(self.truthTable[self][other])
    def __nonzero__(self):
        return self >= 0
    def __repr__(self):
        return "%s(%r)" % (self.__class__.__name__, self.name)

# create the five DelegationAnswer objects.
ForcedNo, No, Unknown, Yes, ForcedYes = map(DelegationAnswer,
                             ('ForcedNo', 'No', 'Unknown', 'Yes', 'ForcedYes'))

class XmlMixin (object):
    """
    Mixin for L{Widget}s that want to be able to deserialize themselves from XML.
    """
    def attributesToConnect (cls):
        """
        Return the list of attributes that a serialized object might have,
        and that would need resolving via delayed traversal.
        """
        return []
    attributesToConnect = classmethod (attributesToConnect)
    
    def fromXmlObj(cls, xmlObj, skin):
        """
        Helper function for loading a Cimarrón app from an xml file. (see
        L{Controller.fromXmlFile<cimarron.controllers.base.Controller.fromXmlFile>}).
        """
        self = cls()
        self.fromXmlObjProps(xmlObj.properties)
        attrs = {self: cls.attributesToConnect()}
        try:
            idDict = {self.id: self}
        except AttributeError:
            idDict = {}
        
        xmlObj = xmlObj.children
        while xmlObj:
            (obj, attrsInChild, idDictInChild) = \
                  self.childFromXmlObj(xmlObj, skin)
            if obj is not None:
                obj.parent = self
                attrs.update (attrsInChild)
            idDict.update (idDictInChild)
            xmlObj = xmlObj.next
        
        return (self, attrs, idDict)
    fromXmlObj = classmethod(fromXmlObj)
        
    def childFromXmlObj (self, xmlObj, skin):
        """
        Load a Cimarrón object child from a libxml2 xmlNode
        """
        obj = (None, None, {})
        if xmlObj.type == 'element':
            obj = getattr(skin, xmlObj.name).fromXmlObj(xmlObj, skin)
        return obj

    def fromXmlObjProp(self, prop):
        """
        Set an attribute from an xml2 property object.
        """
        setattr(self, prop.name, prop.content)

    def fromXmlObjProps(self, prop):
        """
        Set the attributes from an xml2 properties object.
        """
        while prop:
            self.fromXmlObjProp(prop)
            prop = prop.next
        

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


class Widget(XmlMixin):
    """
    L{Widget}s are everything that the user sees of an L{Application
    <fvl.cimarron.controllers.Application>}.
    """

    def __init__(self, parent=None, expand=True, fill=True, border=0, **kwargs):
        """
        @param parent: the parent of the widget (you don't say!)
        @type parent: L{Widget}
        """
        super (Widget, self).__init__ (**kwargs)
        self.delegates = []
        self.expand = expand
        self.fill = fill
        self.border = border
        self.parent = parent
        for key, value in kwargs.items ():
            setattr (self, key, value)

    def _set_parent(self, parent):
        """
        Hook up this L{Widget} to its parent.

        FIXME: explain all the corner cases.
        """
        if parent is not None and self.parent is parent:
            raise ValueError, 'Child already in parent'
        if self.parent is not None:
            if parent is None:
                raise NotImplementedError, 'Cannot deparent'
            else:
                raise NotImplementedError, 'Cannot reparent'
        if parent is not None:
            parent._concreteParenter(self)
            parent._children.append(self)
        self.__parent = parent

        # re-link missed parentizations
        try:
            for child in self._childrenToParent:
                self._concreteParenter (child)
            del self._childrenToParent
        except AttributeError:
            # no dangling children, ignore
            pass
            
    def _get_parent(self):
        """
        Get the L{Widget}'s parent, or None.
        """
        try:
            return self.__parent
        except AttributeError:
            # only happens during init
            return None
    parent = property(_get_parent, _set_parent,
                      doc="parent is either the containing L{Widget}, or None")

    def _get_skin (self):
        """
        Get the L{Widget}'s skin.

        FIXME: This is the same as importing skin from fvl.cimarron.
        """
        try:
            return self.__skin
        except AttributeError:
            from fvl.cimarron import skin
            self.__skin = skin
            return skin
    skin = property(_get_skin,
                    doc="the skin")

    def delegate(self, message, *args):
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
        if self.delegates:
            answer = Unknown
            for i in self.delegates:
                answer_i = getattr(i, message, lambda *a: Unknown)(self, *args)
                try:
                    if answer_i is not None:
                        answer = answer + answer_i
                except IndexError:
                    # an IndexError on addition means answer_i is one of the
                    # Forced values.
                    # FIXME: this is totally unexpected
                    answer = answer_i
                    break
            return answer
        return True

    def _concreteParenter (self, child):
        """
        Does the skin-specific magic that `glues' a child with its parent.
        Do not call directly.
        """
        cimarron.skin._concreteParenter(self, child)

    def _connectWith (self, other):
        """
        Connects the widget with someone else. This is used for loading
        from XML files/objects.
        """
        pass


class Container(Widget):
    """
    An object that can contain (a list of) other objects
    (called its `children').
    """
    def __init__(self, **kwargs):
        super(Container, self).__init__(**kwargs)
        self._children = []

    def show(self):
        """
        Show the object and all its sub-objects.
        """
        for i in self.children:
            i.show()

    def hide(self):
        """
        Hide the object and all its sub-objects.
        """
        for i in self.children:
            i.hide()

    def _get_children(self):
        """
        Return the L{Container}'s children.
        """
        return tuple(self._children)
    children = property(_get_children)

    def skeleton(self, parent=None):
        """
        See L{Widget.skeleton}
        """
        skel = super(Container, self).skeleton(parent)
        for child in self.children:
            child.skeleton(skel)
        return skel

    def dirty(self):
        """
        Is the L{Container} dirty? I.e., are any of its children dirty?
        """
        for i in self.children:
            if i.dirty():
                return True
        return False

class _placeholder(object):
    """A distinctive placeholder object"""

class Control(Widget):
    """
    L{Control} is a Widget that can be interacted with. L{Control}s
    have an action, that is a callback that is called when a
    L{Control}-specific event happens. For example,
    L{Button<gtk2.Button>}s fire the action when you press or click
    them, whereas L{Entry<gtk2.Entry>}s do so when they have focus
    and enter is pressed, or they lose focus.
    """
    def attributesToConnect (cls):
        """
        See L{XmlMixin.attributesToConnect}
        """
        attrs = super (Control, cls).attributesToConnect ()
        return attrs+['onAction']
    attributesToConnect = classmethod(attributesToConnect)

    def __init__(self, onAction=None, target=None, attribute=None, value=None,
                 **kwargs):
        super(Control, self).__init__(**kwargs)
        self.target = target
        self.attribute = attribute
        self.value = value
        self.onAction = onAction

    def _targetValue(self):
        """
        Get the value from the target.
        """
        value = self.target
        if self.target is not None and self.attribute is not None \
               and IModel in interface.providedBy(self.target):
            value = self.target.getattr(self.attribute)
        return value

    def refresh(self):
        """
        Set the L{Control}'s value from its target.

        It also must display this change in the UI, so that's why it is
        commonly overriden.
        """
        self.value = self._targetValue()

    def newTarget (self, target=_placeholder):
        """
        Called when we need to propagate a change elsewere to the value.

        You I{must} call L{newTarget} when you have finished setting
        up a L{Control}, so that target/attribute/value are in sync.

        No, we can't do it automatically: we don't know when you've
        finished setting up the L{Control}.
        """
        if target is not _placeholder:
            self.target = target
        self.refresh()

    def commitValue (self, value=_placeholder):
        """
        Called when we need to propagate a change value to the target.
        """
        if value is not _placeholder:
            self.value = value
        if self.attribute is not None and self.target is not None:
            self.target.setattr(self.attribute, self.value)
        else:
            self.target = self.value
        
    def _get_on_action (self):
        """
        Get the onAction callback.
        """
        return self.__on_action
    def _set_on_action (self, onAction):
        """
        Set the onAction callback.

        FIXME: explain the corner cases.
        """
        if onAction is None:
            onAction = nullAction
        if type (onAction)==str:
            # let the xml loader set str onAction's
            self.__on_action = onAction
        else:
            # default behaviour
            self.__on_action = instancemethod(onAction, self, Control)
    onAction = property(_get_on_action, _set_on_action, doc=\
                         "A callable that is called when the action"
                         " (whatever that means for the particluar Control) "
                         "is issued.")

    def _activate(self, widget=None):
        """
        The user activated the L{Control}. In other words, she hit enter, or
        double-clicked it, or selected it, or whatever action means a
        yes-I-mean-this-one.
        """
        if self.delegate('will_activate'):
            self.commitValue()
            if self.onAction is not None:
                self.onAction()

    def skelargs(self):
        """
        See L{XmlMixin.skelargs}
        """
        skelargs = super(Control, self).skelargs()
        value = self.value
        if is_simple(value):
            skelargs['value'] = value
        return skelargs
