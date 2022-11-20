from metier.game import Game
from metier.player import Player
import random

class GameService:
    '''
    Classe permettant de gérer le jeu.
    '''
    def __init__(self, game, score=20):
        '''
        Initialisation des attributs.

        Paramètres
        -------------
        game : Game
            Une partie du jeu
        score : int
            Score du joueur
        '''
        self.game = Game
        self.score = score
        self.clues = self.game.clues
        self.first_clue= random.choice(self.clues)


    def first_instruction(self):
        '''
        Méthode permettant de donner le premier indice d'une partie.

        Returns:
        ----------
        hint : str
            Le premier indice que va recevoir le joueur
        '''
        return ["Take this hint to guess the article: {} ".format(self.first_clue), self.first_clue]


    def next_instructions(self, previous_clue):
        '''
        Méthode permettant de donner les indices autres que le tout premier au joueur.

        Paramètres :
        ------------
        previous_clue : str
            Le précédent indice qui a été donné

        Returns :
        ----------
        hint : str
            Un indice donné au joueur
        '''
        new_clues= self.clues.remove(previous_clue)
        return ["Take this new hint to guess the article: {}".format(random.choice(new_clues)), random.choice(new_clues)]
    
    
    
        
        
        
        


        
