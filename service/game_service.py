class GameService:
    '''
    Classe permettant de gérer le jeu.
    '''
    def __init__(self):
        '''
        Initialisation des attributs.
        '''
        pass


    def first_task(self,clue : list):
        """_summary_

        Parameters
        ----------
        clue : list
            _description_

        Returns
        -------
        _type_
            _description_
        """
        
        return ["Use this hint to guess the article: {} ".format(clue[-1]),clue[-1]]


    def next_task(self,clue : list,previous_clue):
        """permet de générer les indices apres que le premier indice soit donné

        Parameters
        ----------
        clue : list
            liste d'indice
        previous_clue : string
            indice précédent

        Returns
        -------
        liste
            avec comme premier element 
        """
        index= clue.index(previous_clue)
        return ["Use this new hint to guess the article: {}".format(clue[index-1]), clue[index-1]]
    
    
    
        
        
        
        


        
