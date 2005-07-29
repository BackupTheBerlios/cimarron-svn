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
    def __init__(self, street=None, city=None, country=None):
        self.street = street
        self.city = city
        self.country = country

Person.__values__ = [
    Person ("John", "Cleese",
            [Address(street="Ministry for Funny Walks",
                     city="London", country="UK")]),
    Person ("Michael", "Palin",
            [Address(street="Inquisition Headquarters",
                     city="Madrid", country="Spain")]),
    Person ("Eric", "Idle",
            [Address(street="Bruce Avenue",
                     city="Sydney", country="Australia")]),
    Person ("Graham", "Chapman",
            [Address(street="Stable Alley",
                     city="Bethlehem", country="Judea")]),
    Person ("Terry", "Jones",
            [Address(street="Suggestions?",
                     city="London", country="UK")]),
    Person ("Terry", "Gillian",
            [Address(street="Suggestions?",
                     city="London", country="UK")])
]
