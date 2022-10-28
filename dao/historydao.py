from db_connection import DBConnection
from metier.history import History

class HistoryDao:
    '''
    Classe qui gère le lien avec la base de données stockant l'historique des joueurs.
    '''

    def __init__(self):
        pass
    
    def find_player_history(self,id_player):
        '''
        Méthode permettant de trouver l'historique d'un joueur à partir de son identifiant.

        Paramètres :
        -------------
        id_player : int
            identifiant unique du joueur dont on veut récupérer l'historique

        Return :
        ----------
        history : list
            Liste contenant toutes les informations de l'historique du joueur.
        '''
        with DBConnection().connection as connection:
            history = []
            with connection.cursor() as cursor :
                cursor.execute("SELECT id_player FROM History where id_player=%(id)s",{"id":id_player})
                observation = cursor.fetchone()
                while observation is not None:
                    history.append(observation)
                    observation = cursor.fetchone()
        return history

    def add_history(history):
        '''
        Méthode qui ajoute un historique.

        Paramètres :
        -------------
        history : History
            historique à ajouter

        '''
        connection = DBConnection().connection
        with connection.cursor() as cursor :
            cursor.execute("SELECT id_player FROM History ORDER BY DESC")
            last_id=cursor.fetchone()
            id_history+=last_id
        with connection.cursor() as cursor :
            cursor.execute("INSERT into History (id_history,id_player,score,speed,difficulty,article_name)"
                            "VALUES (%(id_history)s, %(id_player)s, %(score)s,%(speed)s,%(difficulty)s,%(article_name)s",
                            {"id_history":History.id_history,
                              "id_player":History.id_player,
                              "score":History.score,
                              "speed":History.speed,
                              "difficulty":History.difficulty,
                              "article_name":History.article_name
                            })
        
    def get_best_vitesse(self):
        '''
        Méthode permettant de renvoyer la meilleure vitesse avec laquelle un joueur a gagné une partie.

        Return:
        ----------
        observation : float
            maximum de toutes les vitesses
        '''
        connection = DBConnection().connection
        with connection.cursor() as cursor:
            cursor.execute("SELECT MAX(*) vitesse FROM History")
            observation = cursor.fetchone()
        return observation

    def get_best_score(self):
        '''
        Méthode permettant de renvoyer le meilleur des scores.

        Return :
        ---------
        observation : int
            maximum de tous les scores
        '''
        connection = DBConnection().connection
        with connection.cursor() as cursor:
            cursor.execute("SELECT MAX(*) score FROM History")
            observation = cursor.fetchone()
        return observation
    
    def update_score(self):
        '''
        Méthode permettant de mettre à jour un score.
        '''
        pass
    