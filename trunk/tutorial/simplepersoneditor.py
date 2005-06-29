from fvl import cimarron
from simpleperson import Person
cimarron.config()

class PersonEditor(cimarron.skin.WindowController):
    def __init__(self, **kw):
        super(PersonEditor, self).__init__(**kw)
        self.win.title = 'Main Window'
        vbox = cimarron.skin.VBox(parent=self.win)
        hbox = cimarron.skin.HBox(parent=vbox)
        cimarron.skin.Label(parent=hbox, text='Name:')
        self.nameWidget = \
            cimarron.skin.Entry(parent=hbox, attribute="name")
        hbox = cimarron.skin.HBox(parent=vbox)
        cimarron.skin.Label(parent=hbox, text='Surname:')
        self.surnameWidget = \
            cimarron.skin.Entry(parent=hbox, attribute="surname")
        cimarron.skin.Button(parent=vbox, label='Check', 
	     onAction = self.checkValues)
        self.setTarget(self.target)

    def checkValues(self, sender):
       print "Mr/Ms %s, %s" % (self.target.surname, self.target.name)

    def setTarget(self, aPerson):
        self.target = aPerson
        self.nameWidget.newTarget(aPerson)
        self.surnameWidget.newTarget(aPerson)

    def getTarget(self):
        return self.target

app = cimarron.skin.Application()
w = PersonEditor(parent=app)
w.show()
w.setTarget(Person(name="John", surname="Doe"))
app.run()
