from metier.game import Game
from metier.player import Player
import random
import staticmethod

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
        '''
        self.game = Game
        self.score = score
        self.clue = random.choice(self.game.clues)
    def first_instruction(self):
        '''
        Méthode permettant de mettre en oeuvre une partie.
        '''
        return "Take this hint to guess the article: {} ".format(self.clue)
        ###### on ne voit pas comment instancier cette classe
    @staticmethod
    def get_random_different_element(a,list):
        #on suppose que a est dejà dans la liste
        list.remove(a)
        return random.choice(list)
    def next_instructions(self, response_to_instruction = True):
        first_clue=self.clue
        instruction='Get a hint?'
        print(instruction)
        while response_to_instruction:
            self.score=-1
            a
            first_clue= get_random_different_element(self.clue, self.game.clues)
            print("take this hint {}".format)
            print('Another hint?')
        if self.score<0:
            instruction='Game Over'

        
        


        
