import os, sys
import unittest

try:
    import papo
except ImportError:
    sys.path.append(os.path.abspath('..'))

#if __name__ == '__main__':
#    all = sys.argv.count('-a')

from hello import *
from gtkTests import *
from controllerTests import *

if __name__ == '__main__':
    argv = list(sys.argv)
    while sys.argv.count('-v'):
        sys.argv.remove('-v')
    #while sys.argv.count('-a'):
    #    sys.argv.remove('-a')
    unittest.main(argv=argv)
