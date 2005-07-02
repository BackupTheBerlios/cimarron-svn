.. -*- rst -*-

   Copyright 2005 Fundación Via Libre
  
   This file is part of PAPO.
  
   PAPO is free software; you can redistribute it and/or modify it under the
   terms of the GNU General Public License as published by the Free Software
   Foundation; either version 2 of the License, or (at your option) any later
   version.
  
   PAPO is distributed in the hope that it will be useful, but WITHOUT ANY
   WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
   FOR A PARTICULAR PURPOSE.  See the GNU General Public License for more
   details.
  
   You should have received a copy of the GNU General Public License along with
   PAPO; if not, write to the Free Software Foundation, Inc., 59 Temple Place,
   Suite 330, Boston, MA 02111-1307 USA

Cimarrón
========

Introduction
------------

Cimarrón is a framework for the construction of reusable GUI components, using
(recursive) variations of the classic (NeXT-like) MVC pattern. Provided are a
pretty basic set of views (it is trivial to add more, and more will be provided
as the PAPO project advances), and a few controllers. Also provided is a small
example.

The aim of Cimarrón is to be toolkit-agnostic, but we've only had time to
implement the Gtk2 'skin' so far.

As there are several takes on what MVC means, we'll try to explain it here.

Meanwhile, you might want to get your hands dirty with
examples/LEEME.txt. Yes, it's in spanish, and right now, it's not even
completely correct. An English-language tutorial_ is in progress;
Alas, the API described in it is not completely implemented yet (it
should be very soon).

.. _tutorial: tutorial/index.html

The API_ documentation is up to date because it is generated, but it
might not be terribly useful yet (not enough documentation in the
classes, perhaps).

.. _API: api/index.html

Dependencies
------------

Basically, we depend on python_ (2.2.3 or later, although we've not
been able to run all the tests on 2.2 yet), libxml2_ and, for default
(and currently only) skin, pygtk_ 2. Also, we use zope3_'s
zope.interface and zope.schema packages, so you'll need those too.

.. _python: http://www.python.org/
.. _libxml2: http://xmlsoft.org/
.. _pygtk: http://www.pygtk.org/
.. _zope3: http://www.zope.org/DevHome/Wikis/DevSite/Projects/ComponentArchitecture/FrontPage

If you want your windows to be able to take screenshots of themselves
(for documentation purposes, for example) you'll need the ImageMagick_
utilities (specifically, the 'import' tool); for the tests of this
functionality to pass you'll need the `python imaging library`_.

.. _ImageMagick: http://www.imagemagick.org/
.. _python imaging library: http://www.pythonware.com/products/pil/

To generate the documentation you'll need the `python docutils`_ and
epydoc_; to run the tests you'll need epydoc_.

.. _python docutils: http://docutils.sourceforge.net/
.. _epydoc: http://epydoc.sourceforge.net/

We've tested it on Debian_ Sarge_ (python 2.3.5, libxml2 2.6.16, pygtk
2.6.1), Mandrake_ 10.1 (python 2.3, libxml2 2.6.13, pygtk 2.3.96),
and Ubuntu_ Hoary_ (python 2.4.1, libxml2 2.6.17, pygtk 2.6.1).

.. _debian: http://www.debian.org/
.. _sarge: http://www.debian.org/releases/sarge/
.. _mandrake: http://www.mandrivalinux.com/
.. _ubuntu: http://www.ubuntulinux.org/
.. _hoary: http://us.releases.ubuntu.com/releases/5.04/

Quickstart
----------

Once you've checked out the source from SVN, you could run the example directly
from the source tree: assuming you checked out the source with::

    svn checkout svn://svn.berlios.de/cimarron/trunk cimarron

your source tree will be in a directory named 'cimarron'. cd to that directory,
and run the tests::

    cimarron$ make test

All the tests should pass, although epydoc will still complain
about missing documentation.

Once that is out of the way, do this::

    cimarron$ export PYTHONPATH=".:./examples/person:$PYTHONPATH"
    cimarron$ python examples/person/main.py

Misc notes
----------

The documentation can be correctly generated with a patched_ version
of epydoc; otherwise, you'll get ISO-8859-1 instead of UTF-8, and some
characters will look funny. Ha-ha.

.. _patched: http://sourceforge.net/mailarchive/forum.php?thread_id=7254214&forum_id=39919

Also, note the funky formatting of this file is because it's actually
RST_.

.. _RST: http://docutils.sourceforge.net/docs/ref/rst/restructuredtext.html
