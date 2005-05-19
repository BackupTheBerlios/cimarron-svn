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

PYTHON=python

all:

clean:

distclean: clean
	find '(' -name '*.py[co]' -o -name '*~' ')' -print0 | xargs -0 -r rm -v
	$(PYTHON) setup.py clean
	rm -rfv build dist html MANIFEST

test:
	PYTHONPATH=.:./examples/persona:$$PYTHONPATH $(PYTHON) test/run.py $(TESTOPTS)

install:
	$(PYTHON) setup.py install

html:
	epydoc --encoding utf-8 --html `find papo -type f -name __init__.py -printf "%h\n"`

.PHONY: test html
