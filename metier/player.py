from metier.game import Game
from metier.history import History
from typing import Text

class Player:
    '''
    Classe permettant d'identifier un joueur.
    '''

    def __init__(self,*args):
        '''
        Initialisation des paramètres d'un joueur.

        Paramètres :
        -------------
        id_player : int
            identifiant du joueur
        name : str
            nom du joueur
        email : str
            adresse mail du joueur
        password: str
            mot de passe du joueur
        '''
        if len(args)==5:
            if isinstance(args[0],int):
                self.id_player=args[0]
            if isinstance(args[1],Text):
                self.name=args[1]
            if isinstance(args[2],Text):
                self.email=args[2]
            if isinstance(args[3],Text):
                self.password=hash(args[3])
        else :
            if isinstance(args[0],Text):
                self.name=args[0]
            if isinstance(args[1],Text):
                self.email=args[1]
            if isinstance(args[2],Text):
                self.password=hash(args[3])
    '''
    def ask_for_clue(self):
        
        Méthode permettant au joueur d'obtenir un indice supplémentaire.

        Returns:
        ------------
        clue : str
            indice proposé au joueur
        
        return Game(self).clues.pop(0)

    def get_score(self):
        
        Méthode permettant à un joueur d'obtenir son score.

        Returns :
        -----------
        score : int
            score du joueur
        
        return History(self).score

    def make_guess(self, guess):
        
        Méthode permettant de vérifier si la réponse proposée est correcte.

        Paramètres :
        ------------
        guess : str
            réponse proposée par le joueur
        
        Returns :
        ----------
        est_correct : bool
            booléen valant True si la réponse est correcte, False sinon
        
        return (guess == Game(self).answer)
'''




    