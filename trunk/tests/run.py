import sys
import unittest

from hello import *
from windowTests import *
from labelTests import *
from buttonTests import *
from entryTests import *
from boxTests import *
from controllerTests import *

if __name__ == '__main__':
    argv = list(sys.argv)
    #if len(sys.argv) == 1:
    #    argv.append('-v')
    unittest.main(argv=argv)
