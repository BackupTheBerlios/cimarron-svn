from fvl import cimarron

class MainWindowController(cimarron.skin.WindowController):
   def __init__(self, **kw):
       super(MainWindowController, self).__init__(**kw)
       self.win.title = 'Simple Action Demo'
       self.win.size = (40, 5)
       cimarron.skin.Button(parent=self.win, label='Hello',
           onAction = self.doSomething)

   def doSomething(self, sender):
       print 'Button pressed!'

app = cimarron.skin.Application()
w = MainWindowController(parent=app)
w.show()
app.run()
