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

class Person (object):
    def __init__ (self, name='', surname='', addresses= []):
        self.setName (name)
        self.setSurname (surname)
        self.addresses= addresses
        self.new= False
        if name=='' and surname=='' and addresses==[]:
            self.new= True
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
        self.isDirty= self.new= False

    def __str__ (self):
        return "Person (name='%s', surname='%s', addresses=%s)" % (
            self.name,
            self.surname,
            str (self.addresses),
            )
