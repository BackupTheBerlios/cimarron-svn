

import sys
from optparse import OptionParser

default_skin_name = 'gtk2'

class App(object):
    def __init__(self):
        
        parser = OptionParser()
        parser.add_option("-s", "--skin", dest="skin",
                          default=default_skin_name,
                          help="choose default skin [%s]" % default_skin_name,
                          metavar="SKIN")

        (options, args) = parser.parse_args()

        self.skin = __import__('papo.cimarron.skins.' + options.skin,
                               globals(), locals(), options.skin)

        self.children = []

    def show(self):
        for i in self.children:
            i.show()

    def __getattr__(self, attr):
        return getattr(self.skin, attr)
