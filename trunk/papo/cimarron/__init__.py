import sys
import new
from optparse import OptionParser

from papo.cimarron.skins.common import Container

default_skin_name = 'gtk2'



class App(Container):
    def __init__(self, **kw):
        assert 'parent' not in kw, 'App should have no parent'
        super(App, self).__init__(**kw)
        # probably not the best way to do this...
        parser = OptionParser()
        parser.add_option("-s", "--skin", dest="skin",
                          default=default_skin_name,
                          help="choose default skin [%s]" % default_skin_name,
                          metavar="SKIN")
        
        (options, args) = parser.parse_args()

        nskin = __import__('papo.cimarron.skins.' + options.skin,
                          globals(), locals(), options.skin)

        skin.faultFrom(nskin)
        skin._run = nskin._run

    def run(self):
        skin._run()

class proxyModule(new.module):
    def faultFrom(self, other):
        for k, v in other.__dict__.items():
            if not k[0] == '_':
                setattr(self, k, v)
        self.__name__ = other.__name__
        self.__file__ = other.__file__ + ' [proxied]'

skin = proxyModule('skin proxy')
