import gtk
from Generic.SearchTextEntry import SearchTextEntry, _
from Gtk2TextEntry import Gtk2TextEntry

class Gtk2SearchTextEntry(SearchTextEntry, Gtk2TextEntry):
    __obligs = { '_img': gtk.Image,
                 '_obj': gtk.HBox,
                 '_entry': gtk.Entry,
                 }
    def __init__(self, **kw):
        self._processArgs(Gtk2SearchTextEntry, kw)
        obj = self._obj
        img = self._img
        entry = self._entry
        img.set_from_pixbuf(self._accepted)
        obj.add(img)
        obj.add(entry)

        def changed(widget):
            if widget.get_text() != self.getValue():
                img.set_from_pixbuf(self._unknown)
            else:
                img.set_from_pixbuf(self._accepted)

        entry.connect('changed', changed)

    def _doSetValue(self, value):
        super(Gtk2SearchTextEntry, self)._doSetValue(value)
        self._img.set_from_pixbuf(self._accepted)

    def _activate(self, widget):
        self.doSearch(widget.get_text())
        widget.grab_focus()
    def _focusOut(self, widget, event):
        pass

    def _doNotifyNotFound(self):
        self._img.set_from_pixbuf(self._notfound)

Gtk2SearchTextEntry._accepted = gtk.gdk.pixbuf_new_from_file(Gtk2SearchTextEntry.getConfigAsString('accepted_image'))
Gtk2SearchTextEntry._unknown = gtk.gdk.pixbuf_new_from_file(Gtk2SearchTextEntry.getConfigAsString('unknown_image'))
Gtk2SearchTextEntry._notfound = gtk.gdk.pixbuf_new_from_file(Gtk2SearchTextEntry.getConfigAsString('notfound_image'))
