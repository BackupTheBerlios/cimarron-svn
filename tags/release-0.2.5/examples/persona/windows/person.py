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

from papo import cimarron

from model.person import Person
from model.address import Address

import model.data.persons


__all__= (
    'AMBMPerson',
    )

class ABMPerson (cimarron.skin.WindowController):
    def __init__ (self, **kw):
        super (ABMPerson, self).__init__ (**kw)
        # take in account that this is fake
        self.data= model.data.persons.Persons
        self.win.title= 'ABM de Person'
        self.notebook= n= cimarron.skin.Notebook (parent= self.win)
        self.searchPage= PersonSearchPage (
            parent= n,
            data= self.data,
            onAction= self.personSelected,
            )
        self.editPage= PersonEditPage (
            parent= n,
            onAction= self.personAdded,
            )
        self.editAddressesPage= PersonAddressesEditPage (
            parent= n,
            )

    def personSelected (self, *ignore):
        self.editPage.value= self.searchPage.value
        if self.searchPage.value is not None:
            self.editAddressesPage.value= self.searchPage.value.addresses
            self.notebook.activate (self.editPage)

    def personAdded (self, *ignore):
        # NOTE: this is set up like this only because I won't implement
        # a model that can add itself to a transaction and commit
        self.data.append (self.editPage.value)
        print self.data


class PersonSearch (cimarron.skin.Search):
    def __init__ (self, data=[], **kw):
        super (PersonSearch, self).__init__ (**kw)
        self.data= data
        
    def search (self, values):
        name, surname= values[:2]
        ans= []

        for i in self.data:
            found= False
            if name is not None:
                found= name in i.name
            if surname is not None:
                found= found and surname in i.surname

            if found:
                ans.append (i)

        return ans


class PersonSearchPage (cimarron.skin.Controller):
    def __init__ (self, data=[], **kw):
        super (PersonSearchPage, self).__init__ (**kw)
        self.data= data
        v= cimarron.skin.VBox ()
        v.label= 'Search'
        # cimarron.skin.concreteParenter (parent=self, child=v)
        v.parent= self

        columns= (
            cimarron.skin.Column (name='Nombre', read=Person.getName, write=Person.setName),
            cimarron.skin.Column (name='Apellido', read=Person.getSurname, write=Person.setSurname),
            )
        self.searcher= PersonSearch (
            parent= v,
            columns= columns,
            onAction= self.personSelected,
            data= self.data,
            )

    def personSelected (self, *ignore):
        self.value= self.searcher.value
        self.searcher.value= None
        self.onAction ()

    def refresh (self, *ignore):
        pass


class PersonEditPage (cimarron.skin.Controller):
    def __init__ (self, **kw):
        super (PersonEditPage, self).__init__ (**kw)
        h= cimarron.skin.HBox ()
        h.label= 'Edit'
        h.parent= self

        new= cimarron.skin.Button (
            parent= h,
            label= 'New',
            onAction= self.newPerson,
            )
        
        v= cimarron.skin.VBox (parent=h)
        self.name= cimarron.skin.Entry (
            parent= v,
            onAction= self.editModel,
            )
        self.name.delegates.append (self)
        self.surname= cimarron.skin.Entry (
            parent= v,
            onAction= self.editModel,
            )
        self.surname.delegates.append (self)

        save= cimarron.skin.Button (
            parent= h,
            label= 'Save',
            onAction= self.savePerson,
            )

    def will_focus_out (self, *ignore):
        self.editModel ()

    def newPerson (self, *ignore):
        self.value= Person ()

    def savePerson (self, *ignore):
        if self.value.isDirty:
            if self.value.new:
                # NOTE: this is set up like this only because I won't implement
                # a model that can add itself to a transaction and commit
                self.onAction ()
            self.value.save ()
        
    def editModel (self, *ignore):
        if self.value is None:
            value= Person ()
            value.name= self.name.value
            value.surname= self.surname.value
            # we do it this way because doing `self.value= Person()´
            # would empty the Entry's values (due to refresh())
            self.value= value
        else:
            self.value.name= self.name.value
            self.value.surname= self.surname.value
        self.value.isDirty= True
        
    def refresh (self, *ignore):
        if self.value is not None:
            self.name.value= self.value.name
            self.surname.value= self.value.surname
        else:
            self.name.value= ''
            self.surname.value= ''

class PersonAddressesEditPage (cimarron.skin.Controller):
    def __init__ (self, **kw):
        super (PersonAddressesEditPage, self).__init__ (**kw)
        h= cimarron.skin.VBox ()
        h.label= 'Edit addresses'
        h.parent= self

        new= cimarron.skin.Button (
            parent= h,
            label= 'New',
            onAction= self.newAddress,
            )
        self.addresses= cimarron.skin.Grid (
            parent= h,
            columns= (cimarron.skin.Column (read=Address.getText, write=Address.setText), ),
            data= self.value,
            )

    def newAddress (self, *ignore):
        self.value.append (Address ())
        print self.value
        self.refresh ()

    def refresh (self):
        self.addresses.data= self.value
        # self.addresses.widget._widget.show_all ()
