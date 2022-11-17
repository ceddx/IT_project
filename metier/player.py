from metier.game import Game
from metier.history import History
from typing import Text

class Player:
    '''
    Classe permettant d'identifier un joueur.
    '''

    def __init__(self, id_player, name, email, password):
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
        self.id_player = id_player
        self.name = name
        self.email = email
        self._password = password
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




    