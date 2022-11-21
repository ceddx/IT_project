from metier.game import Game
from metier.player import Player
import random

class GameService:
    '''
    Classe permettant de gérer le jeu.
    '''
    def __init__(self,game = Game()):
        '''
        Initialisation des attributs.

        
        '''
        self.game = game
        self.article = self.game.article
        self.clues = self.game.clues
        self.first_clue= random.choice(self.clues)


    def first_task(self):
       
        return ["Use this hint to guess the article: {} ".format(self.first_clue),self.first_clue]
        ###### on ne voit pas comment instancier cette classe


    def next_task(self, previous_clue):
        new_clues= self.clues.remove(previous_clue)
        return ["Use this new hint to guess the article: {}".format(random.choice(new_clues)), random.choice(new_clues)]
    
    
    
        
        
        
        


        
