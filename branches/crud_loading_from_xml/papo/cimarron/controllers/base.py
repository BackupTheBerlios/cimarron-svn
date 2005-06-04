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

import os

from papo import cimarron
from papo.cimarron.tools import traverse
from papo.cimarron.skins.common import Control, Container

class Controller(Control, Container):
    """
    A Controller is the glue between a View and a Model,
    coordinating the reactions to the View's events to
    changes in the Model.
    """
    mainWidget = None # mainWidget is the "default" Control of the
                      # Controller, that which fires when you press
                      # enter.
    def __init__(self, **kw):
        self.__initialized = False
        super (Controller, self).__init__ (**kw)
        self.__initialized = True

    def _set_value(self, value):
        self.__value=value
        if self.__initialized:
            self.refresh()
    def _get_value(self):
        return self.__value
    value = property(_get_value, _set_value, doc="""Holds the Model for the B{Controller}.
        Note that the name is the same that the I{value} for B{Control}.
        That way, Controllers can act as Controls.""")

    def fromXmlFile(klass, filename):
        """
        Load a Cimarrón Controller from an xml file.
        """
        if os.path.isfile(filename):
            return klass.fromXmlObj(libxml2.parseFile(filename).getRootElement (),
                                    cimarron.skin)[0]
        else:
            raise OSError, "Unable to open file: %r" % filename
    fromXmlFile = classmethod(fromXmlFile)

    def fromXmlObj (klass, xmlObj, skin):
        (net, toConnect)= super (Controller, klass).fromXmlObj (xmlObj, skin)
        toConnect= net._connect (toConnect)
        
        return (net, toConnect)
    fromXmlObj = classmethod(fromXmlObj)
    
    def childFromXmlObj (self, xmlObj, skin):
        """
        Load a Cimarron object child from a libxml2 xmlNode
        """
        obj= (None, None)
        if xmlObj.name=='import':
            self.importFromXmlObj (xmlObj)
        else:
            obj= super (Controller, self).childFromXmlObj (xmlObj, skin)
        return obj

    def importFromXmlObj (self, xmlObj):
        """
        Import a module using the description represented by the xmlNode
        """
        import_from, import_what= None, None
        
        prop= xmlObj.properties
        while prop:
            if prop.name=='from':
                import_from= prop.content
            elif prop.name=='what':
                import_what= prop.content
            else:
                # raise KeyError?
                pass
            prop= prop.next

        if import_from is not None:
            module= __import__ (import_from, None, None, True)
            
            if import_what is not None:
                setattr (self, import_what, getattr (module, import_what))
            else:
                setattr (self, import_from, module)
        else:
            # raise KeyError?
            pass
        print self, import_from, import_what
        
    def _connect (self, toConnect):
        stillToConnect= {}
        for obj, attrs in toConnect.items ():
            for attr in attrs:
                # print 'connecting', obj, attr,
                try:
                    # connect
                    path= getattr (obj, attr)
                    # print path, ':',
                    other= traverse (self, path)
                    setattr (obj, attr, other)
                    # print self, 'done'
                except AttributeError:
                    # I can't find it; (hopefully) it will be resolved later
                    try:
                        stillToConnect[obj].append (attr)
                    except KeyError:
                        stillToConnect[obj]= [attr]
                    # print 'not yet'
        return stillToConnect


class WindowController (Controller):
    """
    A WindowController just handles a Window.
    Is typical that each Window will have an associated Controller.
    Those Controllers must inherit from this class.
    """
    def __init__ (self, **kw):
        super (WindowController, self).__init__ (**kw)
        self.win= cimarron.skin.Window (parent= self)
        self.win.delegates.insert (0, self)

    def visibleChildren (self):
        chld= self._children
        # print chld
        return [i for i in chld if getattr (i, 'visible', False) and i.visible]

    def will_hide (self, *ignore):
        return self.delegate ('will_hide')

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
        return len(self.visibleChildren ())>0
    visible= property (_get_visible, None, None,
        """Is the window shown?""")

