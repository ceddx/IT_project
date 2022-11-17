from db_connection import DBConnection
from metier.history import History
from metier.player import Player
from dao.PlayerDao import PlayerDao
class HistoryDao:
    '''
    Classe qui gère le lien avec la base de données stockant l'historique des joueurs.
    '''

    def __init__(self):
        pass
    
    def find_player_history(self, player:Player):
        '''
        Méthode permettant de trouver l'historique d'un joueur à partir de son identifiant.

        Paramètres :
        -------------
        player : Player
            Le joueur dont on veut récupérer l'historique

        Return :
        ----------
        history : list[history]
            Liste contenant toutes les informations de l'historique du joueur.
        '''
        with DBConnection().connection as connection:
            with connection.cursor() as cursor :
                cursor.execute("SELECT * FROM History where id_player=%(id)s",{"id":player.id_player})
                res = cursor.fetchall()
                history = []
                if res:
                    for row in res:
                        history1=History(
                            row['id_history'],
                            row["id_player"]
                            ,row["score"]
                            ,row["speed"]
                            ,row["article"]
                        )
                        history.append(history1)
        return history

    def add_history(history:History):
        '''
        Méthode qui ajoute un historique.

        Paramètres :
        -------------
        history : History
            historique à ajouter
        '''
        created = False
        player= PlayerDao().find_player_by_id(history.id_player)
      
        if player is None :
            return created
        with DBConnection().connection as connection:
           
            with connection.cursor() as cursor :
                cursor.execute("INSERT INTO History (id_player,score,speed,article_name)"
                                "VALUES (%(id_player)s, %(score)s,%(speed)s,%(article)s"
                                "RETURNING id_history",
                                {
                                "id_player":History.id_player,
                                "score":History.score,
                                "speed":History.speed,
                                "article":History.article
                                })
                res=cursor.fetchone()
        if res:
            history.id_history=res["id_history"]
            created = True
        return created
        
    def get_best_vitesse(self,X):
        '''
        Méthode permettant de renvoyer les X meilleures vitesses avec laquelle un joueur a gagné une partie.

        Parameters
        ----------
        X : int
            nombre de meilleurs vitesses que l'on veut

        Return:
        ----------
        observation : float
            maximum de toutes les vitesses
        '''
        with DBConnection().connection as connection:
            history=[]
            with connection.cursor() as cursor:
                cursor.execute("SELECT * FROM History order by vitesse desc limit %(nbr_observation)s", {"nbr_observation":X})
                observation = cursor.fetchone()
                for i in range(len(X)):
                    history.append(observation)
                    observation = cursor.fetchone()
        return history

    def get_best_score(self,X):
        '''
        Méthode permettant de renvoyer les X meilleurs scores.

        Parameters
        ----------
        X : int
            nombre de meilleurs scores que l'on veut

        Return :
        ---------
        history : Hystory
            les X meilleurs scores
        '''
        with DBConnection().connection as connection:
            history=[]
            with connection.cursor() as cursor:
                cursor.execute("SELECT * FROM History order by score desc limit %(nbr_observation)s", {"nbr_observation":X})
                observation = cursor.fetchone()
                for i in range(len(X)):
                    history.append(observation)
                    observation = cursor.fetchone()
        return history