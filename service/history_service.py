from dao.historydao import HistoryDao
from metier.history import History
from util.singleton import Singleton




class HistoryService(metaclass=Singleton):
    '''
    Classe qui gère l'historique des joueurs.
    '''
    def __init__(self):
        pass

    def get_find_player_history(self):
        '''
        Méthode permettant de trouver l'historique d'un joueur.
        '''
        
        
