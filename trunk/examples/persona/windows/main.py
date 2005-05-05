from papo import cimarron

from person import ABMPerson

__all__= (
    'Main',
    )

class Main (cimarron.skin.WindowController):
    def __init__ (self, **kw):
        super (Main, self).__init__ (**kw)
        self.win.title= 'Main window'
        v= cimarron.skin.VBox (parent= self.win)
        b= cimarron.skin.Button (
            parent= v,
            label= 'Person',
            onAction= self.person
            )

    def person (self, *ignore):
        w= ABMPerson (parent= self)
        w.delegates.append (self)
        w.show ()
