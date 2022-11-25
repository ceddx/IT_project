from metier.article import Article

class GameService:
    '''
    Classe permettant de gérer le jeu.
    '''
    def __init__(self):
        '''
        Initialisation des attributs.

        
        '''
        #self.game = Game()
        #self.article = self.game.article
        #self.clues = self.game.clues
        #self.first_clue= self.clues[-1]
        pass


    def first_task(self,clue : list):
        
        return ["Use this hint to guess the article: {} ".format(clue[-1]),clue[-1]]


    def next_task(self,clue : list,previous_clue):
        index= clue.index(previous_clue)
        return ["Use this new hint to guess the article: {}".format(clue[index-1]), clue[index-1]]
    
    
    
        
        
        
        


        
