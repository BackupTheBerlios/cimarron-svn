class Observable(object):
    def __init__ (self, **kw):
        super (Observable, self).__init__ (**kw)
        self.observers= []

    def announce (self, message):
        for o in self.observers:
            o.notify (message)

