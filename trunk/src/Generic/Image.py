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

from Misc import Misc, _
from Exceptions import ImageError

class Image(Misc):
    __kwargs = ('fromFile', 'fromStock')
    def setFromFile(self, filename):
        """

        Creates a new Image displaying the file filename. If the file
        isn't found or can't be loaded, the resulting Image will
        display a "broken image" icon.

        If the file contains an animation, the image will contain an
        animation.
        """
        if self.delegate('will_set_from_file', args=filename):
            try:
                self._doSetFromFile(filename)
            except:
                raise ImageError, _("Unable to build image from file")
            return True
        return False

    def setFromStock(self, *stck):
        """

        Creates a GtkImage displaying a stock icon. Sample stock icon
        names are 'open', 'exit'. Sample stock sizes are 'menu',
        'toolbar'. If the stock icon name isn't known, a "broken
        image" icon will be displayed instead.

        """
        try:
            stock, size = stck
        except ValueError:
            stock, size = stck[0]
        if self.delegate('will_set_from_stock', args=(stock, size)):
            try:
                self._doSetFromStock(stock, size)
            except:
                raise ImageError, _("Unable to build stock image")
            return True
        return False

