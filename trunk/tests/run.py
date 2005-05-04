import os, sys, re
import unittest
from optparse import OptionParser

if 1:
    moduleNames = ['controllerTests', 'gridTests', 'searchTests']

    testnames = ('focus-events', 'delegations')

    parser = OptionParser()
    parser.add_option('-v', '--verbose', help="be verbose",
                      action="store_true", default=False)
    parser.add_option('-q', '--quiet', help="be quiet",
                      action="store_true", default=False)
    parser.add_option('-s', '--sync', help="make X calls synchronous",
                      action="store_true", default=False)
    parser.add_option('-S', '--skin', help="use specified skin", default='gtk2')
    parser.add_option('-M', '--module', help="test this module (may be specified multiple times)", action="append")
    parser.add_option('-a', '--test-all', action="store_true", default=False)
    for testname in testnames:
        optname = testname.replace('-','_')
        parser.add_option('--test-'+testname, action="store_true", dest=optname)
        parser.add_option('--no-test-'+testname, action="store_false", dest=optname)

    test_options, args = parser.parse_args()
    all = test_options.test_all
    for testname in testnames:
        optname = testname.replace('-', '_')
        if getattr(test_options, optname) is None:
            setattr(test_options, optname, all)

    argv = sys.argv[:1]
    if test_options.verbose:
        argv.append('-v')
    if test_options.quiet:
        argv.append('-q')

    if test_options.module is None:
        moduleNames.append(test_options.skin+'Tests')
    else:
        moduleNames = test_options.module

    import run
    run.test_options = test_options

    for i in moduleNames:
        exec 'from %s import *' % i

if __name__ == '__main__':
    unittest.main(argv=argv)
