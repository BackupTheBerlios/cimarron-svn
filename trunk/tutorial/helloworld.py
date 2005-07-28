from fvl import cimarron

class MainWindowController(cimarron.skin.WindowController):
   def __init__(self, **kw):
       super(MainWindowController, self).\
            __init__(title = 'Hello World Demo', size = (40, 5), **kw)
       cimarron.skin.Button(parent=self.window, label='Hello')

app = cimarron.skin.Application()
w = MainWindowController(parent=app)
w.show()
app.run()
