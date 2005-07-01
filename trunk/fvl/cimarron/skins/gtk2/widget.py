# -*- coding: utf-8 -*-
#
# Copyright 2003, 2004, 2005 Fundación Via Libre
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

import logging
logger = logging.getLogger('fvl.cimarron.skins.gtk2.widget')

import gtk

from fvl.cimarron.skins.common import Widget

class Label(Widget):
    """
    A Label is a piece of uneditable static text.
    """
    dirty = staticmethod(bool)
    def __init__(self, text='', **kw):
        """
        @param text: The static test.
        """
        self._widget = gtk.Label()
        super(Label, self).__init__(**kw)
        self.text = text

    def show(self):
        self._widget.show()

    def _set_text(self, text):
        self._widget.set_text_with_mnemonic(text)
    def _get_text(self):
        return self._widget.get_text()
    text = property(_get_text, _set_text, None, """The static test.""")

class Image(Widget):
    """
    A Image is a Static Picture loaded from a file
    """
    dirty = staticmethod(bool)

    def __init__(self,aFile=None,**kw):
        self._widget = gtk.Image()
        super(Image,self).__init__(**kw)
        self.imgFile = self.aFile = aFile

    def show(self):
        self._widget.show()

    def _set_file(self,aFile):
        self._widget.set_from_file(aFile)

    def _get_file(self):
        return self.aFile

    imgFile = property(_get_file, _set_file, None, """The static test.""")
	
