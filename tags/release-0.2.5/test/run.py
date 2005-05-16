# -*- coding: utf-8 -*-
#
# Copyright 2003 Fundación Via Libre
#
# This file is part of PAPO.
#
# PAPO is free software; you can redistribute it and/or modify it under the
# terms of the GNU General Public License as published by the Free Software
# Foundation; either version 2 of the License, or (at your option) any later
# version.
#
# PAPO is distributed in the hope that it will be useful, but WITHOUT ANY
# WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
# FOR A PARTICULAR PURPOSE.  See the GNU General Public License for more
# details.
#
# You should have received a copy of the GNU General Public License along with
# PAPO; if not, write to the Free Software Foundation, Inc., 59 Temple Place,
# Suite 330, Boston, MA 02111-1307 USA

import os, sys, re
import unittest
from optparse import OptionParser

moduleNames = ['hello', 'testController', 'testSearch', 'testSkeleton']

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
    moduleNames.append('test' + test_options.skin.capitalize())
else:
    moduleNames = test_options.module

import run
run.test_options = test_options

for i in moduleNames:
    exec 'from %s import *' % i

if __name__ == '__main__':
    unittest.main(argv=argv)
