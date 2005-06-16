from papo import cimarron
from simpleperson import Person
cimarron.config()

class PersonEditor(cimarron.skin.WindowController):
    def __init__(self, **kw):
        super(PersonEditor, self).__init__(**kw)
        self.win.title = 'Main Window'
        vbox = cimarron.skin.VBox(parent=self.win)
        hbox = cimarron.skin.HBox(parent=vbox)
        cimarron.skin.Label(parent=hbox, label='Name:')
        self.nameWidget = \
            cimarron.skin.Entry(parent=hbox, attribute="name")
        hbox = cimarron.skin.HBox(parent=vbox)
        cimarron.skin.Label(parent=hbox, label='Surname:')
        self.surnameWidget = \
            cimarron.skin.Entry(parent=hbox, attribute="surname")
        cimarron.skin.Button(parent=vbox, label='Check',
            onAction = self.checkValues)
        self.target = None

    def checkValues(self, sender):
        print "Mr/Ms %s, %s" % self.target.surname, self.target.name

    def setTarget(self, aPerson):
        self._target = aPerson
        self.nameWidget.target = aPerson
        self.surnameWidget.target = aPerson

    def getTarget(self):
        return self._target

    target = property(get_target, set_target, None,
                       """The person we're editing""")
    
app = cimarron.skin.App()
w = PersonEditor(parent=app)
w.show()
w.setTarget(Person(name="John", surname="Doe"))
app.run()
