# -*- python -*- coding: ISO-8859-1 -*-
# Copyright 2004 Fundacion Via Libre
#
# This file is part of PAPO.
# 
# PAPO is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
# 
# PAPO is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with PAPO; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA

# wee! this thing works all the way back to python1.5!

from ConfigParser import ConfigParser, NoSectionError
from shlex import shlex
from cStringIO import StringIO
from string import strip
import os.path

try:
    False
except:
    False = 0
    True = 1

class Parser(ConfigParser):
    """
    A ConfigParser that `understands' lists

    For example, assuming the config file says

        foo = a, "blah, bleh", b, 'blih: bloh'
        
    getlist() will return

        [ 'a', 'blah, bleh', 'b', 'blih: bloh' ]

    The contents of the lists are always returned as strings.  The
    string is split at ',', unless quoted.  No triple-quotes.

    The value returned by get(), if not empty is passed through a
    sanitation process thanks to os.path. This is controlled by
    the"raw" kwarg.
    """
    # filters that are applied, in order, to the value returned by
    # get() if argument `clean' is not False
    __filters = [ os.path.expanduser,
                  os.path.expandvars,
                  os.path.normcase,
                  os.path.normpath,
                  ]
    def get(self, section, option, raw=False, vars=None):
        try:
            got = ConfigParser.get(self, section, option, raw, vars)
        except NoSectionError:
            got = None
        if got and not raw:
            got = reduce(lambda a, b: b(a), self.__filters, got)
        return got
    def getlist(self, section, option, raw=False, vars=None):
        x = self.get(section, option, raw, vars)
        s = shlex(StringIO(x))
        s.commenters = "#;"
        s.whitespace = ""
        xs = ['']
        while True:
            token = s.get_token()
            if not token: break
            if token == ',':
                xs.append('')
            else:
                xs[-1] = xs[-1] + token
        ys=[]
        for x in xs:
            x = strip(x)
            if x:
                if x[0]==x[-1] and x[0] in ("'", '"'):
                    x = x[1:-1]
                ys.append(x)
        
        return ys

