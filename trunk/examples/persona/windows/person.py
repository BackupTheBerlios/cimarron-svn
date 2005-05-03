from papo import cimarron
from papo.cimarron.controllers import Controller, Column, WindowController

from model.person import Person

import model.data.persons

__all__= (
    'AMBMPerson',
    )

class PersonSearch (cimarron.controllers.Search):
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


class PersonSearchPage (Controller):
    def __init__ (self, data=[], **kw):
        super (PersonSearchPage, self).__init__ (**kw)
        self.data= data
        v= cimarron.skin.VBox ()
        v.label= 'Search'
        cimarron.skin.concreteParenter (parent=self, child=v)

        columns= (
            Column (name='Nombre', read=Person.getName, write=Person.setName),
            Column (name='Apellido', read=Person.getSurname, write=Person.setSurname),
            )
        self.searcher= PersonSearch (
            parent= v,
            columns= columns,
            onAction= self.personSelected,
            data= self.data,
            )

    def personSelected (self, *ignore):
        self.value= self.searcher.value
        self.onAction ()

    def refresh (self, *ignore):
        pass


class PersonEditPage (Controller):
    def __init__ (self, **kw):
        super (PersonEditPage, self).__init__ (**kw)
        h= cimarron.skin.VBox ()
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
        self.surname= cimarron.skin.Entry (
            parent= v,
            onAction= self.editModel,
            )

        save= cimarron.skin.Button (
            parent= h,
            label= 'Save',
            onAction= self.savePerson,
            )

    def newPerson (self, *ignore):
        self.value= Person ()

    def savePerson (self, *ignore):
        print 'saving', self.value
        if self.value.isDirty:
            if self.value.new:
                # NOTE: this is set up like this only because I won't implement
                # a model that can add itself to a transaction and commit
                self.onAction ()
            self.value.save ()
        
    def editModel (self, *ignore):
        self.value.name= self.name.value
        self.value.surname= self.surname.value
        self.value.isDirty= True
        
    def refresh (self, *ignore):
        if self.value is not None:
            self.name.value= self.value.name
            self.surname.value= self.value.surname


class ABMPerson (WindowController):
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

    def personSelected (self, *ignore):
        print self.searchPage.value
        self.editPage.value= self.searchPage.value
        self.notebook.activate (self.editPage)

    def personAdded (self, *ignore):
        # NOTE: this is set up like this only because I won't implement
        # a model that can add itself to a transaction and commit
        self.data.append (self.editPage.value)
        print self.data
