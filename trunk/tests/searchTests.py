from unittest import TestCase

from papo import cimarron

from gridTests import Persona


__all__=('TestSearch',)

class TestSearch (TestCase):
    def setUp (self):
        self.searchers= [
            self.byName,
            self.bySurname,
            ]

        self.widget= cimarron.controllers.Search (
            parent= self.parent,
            search= self.search,
            entries= [cimarron.skin.Entry (), cimarron.skin.Entry ()]
            )

    def byName (self, name):
        pass

    def search (self, values):
        name, surname= values[:2]
        ans= []

        for i in self.data:
            found= False
            if name is not None:
                found= name in i.name
            if surname is not None:
                found= found and surname in i.surname

            if found:
                ans.append (i)

        return ans

    def testNoneFound (self):
        self.data= []
        # make it search
        # how?
        self.widget.doSearch ()
        self.assertEqual (self.widget.value, None)
