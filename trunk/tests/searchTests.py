from papo import cimarron

from commonTests import abstractTestControl
from gridTests import Person

__all__=('TestSearch',)

class PersonSearch (cimarron.controllers.Search):
    attrs= ('name', 'surname')
    def buildEntries (self):
        for i in PersonSearch.attrs:
            self.entries.append (cimarron.skin.Entry (
                parent= self.box,
                ))
    
    def search (self, values):
        name, surname= values[:2]
        # print 'searching with', values
        ans= []

        for i in self.data:
            found= False
            if name is not None:
                found= name in i.name
            if surname is not None:
                found= found and surname in i.surname

            if found:
                ans.append (i)

        # print 'found', ans
        return ans

    def refresh (self):
        if self.value is not None:
            for i in xrange (len (PersonSearch.attrs)):
                self.entries[i].value= getattr (self.value, PersonSearch.attrs[i])


class TestSearch (abstractTestControl):
    def setUp (self):
        super (TestSearch, self).setUp ()
        self.parent = self.win = cimarron.skin.Window(title='Test', parent=self.app)
        self.widget= PersonSearch (
            parent= self.parent,
            )
        self.data= [
            Person ('jose', 'perez'),
            Person ('marcos', 'dione'),
            Person ('john', 'lenton'),
            Person ('pedro', 'dargenio'),
            ]
        self.value= self.widget.value= self.data[0]

    def testNoneInEmptyFound (self):
        # here we 'plant' the data, but real Search's will fetch its own data
        self.widget.data= []
        self.widget.doSearch ()
        self.assertEqual (self.widget.value, None)

    def testNoneMatchesFound (self):
        # here we 'plant' the data, but real Search's will fetch its own data
        self.widget.data= self.data
        searchingValues= (
            ('martin', ''),
            ('', 'rezk'),
            )
        
        for i in xrange (len (searchingValues)):
            for j in xrange (len (searchingValues[i])):
                self.widget.entries[j].value= searchingValues[i][j]
            self.widget.doSearch ()
            self.assertEqual (self.widget.value, None)

    def testOneFound (self):
        self.widget.data= self.data
        searchingValues= (
            ('jos', ''),
            ('', 'pe'),
            ('m', ''),
            ('', 'dio'),
            ('john', ''),
            ('', 'lenton'),
            ('p', ''),
            ('', 'da'),
            )
        for i in xrange (len (searchingValues)):
            for j in xrange (len (searchingValues[i])):
                self.widget.entries[j].value= searchingValues[i][j]
            self.widget.doSearch ()
            self.assertEqual (self.widget.value, self.data[i/2])

    def testSomeFound (self):
        self.widget.data= self.data
        searchingValues= (
            ('jo', '', self.data[2]),
            ('', 'd',  self.data[3]),
            )
        for i in xrange (len (searchingValues)):
            for j in xrange (2):
                self.widget.entries[j].value= searchingValues[i][j]
            self.widget.doSearch ()
            self.assertEqual (self.widget.value, searchingValues[i][2])
            
    def testOnAction (self):
        self.widget.data= self.data
        super (TestSearch, self).testOnAction ()
        
if 0:
    def testVisual (self):
        self.widget.data= self.data
        self.app.show ()
        self.app.run ()
