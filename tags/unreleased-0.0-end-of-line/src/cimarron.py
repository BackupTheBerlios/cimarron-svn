#!/usr/bin/env python
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

# for if you use this frozen:
import sys
if hasattr(sys, 'setdefaultencoding'):
    import locale
    loc = locale.getdefaultlocale()
    if loc[1]:
        sys.setdefaultencoding(loc[1])
    del locale
                                                                                                                            
# here starts a small bit of hackery to bootstrap the config and the
# translations. Maybe somebody can point out a cleaner way to do it?
from Generic import Config
from Utils.Parser import Parser
from os.path import join, dirname
from locale import setlocale, LC_ALL
from gettext import translation

__config = Parser()

# read in the first, mandatory, config file. These two files,
# i.e. cimarron.cfg and cimarron.py, should be right next to each
# other. At least, that's what I'm using here: if you're packaging it
# up for one specific place, you could set it to say /etc/cimarron.cfg
# or something
try:
    __file__
except NameError:
    # in python2.2 (at least), __file__ isn't defined for
    # scripts. Fortunately, sys.argv[0] is what we're looking for then
    __file__ = sys.argv[0]
__config.readfp(file(join(dirname(__file__), "cimarron.cfg")))

# the mandatory config must hold either the config_files var with a
# list of files, or all the other vars I'll want. Or both, obviously.
__config.read(__config.getlist("DEFAULT", "config_files"))

# This lets Responder et al "see" the config
Config.Config.setConfig(__config)

setlocale(LC_ALL, "")
_ = translation("cimarron", __config.get("DEFAULT", "locales")).ugettext
# This is a *BIG* uglyness: I literally violate Config. Hear her
# scream. But then Responder et all "see" _ without having to do two
# extra function calls each time, nor setting it up by hand in each
# class. If this is too ugly to bear, ... well, come up with something
# better.
Config._ = _

# clean up the mess
del translation, setlocale, LC_ALL, join, dirname, Config, Parser
# /hackery

from Generic.Exceptions import FactoryError
from Generic.Responder import Failed, Reject, Unknown, Accept, Done

__ENGINE = None

def setEngine(engine=None):
    global __ENGINE
    if __ENGINE is not None:
        raise FactoryError, _('Engine has already been set')
    if engine is None:
        engine = __config.get("DEFAULT", "default_engine")
    try:
        __ENGINE = __import__("%s.Engine" % (engine,),
                             globals(), locals(), ('Engine',))
    except:
        raise FactoryError, _('Unable to load %s engine') % (engine,)

def getEngine():
    global __ENGINE
    if __ENGINE is None:
        setEngine()
    return __ENGINE
    
def __main():
    ui = getEngine()
    app = ui.Application()
    win = ui.Window(title=_("Congratulations!"), parent=app, sizeRequest=(300,225))
    lbl = ui.Label(label='<b><span size="xx-large">%s</span></b>'
                           % (_('It worked!'),),
                   parent=win, useMarkup=True)
    win.show()
    app.run()

if __name__ == '__main__':
    __main()

