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

import pygtk
pygtk.require('2.0')
import gdk_xcursor
del pygtk
del gdk_xcursor

# please keep ascii-sorted
# accdording to which field?
from Gtk2Application     import Gtk2Application     as Application
from Gtk2BoolEntry       import Gtk2BoolEntry       as BoolEntry
from Gtk2Button          import Gtk2Button          as Button
from Gtk2DateEntry       import Gtk2DateEntry       as DateEntry
from Gtk2Dialog          import Gtk2Dialog          as Dialog
#from Gtk2SelectDialog    import Gtk2SelectDialog    as SelectDialog
from Gtk2Frame           import Gtk2Frame           as Frame
from Gtk2Grid            import Gtk2Grid            as Grid
from Gtk2HBox            import Gtk2HBox            as HBox
from Gtk2HButtonBox      import Gtk2HButtonBox      as HButtonBox
# from Gtk2Search          import Gtk2HSearch         as HSearch
from Gtk2Image           import Gtk2Image           as Image
from Gtk2Label           import Gtk2Label           as Label
from Gtk2MsgDialog       import Gtk2MsgDialog       as MsgDialog
from Gtk2MsgDialog       import Gtk2WarningDialog   as WarningDialog
from Gtk2MsgDialog       import Gtk2QuestionDialog  as QuestionDialog
from Gtk2Notebook        import Gtk2Notebook        as Notebook
from Gtk2NumEntry        import Gtk2NumEntry        as NumEntry
# from Gtk2Search          import Gtk2Search          as Search
# from Gtk2Search          import Gtk2VSearch         as VSearch
# from Gtk2SearchEntry     import Gtk2SearchTextEntry as SearchTextEntry
# from Gtk2SearchEntry     import Gtk2SearchEntry     as SearchEntry
from Gtk2Table           import Gtk2Table           as Table
from Gtk2TextEntry       import Gtk2TextEntry       as TextEntry
from Gtk2VBox            import Gtk2VBox            as VBox 
from Gtk2VButtonBox      import Gtk2VButtonBox      as VButtonBox
from Gtk2ViewController  import Gtk2ViewController  as ViewController
from Gtk2Window          import Gtk2Window          as Window
