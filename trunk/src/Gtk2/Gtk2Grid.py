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

import gtk , gobject
from Generic.Grid import Grid
from Gtk2Control import Gtk2Control
from Generic.Exceptions import DuplicateObjectReference

#def printSignalParameters(renderer, iter, data, model):
#    print renderer, iter, data, model

class Gtk2Grid(Grid, Gtk2Control):
        
    def __init__(self, showClass=None):
        self._types = {'string':
              {'gobjectType':gobject.TYPE_STRING,
               'renderer':gtk.CellRendererText,
               'editable_parameter':"editable",
               'index_parameter':'text',
               'signal':"edited",
               'signal_action':self._editedAction},
              'bool':
              {'gobjectType':gobject.TYPE_BOOLEAN,
               'renderer':gtk.CellRendererToggle,
               'editable_parameter':"activatable",
               'index_parameter':'active',
               'signal':"toggled",
               'signal_action':self._toggledAction}}
        
        self._view = None
        self._rendDict = {}
        self._scrolled = None
        super (Gtk2Grid, self).__init__(showClass)
        
    def _makeModel(self):
        self._model = gtk.TreeStore(gobject.TYPE_PYOBJECT, *[self._types[col['type']]['gobjectType'] for col in self._columns])
    def _makeView(self):
        #da vida al modelo
        self._makeModel()
        textNumber=0
        view = gtk.TreeView(self._model)
        for col in self._columns:
            textNumber+=1
            renderer=self._types[col['type']]['renderer']()
            #armo el diccionario de renderers, prque las señales de gtk2 me
            #indican la instancia de render y no la columna que estoy editando.
            #este diccionario lo uso para saber que columna estoy editando
            self._rendDict[renderer]=col
            #si es editable, le habilito la propiedad correspondiente segun el renderer.
            if col['editable']:
                renderer.set_property(self._types[col['type']]['editable_parameter'], True)
                #conecto la senal de edicion con el metodo a utilizar segun diccionario "_types".
                renderer.connect(self._types[col['type']]['signal'],self._types[col['type']]['signal_action'], self._model)    
            index={}
            index[self._types[col['type']]['index_parameter']]=textNumber
            #es feo pero el indice en gtk2 tiene un nombre distinto en cada renderer
            #la linea precedente se encarga de buscar el nombre del indice en el diccionario de tipos
            #de datos a mostrar.
            column=gtk.TreeViewColumn(col['label'], renderer,**index)
            view.append_column(column)
        view.show()
        # Create scrollbars around the view.
        scrolled = gtk.ScrolledWindow()
        scrolled.add(view)
        scrolled.show()
        self._view = view
        self._scrolled = scrolled
        self._obj = scrolled
        #primer campo editable
        self.newRow()
        return scrolled

    ### METODOS A CONECTAR CON LAS SENALES DE LOS RENDERS DE GTK2
    def _editedAction (self, rendererInstance, iter, data, model):   
        #print rendererInstance, iter, data, model
        #print "column values :",self._rendDict[rendererInstance]
        #aca llamar al parser
        if self._rendDict[rendererInstance]['parser']:
            parsedData=self._rendDict[rendererInstance]['parser'](data)
        else:
            parsedData=data
        #el objeto de la fila editada
        obj=self._getSelected()
        #llamo al action de la columna, con el valor del dato editado y parsado 
        self._rendDict[rendererInstance]['action'](obj,parsedData)
        self._updateSelected()
        print "obj,data", obj, data
        
    def _toggledAction (self,rendererInstance, iter,data):
        obj=self._getSelected()
        self._rendDict[rendererInstance]['action'](obj,data)
        self._updateSelected()
        print "toogle_obj,data", rendererInstance, iter,data 

    def _updateRow(self,iter):
        textNumber=0
        rowObject=self._model.get_value(iter , 0)
        #solo si el objeto no es nulo
        complete=True

        #saque este if porque nunca puede haber un row sin objeto
        #if rowObject:
        for col in self._columns:
                textNumber+=1
                showValue=col['getter'](rowObject)
                self._model.set_value(iter, textNumber, showValue)
                #reviso si los required estan completos        
                if col['required'] and not showValue:
                   complete=False
                 
        #reviso el estado de cada row:
        state=self._objDict[rowObject]['state']
        print "state", state ,"complete", complete
        
        if state == "incomplete" and complete:
            self._objDict[rowObject]['state']="edited"
        if state == "new" and complete:
            self._objDict[rowObject]['state']="edited"         
            self.newRow()
        if state == "edited" and not complete:
            self._objDict[rowObject]['state']="incomplete"      

    def _addRow(self,rowObject):
        iter = self._model.insert_before(None, None)
        self._objDict[rowObject]['iter'] = iter
        self._model.set_value(iter, 0, rowObject)
        self._updateRow(iter)

    def _getIter(self):    
        model, iter = self._view.get_selection().get_selected()
        return iter

    def _getSelected(self):
        iter = self._getIter()
        selected = None
        if iter:
            selected = self._model.get_value(iter , 0)
        return selected 
           
    def _removeSelected(self):
        iter = self._getIter()
        selected = None
        if iter: 
            selected = self._model.get_value(iter , 0)
            if self._objDict[selected]['state'] == "new":
                self.newRow()
            del self._objDict[selected]
            self._model.remove(iter)
        return selected
       
    def _updateSelected(self):
        iter = self._getIter()
        if iter:
            self._updateRow(iter)
        
    def _select(self, instance):
        iter = self._objDict[instance]['iter']
        if iter:
            self._view.get_selection().select_iter(iter)   
        
    def _updateAll(self):
        for iter in self._objDict.values():
            self._updateRow(iter)
            
    def _getValue(self):
        pass 

    def _setValue(self,list):
        ####hay que repartir este codigo entre gtk2 y generic
        for iter in self._objDict.values()['iter']:
            self._model.remove(iter)
        self._objDict = {}
        for rowObject in list:
            self.addRow(rowObject)
        self.updateAll
    
    
    
