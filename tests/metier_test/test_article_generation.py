from unittest import TestCase
from metier.article_generation import ArticleGeneration

class MockGenerator():
    iter = 0

    def next():
        iter+=1

    def getTitle():
        return "Obama"

def test_get_title(self):
    '''
    Fonction permettant de tester la méthode "get_title" qui donne le titre d'un article.
    '''
    # GIVEN : initialisation du test
    
    article = ArticleGeneration(0, [{"article":"Cookie_(informatique)","views":177667567,"rank":1}])

     #article = Article(.., .., MockGenerator)

    # WHEN : méthode à tester

    titre = article.get_title()

    # THEN : ce qu'on veut tester

    self.assertEqual("Cookie (informatique)", titre)


def test_get_views(self):
    '''
    Fonction permettant de tester la méthode "get_views" qui donne le nombre de vues d'un article.
    '''
    # GIVEN : initialisation du test

    article = ArticleGeneration(0, [{"article":"Cookie_(informatique)","views":177667567,"rank":1}])

    # WHEN : méthode à tester

    vues = article.get_views()

    # THEN : ce qu'on veut tester

    self.assertEqual(177667567, vues)

def test_validation(self):
    '''
    Fonction permettant de tester la méthode "validation" qui dit si un article est jouable.
    '''
     # GIVEN : initialisation du test

    article = ArticleGeneration(0, [{"article":"Lyon","views":44892,"rank":664}])

    # WHEN : méthode à tester

    val = article.validation()

    # THEN : ce qu'on veut tester

    self.assertTrue(val)


def test_get_links(self):
    # À FAIRE

    '''
    Fonction testant la méthode "get_links" qui est censée renvoyer la liste des liens hypertextes d'un article.
    '''
    # GIVEN : initialisation du test


    # WHEN : méthode à tester


    # THEN : ce qu'on veut tester


def test_get_summary(self):
    # À FAIRE

        '''
        Fonction permettant de tester la méthode "get_summary" qui est censée renvoyer le résumé de la page.
        '''
    # GIVEN : initialisation du test


    # WHEN : méthode à tester


    # THEN : ce qu'on veut tester


def test_get_categories(self):
    # À FAIRE

    '''
    Fonction permettant de tester la méthode "get_categories" qui est censée récupérer les catégories et portails de la page.
    '''
   # GIVEN : initialisation du test


    # WHEN : méthode à tester


    # THEN : ce qu'on veut tester