import unittest 
from app.models import Sources,Articles

class SourcesTest(unittest.TestCase):
    '''
    Test class to test the behaviour of the class
    '''

def setUp(self):
    '''
    Set up method that will run before every test
    '''
    self.new_source = Sources('CNN', 'CNN News', 'Cable News Network that is a leader in providing news worldwide', 'cnn.com', 'general', 'general','U.S.A','en')

def test_instance(self):
    self.assertTrue(isinstance(self.new_source,Sources))

def test_to_check_instance_variables(self):
    self.assertEquals(self.new_source.id,'CNN')
    self.assertEquals(self.new_source.name,'CNN News')
    self.assertEquals(self.new_source.description,'Cable News Network that is a lead in providing news worldwide')
    self.assertEquals(self.new_source.url,'cnn.com')
    self.assertEquals(self.new_source.category,'general')
    self.assertEquals(self.new_source.country,'U.S.A')
    self.assertEquals(self.new_source.language,'en')


class ArticlesTest(unittest.TestCase):
    '''
    Test class to test the behaviour of the article class
    '''
    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_article = Articles('CNN','Joan Glory','The next Big thing','A look at the techhubs in Africa','techie.com','2020-07-11T07:57:16Z')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_article,Articles))

    def test_to_check_instance_variables(self):
        self.assertEquals(self.new_article.id,'CNN')
        self.assertEquals(self.new_article.author,'Joan Glory')
        self.assertEquals(self.new_article.title,'The next Big thing')
        self.assertEquals(self.new_article.description,'A look at the techhubs in Africa')
        self.assertEquals(self.new_article.url,'techie.com')
        self.assertEquals(self.new_article.date,'2020-07-11T07:57:16Z')