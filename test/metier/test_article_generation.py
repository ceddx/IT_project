from unittest import TestCase
from metier.article_generation import ArticleGeneration

def test_get_title(self):
    '''
    Fonction permettant de tester la méthode "get_title" qui donne le titre d'un article.
    '''
    # GIVEN : initialisation du test
    
    article = ArticleGeneration(0, [{"article":"Cookie_(informatique)","views":177667567,"rank":1}])

    # WHEN : méthode à tester

    titre = article.get_title(self)

    # THEN : ce qu'on veut tester

    self.assertEqual("Cookie (informatique)", titre)


def test_get_views(self):
    '''
    Fonction permettant de tester la méthode "get_views" qui donne le nombre de vues d'un article.
    '''
    # GIVEN : initialisation du test

    article = ArticleGeneration(0, [{"article":"Cookie_(informatique)","views":177667567,"rank":1}])

    # WHEN : méthode à tester

    vues = article.get_views(self)

    # THEN : ce qu'on veut tester

    self.assertEqual(177667567, vues)

