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
    unittest.main(argv=[sys.argv[0], '-v'])
