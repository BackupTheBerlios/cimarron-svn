

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

from Control import Control, _

class Grid(Control):
    __FIXME__=True
    def __init__(self, objectClass=None, objectConstructor=None):
        self._objectConstructor = objectConstructor
        self._objectClass = objectClass
        self._columns = []
        self._objDict = {}
        #diccionario de diccionarios de objetos.
        #primera llave Instancia. anidadas: genericas:{state} de gtk2:{iter}
        self._order = 0
        super(Grid, self).__init__()

    def addColumn(self, label=None, getter=None, printer='string', editable=False, parser=None, action=None, required=True, columnType='string'):    
        column = {}
        #llevar a gtk lo que sea de gtk
        column['label'] = label
        column['getter'] = getter
        column['printer'] = printer
        column['type'] = columnType
        column['editable'] = editable
        column['parser'] = parser
        column['action'] = action
        column['required'] = required
        self._columns.append(column)
      
    def makeView(self):
        scrolled = self._makeView()
        return scrolled

    def newRow(self):
        if self._objectConstructor:
            self._objectConstructor()
        else:
            rowObject=self._objectClass()
        self.addRow(rowObject,'new')    
    
    def addRow(self,rowObject,state="edited"):
        if self._objDict.has_key(rowObject):
            raise DuplicateObjectReference,\
                  _("Attempted to add a row twice")
        if self.delegate ('will_add_row', args=rowObject):
            self._objDict[rowObject] = {}
            self._objDict[rowObject]['state']=state
            self._addRow(rowObject)
            
    def getSelected(self):
        if self.delegate('will_get_selected'):
            return self._getSelected()
  
    def removeSelected(self):
        if self.delegate('will_remove_selected'):
            selected = self._removeSelected()
            return selected 
      
    def updateSelected(self):
        if self.delegate('will_update_selected'):
            self._updateSelected()
                  
    def select(self, instance):
        if self.delegate ('will_select',args=instance):
            self._select(instance)
     
    def updateAll(self):
        if self.delegate ('will_update_all'):
            self._updateAll()

    def setValue(self,list):
        if list and self.delegate ('will_set_value'):
            self._setValue(list)

    def getValue(self):
        if self.delegate ('will_get_value'):
            value = self._objDict.keys()
            return value
