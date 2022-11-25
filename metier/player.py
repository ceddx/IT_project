from metier.game import Game
from metier.history import History
from typing import Text


class Player:
    '''
    Classe permettant d'identifier un joueur.
    '''

    def __init__(self, *args):
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
        if len(args) == 4:
            if isinstance(args[0], int):
                self.id_player = args[0]
            if isinstance(args[1], Text):
                self.name = args[1]
            if isinstance(args[2], Text):
                self.email = args[2]
            if isinstance(args[3], Text):
                self.password = args[3]
        else:
            if isinstance(args[0], Text):
                self.name = args[0]
            if isinstance(args[1], Text):
                self.email = args[1]
            if isinstance(args[2], Text):
                self.password = args[2]

