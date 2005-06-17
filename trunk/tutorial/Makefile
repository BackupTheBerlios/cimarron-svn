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

PYTHON		?= python
PYTHON_BASE	?= $(shell $(PYTHON) -c 'import os; print os.path.dirname(os.__file__)')
MKHOWTO		= $(PYTHON_BASE)/doc/tools/mkhowto

SOURCES		= tutorial.tex \
		  helloworld.py \
		  multiplexedaction.py \
		  simpleaction.py \
		  simplepersoneditor.py \
		  simpleperson.py

all:	tutorial/index.html tutorial.dvi tutorial.pdf

clean:
	$(RM) -r tutorial tutorial.dvi tutorial.pdf *~

distclean: clean

tutorial/index.html: $(SOURCES)
	$(MKHOWTO) --html tutorial.tex

tutorial.dvi: $(SOURCES)
	$(MKHOWTO) --dvi tutorial.tex

tutorial.pdf: $(SOURCES)
	$(MKHOWTO) --pdf tutorial.tex

.PHONY: all clean distclean
