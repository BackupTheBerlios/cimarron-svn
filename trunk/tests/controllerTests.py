class FooController():
    def __init__(self):
        self.app = cimarron.App()
        self.win = cimarron.Window(parent=app)
        self.model = dict(foo=1,
                          bar=2,
                          baz=3)
        self.label = cimarron.Label(parent=self.win)
        self.entry = cimarron.Entry(parent=self.win, action=action)
        def action(entry):
            #  When the user enters a value, if it has a '=', it is
            #  used as a key-value pair to update the model; otherwise
            #  as a simple key to fetch the value from the model. The
            #  entry then displays the value associated with the key.

            if entry.value.index('=') > -1:
                self.model.update(dict((entry.value.split('='),)))
            entry.value = repr(self.model.get(entry.value))
            self.update()
        self.update()


    def update(self):
        #
        # update the label to show the stringification of the model

        self.label.text = repr(self.model)

