class Person(object):
    def __init__(self, name=None, surname=None):
        super(Person, self).__init__()
        self.set_name(name)
        self.set_surname(surname)

    def set_name(self, name):
        self._name = name
    def get_name(self):
        return self._name
    name = property(get_name, set_name, None,
                    """The person's given name""")

    def set_surname(self, surname):
        self._surname = surname
    def get_surname(self):
        return self._surname
    surname = property(get_surname, set_surname, None,
                       """The person's family name""")
