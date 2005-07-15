from fvl import cimarron

class MainWindowController(cimarron.skin.WindowController):
   def __init__(self, **kw):
       super(MainWindowController, self).__init__(**kw)
       self.win.title = 'Multiplexed Action Demo'
       self.win.size = (40, 10)
       vbox = cimarron.skin.VBox(parent=self.win)
       cimarron.skin.Button(parent=vbox, label='Pleasure',
           onAction = self.doSomething)
       cimarron.skin.Button(parent=vbox, label='Pain',
           onAction = self.doSomething)

   def doSomething(self, sender):
       if sender.label == 'Pleasure':
           print 'That was *nice*! Thank you!'
       else:
           print 'Ouch!!! Don\'t do that!'

app = cimarron.skin.Application()
w = MainWindowController(parent=app)
w.show()
app.run()
