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
from Utils.Debug import debug

class MagicArgsError(StandardError):
    pass

class metaMagicArgs(type):
    def __new__(meta, name, bases, dct):
        klass = super(metaMagicArgs, meta).__new__(meta, name, bases, dct)
        if not klass.__dict__.get('__init__', None):
            klass.__init__ = lambda self, **kw: self._processArgs(klass, kw)
        return klass

class MagicArgs(object):
    # set up debug method
    debug= debug

    __metaclass__ = metaMagicArgs
    def __init__(self, **kw):
        if kw:
            raise MagicArgsError, "%s got unexpected keyword arguments %s" % \
                  (self.__class__.__name__, ", ".join(kw))
        super(MagicArgs, self).__init__(kw)
    def _processArgs(self, klass, kw):
        """
        This protected method is the only thing you should need to do
        from __init__, and then only if the class has setFoo
        methods. What you should do is define a class attribute
        "__kwargs" that is a tuple of optional keyword arguments. For
        example, if you have a setFoo, you'd put "foo" in the
        tuple. Next, if the class has instance attributes it must have
        (obligatory instance attributes), you define a class attribute
        "__obligs" that is either a dictionary of obligatory argument:
        default value constructor, or a sequence of (obligatory
        argument, default value constructor). This last one is for
        when you need an ordering.
        """
        self.debug ( 'processing %s in class %s' % (kw, klass))
        name = klass.__name__
        args = {}
        kwargs = getattr(klass, "_%s__kwargs" % (name), ())
        self.debug ('kwargs= %s' % str(kwargs))
        obligs = getattr(klass, "_%s__obligs" % (name), ())
        self.debug ('obligs= %s' % str(obligs))
        if isinstance(obligs, dict):
            obligs = [(k, v) for k, v in obligs.items()]
        for i in kwargs:
            try:
                args[i] = kw[i]
                del kw[i]
            except KeyError:
                self.debug ('KeyError exception on %s' % i)
                pass
        for k, v in [i for i in obligs if not hasattr(self, i[0])]:
            setattr(self, k, v())
        self.debug ('calling inherited init for class %s; params %s' % (klass, kw))
        super(klass, self).__init__(**kw)
        for i, v in args.items():
            getattr(self, "set" + i[0].upper() + i[1:])(v)

