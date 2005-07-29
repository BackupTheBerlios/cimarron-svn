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

"""
L{Widget}s are everything that the user sees of an L{Application}.
"""

__revision__ = int('$Rev$'[5:-1])

import logging
logger = logging.getLogger('fvl.cimarron.skins.gtk2.widget')

import gtk

from fvl.cimarron.skins.common import Widget

class Label(Widget):
    """
    A Label displays a piece of uneditable static text.
    """
    dirty = staticmethod(bool)
    def __init__(self, text='', **kwargs):
        """
        @param text: The text that will be displayed.
        """
        if '_concreteWidget' not in self.__dict__:
            self._outerWidget = self._concreteWidget = gtk.Label()
        super(Label, self).__init__(**kwargs)
        self.text = text

    def _set_text(self, text):
        """
        Set the L{Label}'s text. Underscores are converted into
        mnemonics.
        """
        self._concreteWidget.set_text_with_mnemonic(text)
    def _get_text(self):
        """
        Get the L{Label}'s text.
        """
        return self._concreteWidget.get_text()
    text = property(_get_text, _set_text,
                    doc="""The text to display""")

class Image(Widget):
    """
    An Image widget displays a static picture loaded from a file
    """
    dirty = staticmethod(bool)

    def __init__(self, filename=None, **kwargs):
        """
        @param filename: The name of the file that contains the image.
        """
        if '_concreteWidget' not in self.__dict__:
            self._outerWidget = self._concreteWidget = gtk.Image()
        super(Image, self).__init__(**kwargs)
        self.load(filename)

    def load(self, filename):
        """
        Load an image from a file.
        """
        self._concreteWidget.set_from_file(filename)

	
