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
"""
Provides basic controllers.

L{fvl.cimarron.controllers.base} provides the root of all controllers,
L{Controller}, and the root of all controllers that handle a window,
L{WindowController}.
"""

__revision__ = int('$Rev$'[5:-1])

import os
import libxml2
import logging

from fvl.cimarron.tools import traverse
from fvl.cimarron.skins.common import Control, Container

logger = logging.getLogger('fvl.cimarron.controllers.base')

class Controller(Control, Container):
    """
    A Controller is the glue between a View and a Model,
    coordinating the reactions to the View's events to
    changes in the Model.
    """
    mainWidget = None # mainWidget is the "default" Control of the
                      # Controller, that which fires when you press
                      # enter.
    def __init__(self, **kwargs):
        super (Controller, self).__init__ (**kwargs)

    def fromXmlFile(cls, filename):
        """
        Load a Cimarrón Controller from an xml file.
        """
        if os.path.isfile(filename):
            root = libxml2.parseFile(filename).getRootElement()
            (self, attrs, idDict) = cls.fromXmlObj(root)
            self.idDict = idDict
            self._connect(attrs)
            return self
        else:
            raise OSError, "Unable to open file: %r" % filename
    fromXmlFile = classmethod(fromXmlFile)

    def childFromXmlObj(self, xmlObj):
        """
        Load a Cimarron object child from a libxml2 xmlNode
        """
        obj = (None, None, {})
        if xmlObj.name == 'import':
            obj = self.importFromXmlObj(xmlObj)
        else:
            obj = super(Controller, self).childFromXmlObj(xmlObj)
        return obj

    def importFromXmlObj(self, xmlObj):
        """
        Import a module using the description represented by the xmlNode
        """
        idDict = {}
        import_from = xmlObj.prop('from') or None
        import_what = xmlObj.prop('what') or None
        hasId = xmlObj.prop('id') or None

        if import_from is not None:
            obj = __import__(import_from, None, None, 'x')
            if import_what is not None:
                obj = getattr(obj, import_what)
        else:
            # raise KeyError?
            pass

        if hasId:
            idDict[hasId] = obj
        return (None, None, idDict)
        
    def _connect (self, attrs):
        for obj, attrs in attrs.items():
            for attr in attrs:
                path = None
                try:
                    path = getattr(obj, attr)
                except AttributeError:
                    # the info is not quite right
                    pass
                # print self.idDict
                # print `obj`, '.', `attr`, '=', `path`,
                if isinstance (path, basestring):
                    try:
                        (key, path)= path.split ('.', 1)
                        other = DelayedTraversal(self.idDict[key], path)
                        # print 'connected to DT', `self.idDict[key]`, path,
                    except ValueError:
                        # no path, directly the object
                        other = self.idDict[path]
                        # print 'connected to', `self.idDict[path]`,
                    setattr(obj, attr, other)
                # else:
                    # print 'connect impossible', 
                # print

class DelayedTraversal(object):
    """
    Encapsulate a traversal so that it can be done repeatedly at runtime,
    instead of just once at load time.
    """
    def __init__(self, other, path):
        self.path = path
        self.other = other
 
    def __call__(self, *args, **kwargs):
        return traverse (self.other, self.path)(*args, **kwargs)


class WindowController (Controller):
    """
    A WindowController just handles a Window.
    Is typical that each Window will have an associated Controller.
    Those Controllers must inherit from this class.
    """
    def __init__ (self, title='', size=(-1, -1), **kwargs):
        super(WindowController, self).__init__(**kwargs)
        from fvl.cimarron.skin import Window
        self.win = Window(parent=self, title=title, size=size)
        self.win.delegates.insert(0, self)

    def visibleChildren (self):
        """
        Return a list of visible children.
        """
        chld = self._children
        # print chld
        return [i for i in chld if getattr(i, 'visible', False) and i.visible]

    def will_hide (self, *ignore):
        """
        Window is trying to hide.
        """
        return self.delegate('will_hide')

    def show (self):
        """
        Show the window.
        """
        self.win.show ()

    def hide (self):
        """
        Hide the window.
        """
        self.win.hide ()

    def _get_visible (self):
        """
        Return whether the window is shown.
        """
        return len(self.visibleChildren ())>0
    visible = property (_get_visible, doc="Is the window shown?")

