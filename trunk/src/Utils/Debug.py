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

from traceback import extract_stack
from os.path import basename
# from sets import Set

# sections= Set ([])
sections= []

if __debug__:
    def debug (*seq, **kwargs):
        if len (seq)==2:
            s= seq[1]
        else:
            s= seq[0]
        stack= extract_stack ()
        (filename, lineno, funname, something)= stack[-2]
        filename= basename (filename)
        section= filename[:-3]
        if not section in sections:
            return
        print "[%s:%d, %s()] %s" % (filename, lineno, funname, s)
        if kwargs.has_key ('parents'):
            parent= -3
            print "stack:"
            for i in xrange (kwargs['parents']):
                (filename, lineno, funname, something)= stack[parent]
                filename= basename (filename)
                print "[%s:%d, %s()]" % (filename, lineno, funname)
                parent-= 1
            print
                

else:
    def debug (*seq):
        pass
