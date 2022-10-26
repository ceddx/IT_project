from unittest import TestCase
from metier.article_generation import ArticleGeneration

def test_get_title(self):
    '''
    Fonction permettant de tester la méthode "get_title" qui donne le titre d'un article.
    '''
    # GIVEN : initialisation du test
    
    article = ArticleGeneration(0, [{"article":"Cookie_(informatique)","views":177667567,"rank":1}])

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

    article = ArticleGeneration(0, [{"article":"Stephen_Hawking","views":47663,"rank":610}])

    # WHEN : méthode à tester

    val = article.validation()

    # THEN : ce qu'on veut tester

    self.assertEqual(True, val)


def test_get_links(self):
    '''
    Fonction permettant de tester la méthode "get_links" qui renvoie les liens hypertextes contenus dans un article.
    '''
     # GIVEN : initialisation du test

    article = ArticleGeneration(0, [{"article":"Lyon","views":44892,"rank":66}])

    # WHEN : méthode à tester

    liens = article.get_links()

    # THEN : ce qu'on veut tester

    self.assertEqual([], liens)


