from fvl import cimarron
from simpleperson import Person

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
        self.widgets = \
            (cimarron.skin.Entry(parent=vbox, attribute="name",
                                 onAction=self.checkValues),
             cimarron.skin.Entry(parent=vbox, attribute="surname",
                                 onAction=self.checkValues))
        cimarron.skin.Button(parent=outer_vbox, label='Check', 
	     onAction = self.checkValues)
        self.label = cimarron.skin.Label(parent=outer_vbox, text="")
        if target is not None:
            self.newTarget(target)

    def checkValues(self, sender=None):
        self.label.text = "Mr/Ms %s, %s" % \
                          (self.target.surname, self.target.name)

    def newTarget(self, target):
        super(PersonEditor, self).newTarget(target)
        for w in self.widgets:
            w.newTarget(self.value)
        self.checkValues(self)

app = cimarron.skin.Application()
w = PersonEditor(parent=app, target=Person(name="John", surname="Doe"))
w.show()
app.run()
