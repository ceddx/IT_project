from unittest import TestCase
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


