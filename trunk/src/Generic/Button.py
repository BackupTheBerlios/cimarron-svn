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

import gtk
from Control import Control
from Exceptions import ButtonError

class Button(Control):
    """
    Generic push button. Has a caption that consists of a Image and a Label.
    Both the image and the label are optional.
    The button can also carry a value, which is neither the label nor the icon,
    which obviously cannot be changed by the user (thru direct input), 
    but can be changed 'by soft'.
    """
    # _default_value = 0
    # the button is the only Control where the value is a public attr.
    __kwargs = ('label', 'image', 'stockImage', 'stock', 'value')

    def setLabel(self, label):
        """
        Change the label part of the caption. Only text.
        """
        if self.delegate ('will_set_label', args=label):
            try:
                self._doSetLabel(label)
            except:
                raise ButtonError, _("Unable to set label")
            return True
        return False

    def setStockImage(self, image):
        if self.delegate('will_set_stock_image', args=image):
            self._doSetStockImage(image)
            return True
        return False
    def setImage(self, image):
        """
        Change the image part of the caption. Specify a path.
        """
        if self.delegate ('will_set_image', args=image):
            try:
                self._doSetImage(image)
            except:
                raise ButtonError, _("Unable to set image")
            return True
        return False

    def setStock (self, stock):
        """
        Change both the label and the image to that of a stock label,
        image pair.
        """
        if self.delegate('will_set_stock', args=stock):
            try:
                self._doSetStock (stock)
            except:
                raise ButtonError, _("Unable to set from stock")
            return True
        return False

    def getStock(self):
        return self._doGetStock()
