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

from Dialog import Dialog
import mvc


class SelectDialog (Dialog):

    def __init__ (self, title, gridColumns):
        ui= mvc.getEngine ()
    
        # stock button lists
        ok= ui.Button ('OK', True)
        ok.fromStock ('OK')
        cancel= ui.Button ('CANCEL', False)
        cancel.fromStock ('CANCEL')

        contents= ui.HBox ()
        grid = ui.Grid()
        for key in gridColumns.keys():
            grid.addColumn(key, gridColumns[key])
        grid.makeView()
        self._grid = grid
        contents.addChild (grid)
        super (SelectDialog, self).__init__ (title, contents, [ok,cancel])

    def setOptionsList(self, result):
        self.getGrid().setValue(result)
        
    def getGrid(self):
        return self._grid
    
