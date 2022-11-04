from metier.game import Game
from metier.player import ask_for_clue

class GameService:
    '''
    Classe permettant de gérer le jeu.
    '''
    def __init__(self, game):
        '''
        Initialisation des attributs.

        Paramètres
        -------------
        game : Game
            Une partie du jeu
        '''
        self.game = game

    def generate_game(self):
        '''
        Méthode permettant de mettre en oeuvre une partie.
        '''
        ###### on ne voit pas comment instancier cette classe