from papo import cimarron
cimarron.config ()
from papo.cimarron.controllers import App

from windows import Main

def main ():
    app= App ()
    w= Main (parent= app)
    w.show ()
    app.run ()

if __name__=='__main__':
    main ()
