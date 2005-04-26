import os, sys, re
import unittest

try:
    import papo
except ImportError:
    sys.path.append(os.path.abspath('..'))

moduleNames = ['controllerTests', 'gridTests']

argv = list(sys.argv)
skin = 'gtk2'
for i, v in enumerate(sys.argv):
    if v in ('-v', '-q'):
        # these are for for unittest.main
        sys.argv.pop(i)
    elif v == '-a':
        # '-a' is for commonTests.abstractTestDelegateGenerated
        argv.pop(i)
    elif v.startswith('--skin='):
        # '--skin=foo' is for importing skin-specific tests
        argv.pop(i)
        skin = re.match('--skin=(.*)', v).group(1).strip()
moduleNames.append(skin+'Tests')
from searchTests import *

for i in moduleNames:
    exec 'from %s import *' % i

unittest.main(argv=argv)
