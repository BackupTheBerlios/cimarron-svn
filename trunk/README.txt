Cimarrón is a framework for the construction of reusable GUI components, using
(recursive) variations of the classic (NeXT-like) MVC pattern. Provided are a
pretty basic set of views (it is trivial to add more, and more will be
provided as the PAPO project advances), and a few controllers. Also provided
is a small example.

The aim of Cimarrón is to be toolkit-agnostic, but we've only had time to
implement the Gtk2 'skin' so far.

As there are several takes on what MVC means, we'll try to explain it here.

Meanwhile, you might want to get your hands dirty with examples/LEEME.txt
(yes, it's in spanish).

The documentation can be correctly generated with a patched version of epydoc.
You can grab the patch from here:

http://sourceforge.net/mailarchive/forum.php?thread_id=7254214&forum_id=39919

Or you can mofify the Makefile, and remove the --encoding parameter.
