from unittest import TestCase
import re
from metier.article_generation import ArticleGeneration
from metier.article import Article

def test_is_date_or_number(self):
    '''
    Fonction testant la méthode "is_date_or_number" qui est censée renvoyer si un objet est une date ou un nombre.
    '''
    # GIVEN : initialisation du test

    smth = 25

    # WHEN : méthode à tester

    sortie = self.is_date_or_number(smth)

    # THEN : ce qu'on veut tester

    self.assertEqual(True, sortie)


def test_select_clue(self):
    # À FAIRE
    '''
    Fonction testant la méthode "select_clue" qui est censée renvoyer la liste des indices à proposer pour faire deviner un article.
    '''
    # GIVEN : initialisation du test


    # WHEN : méthode à tester


    # THEN : ce qu'on veut tester
