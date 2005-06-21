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

PYTHON ?= python
EPYDOC ?= epydoc
EPYDOC_OPTS ?=

EPYDOC_FILES=$(shell find fvl -type f -name \*.py)

all: docs

clean:
	$(MAKE) -C tutorial clean
	$(MAKE) -C html clean

distclean: clean
	find '(' -name '*.py[co]' -o -name '*~' ')' -print0 | xargs -0 -r $(RM)
	$(PYTHON) setup.py clean
	$(RM) -r build dist MANIFEST
	$(MAKE) -C tutorial distclean
	$(MAKE) -C html clean

test:
	$(EPYDOC) --check $(EPYDOC_FILES)
	PYTHONPATH=.:./examples/person:$$PYTHONPATH $(PYTHON) test/run.py $(TESTOPTS)

install:
	$(PYTHON) setup.py install

docs: html tutorial

tutorial:
	$(MAKE) -C tutorial

html: tutorial
	$(MAKE) -C html

.PHONY: test docs tutorial all clean distclean api
