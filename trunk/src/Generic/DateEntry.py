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

from Utils import Debug
# Debug.sections.append ('DateEntry')

from TextEntry import TextEntry, _
import mx.DateTime

class DateEntry(TextEntry):
    def __init__(self, **kw):
        if not kw.has_key ('defaultValue') or kw['defaultValue'] is None:
            kw['defaultValue'] = mx.DateTime.today()
        # super(DateEntry, self).__init__(**kw)
        self._processArgs(DateEntry, kw)

        formats = self.getConfigAsList("custom_input_formats",
                                       default=_('%F::%Y%m%d').split('::'))
        self.debug (formats)
        def parser(date):
            for i in formats:
                try:
                    return mx.DateTime.strptime(date, i, self.getDefaultValue())
                except Exception:
                    pass
            return None

        format = self.getConfigAsString("custom_output_format", _('%F'))
        self.debug (format)
        def printer(datetime):
            try:
                return datetime.strftime(format)
            except:
                return None

        self.appendParser(parser)
        self.appendPrinter(printer)

        self.reset()
