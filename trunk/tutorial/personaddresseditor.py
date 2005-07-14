from fvl import cimarron
from model import Person, Address
cimarron.config()

class PersonAddressEditor(cimarron.skin.WindowController):
    def __init__(self, target=None, **kw):
        super(PersonAddressEditor, self).__init__(**kw)
        self.win.title = 'Person Editor'
        outer_vbox = cimarron.skin.VBox(parent=self.win)
        hbox = cimarron.skin.HBox(parent=outer_vbox)
        vbox = cimarron.skin.VBox(parent=hbox)
        cimarron.skin.Label(parent=vbox, text='Name:')
        cimarron.skin.Label(parent=vbox, text='Surname:')
        vbox = cimarron.skin.VBox(parent=hbox)
        gridColumns = (cimarron.skin.Column(name="Street", attribute="street"),
                       cimarron.skin.Column(name="Zip Code", attribute="zipcode"),
                       cimarron.skin.Column(name="City", attribute="city"),
                       cimarron.skin.Column(name="Country", attribute="country"))
        self.widgets = \
            (cimarron.skin.Entry(parent=vbox, attribute="name",
                                 onAction=self.checkValues),
             cimarron.skin.Entry(parent=vbox, attribute="surname",
                                 onAction=self.checkValues),
             cimarron.skin.Grid(parent=outer_vbox, cls=Address,
                                attribute="addresses", columns=gridColumns))
        cimarron.skin.Button(parent=outer_vbox, label='Check', 
	     onAction = self.checkValues)
        self.label = cimarron.skin.Label(parent=outer_vbox, text="")
        if target is not None:
            self.newTarget(target)

    def checkValues(self, sender=None):
        self.label.text = "Mr/Ms %s, %s" % \
                          (self.target.surname, self.target.name)

    def newTarget(self, target=None):
        super(PersonAddressEditor, self).newTarget(target)
        for w in self.widgets:
            w.newTarget(self.value)
        self.checkValues(self)

app = cimarron.skin.Application()
p = Person(name="John", surname="Doe",
           addresses=[Address("Belgrano 594", "X500JQL", "Cordoba", "Argentina")])
w = PersonAddressEditor(parent=app, target=p)
w.show()
app.run()
