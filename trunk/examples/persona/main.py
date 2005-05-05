from papo import cimarron
cimarron.config ()

from windows import Main

def main ():
    app= cimarron.skin.App ()
    w= Main (parent= app)
    w.show ()
    app.run ()

if __name__=='__main__':
    main ()
