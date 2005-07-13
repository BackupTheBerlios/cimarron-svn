import operator
from fvl import cimarron
cimarron.config()

class CalculatorController(cimarron.skin.WindowController):
    def __init__(self, **kw):
        super(CalculatorController, self).__init__(**kw)
        self.win.title = 'Calculator'
        vbox = cimarron.skin.VBox(parent=self.win)
        self.display = cimarron.skin.Label(parent=vbox, text='0')
        hbox = cimarron.skin.HBox(parent=vbox)
        for aRow in (({'label': '7', 'onAction': self.numberButton},
                      {'label': '4', 'onAction': self.numberButton},
                      {'label': '1', 'onAction': self.numberButton},
                      {'label': 'C', 'onAction': self.clear}),
                     ({'label': '8', 'onAction': self.numberButton},
                      {'label': '5', 'onAction': self.numberButton},
                      {'label': '2', 'onAction': self.numberButton},
                      {'label': '0', 'onAction': self.numberButton}),
                     ({'label': '9', 'onAction': self.numberButton},
                      {'label': '6', 'onAction': self.numberButton},
                      {'label': '3', 'onAction': self.numberButton},
                      {'label': '.', 'onAction': self.numberButton}),
                     ({'label': '+', 'onAction': self.operate, 'calcOp': operator.add},
                      {'label': '-', 'onAction': self.operate, 'calcOp': operator.sub},
                      {'label': '*', 'onAction': self.operate, 'calcOp': operator.mul},
                      {'label': '/', 'onAction': self.operate, 'calcOp': operator.div})):
            vbox = cimarron.skin.VBox(parent=hbox)
            for parms in aRow:
                cimarron.skin.Button(parent=vbox, **parms)
        self.clear()

    def numberButton(self, sender=None):
        if self.resetInput:
            self.display.text = sender.label
        else:
            self.display.text = self.display.text + sender.label
        self.resetInput = False

    def clear(self, sender=None):
        self.op = None
        self.display.text = '0'
        self.X = 0
        self.resetInput = True

    def operate(self, sender=None):
        try:
            if not self.resetInput:
                val = float(self.display.text)
                if self.op is not None:
                    val = self.op(self.X, val)
                self.display.text = str(val)
                self.X = val
                self.resetInput = True
            self.op = sender.calcOp
        except (ArithmeticError, ValueError):
            self.clear()
            self.display.text = '-- Error --'

app = cimarron.skin.Application()
w = CalculatorController(parent=app)
w.show()
app.run()
