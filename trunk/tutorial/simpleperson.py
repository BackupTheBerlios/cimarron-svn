from fvl.cimarron.model import Model

class Person(Model):
    def __init__(self, name=None, surname=None):
        super(Person, self).__init__()
        self.name = name
        self.surname = surname
