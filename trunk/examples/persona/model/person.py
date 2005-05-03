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
