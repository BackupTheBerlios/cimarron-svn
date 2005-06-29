from fvl import cimarron
cimarron.config()

class CalculatorController(cimarron.skin.WindowController):
    def __init__(self, **kw):
        super(CalculatorController, self).__init__(**kw)
        self.win.title = 'Calculator'
        vbox = cimarron.skin.VBox(parent=self.win)
        self.display = cimarron.skin.Label(parent=vbox, text='0')
        for aRow in [[['7', self.numberButton], ['8', self.numberButton],
                      ['9', self.numberButton], ['+', self.operate]],
                     [['4', self.numberButton], ['5', self.numberButton],
                      ['6', self.numberButton], ['-', self.operate]],
                     [['1', self.numberButton], ['2', self.numberButton],
                      ['3', self.numberButton], ['*', self.operate]],
                     [['C', self.clear], ['0', self.numberButton],
                      ['.', self.numberButton], ['/', self.operate]]]:
            hbox = cimarron.skin.HBox(parent=vbox)
            for aLabel, anAction in aRow:
                cimarron.skin.Button(parent=hbox, label=aLabel, onAction=anAction)
        self.clear()

    def numberButton(self, sender=None):
        if self.resetDisplay:
            self.display.text = sender.label
        else:
            self.display.text = self.display.text + sender.label
        self.resetDisplay = False

    def clear(self, sender=None):
        self.op = None
        self.display.text = '0'
        self.resetDisplay = True

    def operate(self, sender=None):
        if self.op == None:
            self.X = float(self.display.text)
        else:
            if self.op == '+':
                self.X = self.X + float(self.display.text)
            elif self.op == '-':
                self.X = self.X - float(self.display.text)
            elif self.op == '*':
                self.X = self.X * float(self.display.text)
            elif self.op == '/':
                self.X = self.X / float(self.display.text)
        self.op = sender.label
        self.display.text = str(self.X)
        self.resetDisplay = True

app = cimarron.skin.Application()
w = CalculatorController(parent=app)
w.show()
app.run()
