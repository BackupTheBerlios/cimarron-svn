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

from papo import cimarron
from papo.cimarron.skins.common import XmlMixin

class ColumnAwareXmlMixin (object):
    def fromXmlObj(klass, xmlObj, skin):
        """
        Helper function for loading a Cimarrón app from an xml file. (see
        L{Controller.fromXmlFile}).
        """
        self = klass()
        self.fromXmlObjProps(xmlObj.properties)
        attrs= {self: klass.attributesToConnect ()}
        try:
            idDict= {self.id: self}
        except AttributeError:
            idDict= {}

        columns= []
        xmlObj = xmlObj.children
        while xmlObj:
            (obj, attrsInChild, idDictInChild)= self.childFromXmlObj (xmlObj, skin)
            if obj is not None:
                columns.append (obj)
                attrs.update (attrsInChild)
                # print `attrs`
                idDict.update (idDictInChild)
            xmlObj= xmlObj.next
        if columns:
            # warn (if not?)
            self.columns= columns

        return (self, attrs, idDict)
    fromXmlObj = classmethod(fromXmlObj)


class Column (XmlMixin):
    """
    A Column describes a field. This field can be used for both
    B{SearchEntry}s and B{Grid}s.
    """
    def attributesToConnect (klass):
        attrs= super (Column, klass).attributesToConnect ()
        return attrs+['read', 'write']
    attributesToConnect= classmethod (attributesToConnect)

    def __init__ (self, name='', read=None, write=None, entry=None):
        """
        @param name: A text associated with the field.
            In the case of B{Grids}, it's the colunm header.

        @param read: A callable that, given an object, returns the value
            of that object for the field. Tipically, is an unbound getter
            method from the object class.

        @param write: A callable that, given an object and a new value,
            modifies the object. Tipically, is an unbound setter method
            from the object class.
        """
        self.name= name
        if read is not None and not callable (read):
            raise ValueError, 'read parameter must be callable'
        self.read= read
        if write is not None and not callable (write):
            raise ValueError, 'write parameter must be callable'
        self.write= write
        if entry is None:
            entry = cimarron.skin.Entry
        self.entry= entry


