from metier.game import Game
from metier.player import Player

def test_ask_for_clue(self):
    #GIVEN
    langue = "français"
    difficulte = 1
    indices = ["animal", "mammifère", "domestique", "équitation"]
    reponse = "cheval"
    partie = Game(langue, difficulte, indices, reponse)
    #WHEN
    indice_donne = partie.ask_for_clue()
    #THEN
    self.assertEqual(reponse, indice_donne)