from fvl import cimarron
from fvl.cimarron.model import Model

from model.person import Person

class Row(Model):
    def __init__(self, a='more', person=None, b='less'):
        self.person= person
        self.a= a
        self.b= b

a= cimarron.skin.Application()
w= cimarron.skin.Window(parent= a)

seColumns= (cimarron.skin.Column(attribute='name'),
            cimarron.skin.Column(attribute='surname'),)
gColumns= (cimarron.skin.Column(name='A', attribute= 'a'),
           cimarron.skin.Column(name='B1', attribute= 'b'),
           cimarron.skin.Column(name='Person',
                                attribute='person',
                                entry= cimarron.skin.SearchEntry,
                                columns= seColumns,
                                cls= Person,
                                searcher= Person,
                                ),
           cimarron.skin.Column(name='B2', attribute= 'b'),
           )

data= [Row(person= Person(name= 'Marcos', surname='Dione')),
       Row(person= Person(name= 'Fer', surname= 'Simes')),
       Row(person= Person(name= 'John', surname= 'Lenton')),
       Row(person= Person(name= 'Fede', surname= 'Heinz')),
       ]

g= cimarron.skin.Grid(parent= w,
                      columns= gColumns,
                      value= data,
                      )

w.show()
a.run()
