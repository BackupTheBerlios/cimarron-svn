from fvl import cimarron
from model import Person, Address

class PersonAddressEditor(cimarron.skin.WindowController):
    def __init__(self, target=None, **kw):
        super(PersonAddressEditor, self).\
            __init__(title='Person Editor', size=(50, 15), **kw)
        outer_vbox = cimarron.skin.VBox(parent=self.window)
        hbox = cimarron.skin.HBox(parent=outer_vbox, expand=False)
        vbox = cimarron.skin.VBox(parent=hbox, expand=False)
        cimarron.skin.Label(parent=vbox, text='Name:')
        cimarron.skin.Label(parent=vbox, text='Surname:')
        vbox = cimarron.skin.VBox(parent=hbox)
        gridColumns = (cimarron.skin.Column(name="Street", attribute="street"),
                       cimarron.skin.Column(name="City", attribute="city"),
                       cimarron.skin.Column(name="Country", attribute="country"))
        self.widgets = \
            (cimarron.skin.Entry(parent=vbox, attribute="name",
                                 onAction=self.checkValues, delegates=[self]),
             cimarron.skin.Entry(parent=vbox, attribute="surname",
                                 onAction=self.checkValues, delegates=[self]),
             cimarron.skin.Grid(parent=outer_vbox, cls=Address,
                                attribute="addresses", columns=gridColumns))
        cimarron.skin.Button(parent=outer_vbox, label='Check',
                             onAction = self.checkValues, expand=False)
        self.label = cimarron.skin.Label(parent=outer_vbox, text="", expand=False)
        if target is not None:
            self.newTarget(target)

    def checkValues(self, sender=None):
        self.label.text = "Mr/Ms %s, %s (%d addresses)" % \
                          (self.target.surname, self.target.name,
                           len(self.target.addresses))

    def will_focus_out(self, control):
        if control.value:
            control.value = control.value.strip().title()
        if not control.value:
            return cimarron.skin.ForcedNo
        return cimarron.skin.Yes

    def newTarget(self, target=None):
        super(PersonAddressEditor, self).newTarget(target)
        for w in self.widgets:
            w.newTarget(self.value)
        self.checkValues(self)

app = cimarron.skin.Application()
w = PersonAddressEditor(parent=app, target=Person.__values__[0])
w.show()
app.run()
