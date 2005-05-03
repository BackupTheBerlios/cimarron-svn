class Address (object):
    def __init__ (self, text=''):
        self.text= text

    def __get_text (self):
        return self.__text
    def __set_text (self, text):
        self.__text= text
    text= property (__get_text, __set_text)

    def __str__ (self):
        return "Address (text='%s')" % self.text
