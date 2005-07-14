from fvl.cimarron.model import Model

class Person(Model):
    def __init__(self, name=None, surname=None, addresses=None):
        super(Person, self).__init__()
        self.name = name
        self.surname = surname
        if addresses is None:
            self.addresses = []
        else:
            self.addresses = addresses

class Address(Model):
    def __init__(self, street=None, zipcode=None, city=None, country=None):
        self.street = street
        self.zipcode = zipcode
        self.city = city
        self.country = country
        self.isDirty= False

    def setattr(self, attr, value):
        super(Address, self).setattr(attr, value)
        self.isDirty= True
