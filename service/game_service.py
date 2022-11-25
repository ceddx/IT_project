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


    def first_task(self,article:Article):
        
        return ["Use this hint to guess the article: {} ".format(article.get_clue()[-1]),article.get_clue()[-1]]


    def next_task(self,article:Article,previous_clue):
        index= article.get_clue().index(previous_clue)
        return ["Use this new hint to guess the article: {}".format(article.get_clue()[index-1]), article.get_clue()[index-1]]
    
    
    
        
        
        
        


        
