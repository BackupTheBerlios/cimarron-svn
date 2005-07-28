from fvl import cimarron

class MainWindowController(cimarron.skin.WindowController):
   def __init__(self, **kw):
       super(MainWindowController, self).\
            __init__(title = 'Multiplexed Action Demo',
                     size = (40, 10), **kw)
       vbox = cimarron.skin.VBox(parent=self.window)
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
