from unittest import TestCase
from metier.game import Game
from metier.player import Player

def test_ask_for_clue(self):
    '''
    Fonction testant la méthode "ask_for_clue", qui est censée renvoyer au joueur le premier élément de la liste d'indices.
    '''
    # GIVEN : initialisation du test

    langue = "français"
    difficulte = 1
    indices = ["animal", "mammifère", "domestique", "équitation"]
    reponse = "cheval"
    partie = Game(langue, difficulte, indices, reponse)

    # WHEN : méthode à tester

    indice_donne = partie.ask_for_clue()

    # THEN : ce qu'on veut tester

    self.assertEqual(indices[0], indice_donne)


def test_make_guess(self):
    '''
    Fonction testant la méthode "make_guess", qui est censée renvoyer True si le joueur a fait une proposition correcte, False sinon.
    '''
    # GIVEN : initialisation du test

    langue = "français"
    difficulte = 1
    indices = ["animal", "mammifère", "domestique", "équitation"]
    reponse = "cheval"
    partie = Game(langue, difficulte, indices, reponse)
    proposition_joueur = "cheval"

    # WHEN : méthode à tester

    guess = partie.make_guess(proposition_joueur)

    # THEN : ce qu'on veut tester

    self.assertEqual(True, guess)





