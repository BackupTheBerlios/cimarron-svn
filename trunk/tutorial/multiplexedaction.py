from fvl import cimarron
cimarron.config()

class MainWindowController(cimarron.skin.WindowController):
   def __init__(self, **kw):
       super(MainWindowController, self).__init__(**kw)
       self.win.title = 'Main Window'
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

app = cimarron.skin.App()
w = MainWindowController(parent=app)
w.show()
app.run()
