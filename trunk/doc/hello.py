# This is probably the simplest cimarron program you can have.

# first, import it :)
import cimarron

# next, ask cimarron for an user interface engine. As we haven't
# specified any engine (with cimarron.setEngine()), a default is used.
ui = cimarron.getEngine()

# coordinator of all windows
app = ui.Application()

# a Window.
win = ui.Window(parent=app)

# a Label.
lbl = ui.Label(parent=win,
               label="Hello, World!")

# show the window
win.show()

# start the app
app.run()
