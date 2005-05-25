class Country (object):
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

    def setIso2 (self, iso2):
        self.iso2= iso2
    def getIso2 (self):
        return self.iso2

    def setIso3 (self, iso3):
        self.iso3= iso3

    def setUn (self, un):
        self.un= un

class State (object):
    def __init__ (self, name='', country=None):
        self.name= name
        self.country= country

    def setName (self, name):
        self.name= name

    def setCountry (self, country):
        self.country= country

class City (object):
    def __init__ (self, name='', state=None):
        self.name= name
        self.state= state

    def setName (self, name):
        self.name= name

    def setState (self, state):
        self.state= state
