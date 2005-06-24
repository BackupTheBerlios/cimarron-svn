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

from base import Model

class Person (Model):
    def __init__ (self, name='', surname='', addresses= []):
        self.setName (name)
        self.setSurname (surname)
        self.addresses= addresses
        self.isDirty= False
        
    def getName (self):
        return self.__name
    def setName (self, name):
        self.__name= name
        self.isDirty= True
    name= property (getName, setName)

    def getSurname (self):
        return self.__surname
    def setSurname (self, sn):
        self.__surname= sn
        self.isDirty= True
    surname= property (getSurname, setSurname)

    def getAddresses (self):
        return self.__addrs
    def setAddresses (self, addrs):
        self.__addrs= addrs
    def addToAddresses (self, addr):
        self.__addrs.append (addr)
        self.isDirty= True
    addresses= property (getAddresses, setAddresses)

    def save (self):
        self.isDirty= False

    def __str__ (self):
        return "Person (name='%s', surname='%s', addresses=%s)" % (
            self.name,
            self.surname,
            str (self.addresses),
            )

    def search (klass, values):
        name, surname= values[:2]
        ans= []

        for i in klass.__values__:
            found= False
            if surname is None and name is None:
                found= True
            else:
                if name is not None:
                    found= name in i.name
                if surname is not None:
                    if name is not None:
                        found= found and surname in i.surname
                    else:
                        found= surname in i.surname

            if found:
                ans.append (i)

        return ans
    search= classmethod (search)


class Address (Model):
    def __init__ (self, text=''):
        self.text= text
        self.isDirty= False

    def getText (self):
        return self.__text
    def setText (self, text):
        self.__text= text
        self.isDirty= True
    text= property (getText, setText)

    def __str__ (self):
        s= "Address (text='%s')" % self.text
        if self.isDirty:
            s= "* "+s
        return 


Person.__values__= [
    Person ("Freeman", "Newman", [Address (text="San luis 870"), Address (text="San luis 594 2D")]),
    Person ("Roxanne", "Oneal"),
    Person ("Ward", "Fischer"),
    Person ("Philis", "Eggbert"),
    Person ("September", "Gibson"),
    Person ("Layton", "Albright"),
    Person ("Janna", "Dimsdale"),
    Person ("Lexia", "Canham"),
    Person ("Jake", "Wickes"),
    Person ("Mona", "Prevatt"),
    Person ("Eugenia", "Sherlock"),
    Person ("Lynnette", "Briggs"),
    Person ("Adam", "Eisenman"),
    Person ("Lloyd", "Bash"),
    Person ("Ford", "Leslie"),
    Person ("Perce", "Bellinger"),
    Person ("Daly", "Ream"),
    Person ("Katy", "Mcfall"),
    Person ("Bryan", "Langston"),
    Person ("Kerena", "Rowe"),
    Person ("Elenora", "Moon"),
    Person ("Bindy", "Foster"),
    Person ("Toni", "Oppie"),
    Person ("Driskoll", "Patterson"),
    Person ("Roscoe", "Vanleer"),
    Person ("Deemer", "Barrett"),
    Person ("Dreda", "Siegrist"),
    Person ("Carlyn", "Nash"),
    Person ("Rexana", "Nehling"),
    Person ("Robyn", "Green"),
    Person ("Katelyn", "Fisher"),
    Person ("Jilly", "Kifer"),
    Person ("Reannon", "Craig"),
    Person ("Anima", "Ironmonger"),
    Person ("Willie", "Reese"),
    Person ("Jemima", "Schrader"),
    Person ("Ernie", "Stoddard"),
    Person ("Judd", "Mcclymonds"),
    Person ("Aaren", "Smith"),
    Person ("Jonny", "Merryman"),
    Person ("Sam", "Blaine"),
    Person ("Hugh", "Zimmer"),
    Person ("Kaylin", "Blessig"),
    Person ("Earline", "Alliman"),
    Person ("Barret", "Rifler"),
    Person ("Hall", "Burnett"),
    Person ("Avila", "Park"),
    Person ("Ronnette", "Lalty"),
    Person ("Lou", "Day"),
    Person ("Bessie", "Robinson"),
]
