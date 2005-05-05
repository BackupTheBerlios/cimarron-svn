class Address (object):
    def __init__ (self, text=''):
        self.text= text

    def getText (self):
        return self.__text
    def setText (self, text):
        self.__text= text
    text= property (getText, setText)

    def __str__ (self):
        return "Address (text='%s')" % self.text
