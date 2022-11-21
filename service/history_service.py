from dao.historydao import HistoryDao
from metier.history import History
from util.singleton import Singleton
from dao.PlayerDao import PlayerDao


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
        History()
        HistoryDao.find_player_history(self, id)
        
    def find_rank_scores(self):
        '''
        Méthode permettant de renvoyer le classement des 100 meilleurs joueurs en terme de score. 
        '''
        History()
        HistoryDao.get_best_score(self, 100)

    def find_rank_speeds(self):
        '''
        Méthode permettant de renvoyer le classement des 100 meilleurs joueurs en terme de vitesse. 
        '''
        History()
        HistoryDao.get_best_vitesse(self, 100)
