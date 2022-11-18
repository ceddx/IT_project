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
        Méthode permettant de mettre en oeuvre une partie.
        '''
        return ["Take this hint to guess the article: {} ".format(self.first_clue), self.first_clue]
        ###### on ne voit pas comment instancier cette classe


    def next_instructions(self, previous_clue):
        new_clues= self.clues.remove(previous_clue)
        return ["Take this new hint to guess the article: {}".format(random.choice(new_clues)), random.choice(new_clues)]
    
    
    
        
        
        
        


        
