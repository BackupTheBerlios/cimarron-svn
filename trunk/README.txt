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

Meanwhile, you might want to get your hands dirty with examples/LEEME.txt (yes,
it's in spanish).

Dependencies
------------

Basically, we depend on python_ (2.2.3 or later) and pygtk_ 2. We've tested it
on Debian_ Sarge_ (python 2.3.5, pygtk 2.6.1), Mandrake_ 10.1_ (python 2.3,
pygtk 2.3.96), and Ubuntu_ Hoary_ (python 2.4.1, pygtk 2.6.1).

.. _python: http://www.python.org/
.. _pygtk: http://www.pygtk.org/
.. _debian: http://www.debian.org/
.. _sarge: http://www.debian.org/releases/sarge/
.. _mandrake: http://www.mandrivalinux.com/
.. _10.1: http://www.google.com/
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
