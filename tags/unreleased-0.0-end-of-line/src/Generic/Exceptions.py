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

import sys
import traceback

class MagicError(StandardError):
    def __init__(self, msg):
        self.__msg = msg
        self.__exception = sys.exc_info()
    def __str__(self):
        if self.__exception[0] is not None:
            bt = "".join(traceback.format_exception(*self.__exception))
            bt = bt[:-1].replace("\n", "\n... ")
            #return "\033[31m%s\033[0m:\n... %s" \
            return "%s:\n... %s" \
                   % (self.__msg, bt)
        else:
            return str(self.__msg)

class ConfigError(MagicError):
    pass

class ResponderError(ConfigError):
    pass

class ViewError(ResponderError):
    pass

class CompositionError(ResponderError):
    pass

class MiscError(ViewError):
    pass

class LabelError(MiscError):
    pass

class ImageError(MiscError):
    pass

class FactoryError(ViewError):
    pass

class GridError(ViewError):
    pass

class ViewParentingError(ViewError):
    pass

class CompositeViewError(ViewError):
    pass

class ControlError(ViewError):
    pass

class BoolEntryError(ControlError):
    pass

class ButtonError(ControlError):
    pass

class StatefulControlError(ControlError):
    pass

class TextEntryError(StatefulControlError):
    pass

class SearchTextEntryError(TextEntryError):
    pass

class NumEntryError(TextEntryError):
    pass

class BoxError(CompositeViewError):
    pass

class ButtonBoxError(BoxError):
    pass

class FrameError(CompositeViewError):
    pass

class NotebookError(CompositeViewError):
    pass

class TableError(CompositeViewError):
    pass

class WindowError(CompositeViewError):
    pass

class ViewCompositionError(CompositeViewError):
    pass

class InvalidLabelJustification(ViewError):
    pass

class DuplicateObjectReference(GridError):
    pass
