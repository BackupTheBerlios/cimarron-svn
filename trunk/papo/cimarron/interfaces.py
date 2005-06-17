from zope import interface, schema

class IWindow(interface.Interface):
    def __init__(title, **kw): pass
    title = interface.Attribute('')

class ISkin(interface.Interface):
    def _run():
        """
        _run() is called from App.run, to set in motion whatever
        mechanism the concrete backend uses to display widgets.
        """

    def _quit():
        """
        _quit() is called from App.quit to terminate the application;
        it might never return (or leave the backend in an unspecified
        state)
        """

    def _schedule(timeout, callback, repeat=False):
        """
        _schedule is called from App.schedule to actually do the
        scheduling of the delayed action.
        """

    def concreteParenter(parent, child):
        """
        concreteParenter dos the skin-specific magic that `glues' a
        child with its parent.
        """

    # thanks to Stephan Richter <srichter@cosmos.phy.tufts.edu>
    Window = schema.Object(
        schema = IWindow,
        title = u'Window',
        required = True,
        )
