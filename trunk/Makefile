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

PYTHON ?= python
EPYDOC ?= epydoc
EPYDOC_OPTS ?=

EPYDOC_FILES=$(shell find papo -type f -name \*.py)

all:

clean:

distclean: clean
	find '(' -name '*.py[co]' -o -name '*~' ')' -print0 | xargs -0 -r $(RM) -v
	$(PYTHON) setup.py clean
	$(RM) -rv build dist html MANIFEST

test:
	$(EPYDOC) --check --tests all $(EPYDOC_FILES)
	PYTHONPATH=.:./examples/persona:$$PYTHONPATH $(PYTHON) test/run.py $(TESTOPTS)

install:
	$(PYTHON) setup.py install

html:
	$(EPYDOC) --html $(EPYDOC_OPTS) $(EPYDOC_FILES)

.PHONY: test html
