# -*- coding: utf-8 -*-
#
# Copyright 2005 Fundación Via Libre
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
L{fvl} is the base package for anything developed by Fundación Vía
Libre.

All we actually do here right now is set up a logger.
"""

__revision__ = '$Rev$'

import logging

handler = logging.StreamHandler()
formatter = logging.Formatter("%(asctime)s %(name)40s:%(lineno)03d"
                              " %(levelname)-8s %(message)s")
handler.setFormatter(formatter)
logger = logging.getLogger('fvl')
logger.addHandler(handler)
# logger.setLevel(logging.DEBUG)
