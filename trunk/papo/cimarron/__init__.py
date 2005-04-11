import sys
from optparse import OptionParser

from papo.cimarron.skins.common import Container

default_skin_name = 'gtk2'



class App(Container):
    def __init__(self, **kw):
        assert 'parent' not in kw, 'App should have no parent'
        super(App, self).__init__(**kw)
#    def __getattr__(self, attr):
#        return getattr(skin, attr)

parser = OptionParser()
parser.add_option("-s", "--skin", dest="skin",
                  default=default_skin_name,
                  help="choose default skin [%s]" % default_skin_name,
                  metavar="SKIN")

(options, args) = parser.parse_args()

skin = __import__('papo.cimarron.skins.' + options.skin,
                  globals(), locals(), options.skin)
