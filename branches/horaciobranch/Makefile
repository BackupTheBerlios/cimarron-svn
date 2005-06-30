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
COLORIZER ?= tools/ppython
EPYDOC ?= epydoc
EPYDOC_OPTS ?=

PYTHON_FILES=$(shell find fvl -type f -name \*.py)

all: docs

clean:
	$(MAKE) -C tutorial clean
	$(MAKE) -C html clean

distclean: clean
	find '(' -name '*.py[co]' -o -name '*~' -o -name '*,cover' ')' -print0 | xargs -0 -r $(RM)
	$(PYTHON) setup.py clean
	$(RM) -r build dist MANIFEST .coverage
	$(MAKE) -C tutorial distclean
	$(MAKE) -C html clean

test: epytest unittest

epytest:
	$(EPYDOC) --check $(PYTHON_FILES)

unittest:
	PYTHONPATH=.:./examples/person:$$PYTHONPATH $(PYTHON) test/run.py $(TESTOPTS) 2>&1 | $(COLORIZER)

.coverage: $(PYTHON_FILES)
	PYTHONPATH=.:./examples/person:$$PYTHONPATH $(PYTHON) tools/coverage.py -x test/run.py --test-all || true
	$(PYTHON) tools/coverage.py -a $(PYTHON_FILES)

coverage: .coverage
	$(PYTHON) tools/coverage.py -r -m $(PYTHON_FILES)

install:
	$(PYTHON) setup.py install

docs: html tutorial

tutorial:
	$(MAKE) -C tutorial

html: tutorial
	$(MAKE) -C html

.PHONY: test epytest unittest docs tutorial all clean distclean api coverage
