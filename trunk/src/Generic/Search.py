from StatefulControl import StatefulControl, _
from SearchEntry import SearchEntry, SearchTextEntry
from Exceptions import MiscError

import cimarron
ui= cimarron.getEngine ()

class Search(StatefulControl):
    __kwargs = ("innerContainerClass", "searchEntries")
    __obligs = {"_searchEntries": list,
                # "_finders": list,
                "_entries": list,
                }

    def setInnerContainerClass(self, ick):
        self._ick = ick
    def getInnerContainerClass(self):
        return self._ick

    def addChild (self, child):
        if not isinstance (child, SearchEntry):
            raise MiscError ('a')
        super (Search, self).addChild (child)
        self._entries.append(child)
        
    def foundOne(self, value):
        self._doSetValue(value)
        self.acceptInput()

    def search(self, entry, value):
        if not value:
            self.foundOne(None)
        else:
            self.busy()
            finder = entry.getFinder()
            found = finder.finder(value)
            if found[0] > 1:
                self.choose(found, entry)
            elif found[0] == 1:
                self.foundOne(finder.fetchAll(found)[0])
            else:
                entry.notifyNotFound()
            self.idle()
            
    def choose(self, found, entry):
        self.pushStatus(_('Waiting for selection...'))
        self.getWindow().disable()
        try:
            self._doChoose(found, entry)
        finally:
            self.getWindow().enable()
            self.popStatus()


class BoxedSearch (Search):
    def __init__ (self, **kw):
        self._processArgs(BoxedSearch, kw)

class VSearch (BoxedSearch):
    def __init__ (self, **kw):
        self._processArgs(VSearch, kw)

class HSearch (BoxedSearch):
    def __init__ (self, **kw):
        self._processArgs(HSearch, kw)
