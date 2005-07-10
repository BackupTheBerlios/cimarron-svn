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

from fvl.cimarron.model import Model

class Country (Model):
    def __init__ (self, name='', phone='', iso2='', iso3='', un=''):
        self.name= name
        self.phone= phone
        self.iso2= iso2
        self.iso3= iso3
        self.un= un

    def setName (self, name):
        self.name= name
    def getName (self):
        return self.name

    def setPhone (self, phone):
        self.phone= phone
    def getPhone (self):
        return self.phone

    def setIso2 (self, iso2):
        self.iso2= iso2
    def getIso2 (self):
        return self.iso2

    def setIso3 (self, iso3):
        self.iso3= iso3
    def getIso3 (self):
        return self.iso3

    def setUn (self, un):
        self.un= un
    def getUn (self):
        return self.un

    def search (klass, values):
        # this is what I don't want: the search alg is tied
        # to what-the-screen needs. that sucks. may be, now
        # that we have (almost) fields in Entries and Searches,
        # we can just pass a dict around and figure it out here
        iso2, name= values[:2]
        ans= []

        for i in klass.__values__:
            found= False

            if iso2 is None and name is None:
                found= True
            else:
                if name is not None:
                    found= name in i.name
                if iso2 is not None:
                    if name is not None:
                        found= found and iso2==i.iso2
                    else:
                        found= iso2==i.iso2

            if found:
                ans.append (i)

        return ans
    search= classmethod (search)

    def __str__ (self):
        return 'Country name: '+self.name


class State (Model):
    def __init__ (self, name='', country=None):
        self.name= name
        self.country= country

    def setName (self, name):
        self.name= name
    def getName (self):
        return self.name

    def setCountry (self, country):
        self.country= country
    def getCountry (self):
        return self.country

    def search (klass, values):
        name= values[0]
        ans= []

        for i in klass.__values__:
            found= False
            if name is not None:
                found= name in i.name

            if found:
                ans.append (i)

        return ans
    search= classmethod (search)

    def __str__ (self):
        return 'State name: '+ self.name+', Country: '+str (self.country)


class City (Model):
    def __init__ (self, name='', state=None):
        self.name= name
        self.state= state

    def setName (self, name):
        self.name= name

    def setState (self, state):
        self.state= state


Country.__values__= [
    Country (name="Argentina", phone="54", iso2="ar"),
    Country (name="Uruguay", phone="598", iso2="uy"),
    ]

State.__values__= [
    State (name="Jujuy", country=Country.__values__[0]),
    State (name="Salta", country=Country.__values__[0]),
    State (name="Catamarca", country=Country.__values__[0]),
    State (name="La Rioja (/me grabs)", country=Country.__values__[0]),
    State (name="San Juan", country=Country.__values__[0]),
    State (name="Mendoza", country=Country.__values__[0]),
    State (name="Neuquen", country=Country.__values__[0]),
    State (name="Rio Negro", country=Country.__values__[0]),
    State (name="Chubut", country=Country.__values__[0]),
    State (name="Santa Cruz", country=Country.__values__[0]),
    State (name="Tierra Del Fuego y demase", country=Country.__values__[0]),
    State (name="La Pampa", country=Country.__values__[0]),
    State (name="San Luis", country=Country.__values__[0]),
    State (name="Cordoba", country=Country.__values__[0]),
    State (name="Santiago Del Estero", country=Country.__values__[0]),
    State (name="Tucuman", country=Country.__values__[0]),
    State (name="Chaco", country=Country.__values__[0]),
    State (name="Formosa", country=Country.__values__[0]),
    State (name="Misiones", country=Country.__values__[0]),
    State (name="Corrientes", country=Country.__values__[0]),
    State (name="Entre Rios", country=Country.__values__[0]),
    State (name="Santa Fe", country=Country.__values__[0]),
    State (name="Buenos Aires", country=Country.__values__[0]),
    State (name="Capital Federal", country=Country.__values__[0]),

    State (name="Artigas", country=Country.__values__[1]),
    State (name="Canelones", country=Country.__values__[1]),
    State (name="Cerro Largo", country=Country.__values__[1]),
    State (name="Colonia", country=Country.__values__[1]),
    State (name="Durazno", country=Country.__values__[1]),
    State (name="Flores", country=Country.__values__[1]),
    State (name="Florida", country=Country.__values__[1]),
    State (name="Lavalleja", country=Country.__values__[1]),
    State (name="Maldonado", country=Country.__values__[1]),
    State (name="Montevideo", country=Country.__values__[1]),
    State (name="Paysandu", country=Country.__values__[1]),
    State (name="Rio Negro", country=Country.__values__[1]),
    State (name="Rivera", country=Country.__values__[1]),
    State (name="Rocha", country=Country.__values__[1]),
    State (name="Salto", country=Country.__values__[1]),
    State (name="San Jose", country=Country.__values__[1]),
    State (name="Soriano", country=Country.__values__[1]),
    State (name="Tacuarembo", country=Country.__values__[1]),
    State (name="Treinta Y Tres", country=Country.__values__[1]),
    ]
