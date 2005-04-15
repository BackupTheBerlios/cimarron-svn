from papo.cimarron.skins.common import Container

class App(Container):
    def __init__(self, **kw):
        assert 'parent' not in kw, 'App should have no parent'
        super(App, self).__init__(**kw)

    def run(self):
        skin._run()
