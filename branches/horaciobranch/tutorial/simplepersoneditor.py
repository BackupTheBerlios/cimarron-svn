from fvl import cimarron
from simpleperson import Person
cimarron.config()

class PersonEditor(cimarron.skin.WindowController):
    def __init__(self, target=None, **kw):
        super(PersonEditor, self).__init__(**kw)
        self.win.title = 'Person Editor'
        outer_vbox = cimarron.skin.VBox(parent=self.win)
        hbox = cimarron.skin.HBox(parent=outer_vbox)
        vbox = cimarron.skin.VBox(parent=hbox)
        cimarron.skin.Label(parent=vbox, text='Name:')
        cimarron.skin.Label(parent=vbox, text='Surname:')
        vbox = cimarron.skin.VBox(parent=hbox)
        self.nameWidget = \
            cimarron.skin.Entry(parent=vbox, attribute="name")
        self.surnameWidget = \
            cimarron.skin.Entry(parent=vbox, attribute="surname")
        cimarron.skin.Button(parent=outer_vbox, label='Check', 
	     onAction = self.checkValues)
        if target is not None:
            self.newTarget(target)

    def checkValues(self, sender):
        print "Mr/Ms %s, %s" % (self.target.surname, self.target.name)

    def newTarget(self, *a, **kw):
        super(PersonEditor, self).newTarget(*a, **kw)
        self.nameWidget.newTarget(self.target)
        self.surnameWidget.newTarget(self.target)

    def refresh(self):
        self.nameWidget.refresh()
        self.surnameWidget.refresh()

app = cimarron.skin.Application()
w = PersonEditor(parent=app, target=Person(name="John", surname="Doe"))
w.show()
app.run()
