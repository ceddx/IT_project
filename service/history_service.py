from dao.historydao import HistoryDao
from metier.history import History
from util.singleton import Singleton
from dao.playerdao import PlayerDao


class HistoryService(metaclass=Singleton):
    '''
    Classe qui gère l'historique des joueurs.
    '''
    def __init__(self):
        pass

    def find_player_history(self):
        '''
        Méthode permettant de trouver l'historique d'un joueur.
        '''
        History()
        HistoryDao.find_player_history(self, id, name)
        
    def find_classement(self):
        '''
        Méthode permettant de renvoyer le classement des 100 meilleurs joueurs ainsi que leur score.
        '''
        players = PlayerDao.get_all_players(self).id_player
        classement = []
        scores = []
        for i in players:
            scores.append(HistoryDao.get_best_score(self, id = i))
        j = 0
        while len(classement) < 100:
            for k in range(len(classement)):
                if scores[j] > classement[k]:
                    classement.append(scores[j])
                    break
            j = j + 1
        return classement
