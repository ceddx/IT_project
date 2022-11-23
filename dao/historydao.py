from dao.db_connection import DBConnection
from metier.history import History
from metier.player import Player
from dao.PlayerDao import PlayerDao


class HistoryDao:
    '''
    Classe qui gère le lien avec la base de données stockant l'historique des joueurs.
    '''

    def __init__(self):
        pass

    def find_player_history(self, player: Player):
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
            with connection.cursor() as cursor:
                cursor.execute(
                    "SELECT * FROM History where id_player=%(id)s", {"id": player.id_player})
                res = cursor.fetchall()
        history = []
        if res:
            for row in res:
                history1 = History(
                    row['id_history'],
                    row["id_player"],
                    row["score"],
                    row["attempts"],
                    row["article"])
                history.append(history1)
        return history

    def add_history(self,history: History):
        '''
        Méthode qui ajoute un historique.

        Paramètres :
        -------------
        history : History
            historique à ajouter
        '''
        created = False
        player = PlayerDao().find_player_by_id(history.id_player)

        if player is None:
            return created
        with DBConnection().connection as connection:

            with connection.cursor() as cursor:
                cursor.execute(
                    "INSERT INTO History (id_player,score,attempts,article)"
                    "VALUES (%(id_player)s, %(score)s,%(attempts)s,%(article)s)"
                    "RETURNING id_history",
                    {
                        "id_player": history.id_player,
                        "score": history.score,
                        "attempts": history.number_of_attempts,
                        "article": history.article})
                res = cursor.fetchone()
        if res:
            history.id_history = res["id_history"]
            created = True
        return created


    def get_best_score(self, player:Player):

        list_of_scores=[]
        l=self.find_player_history(player)
        for x in l:
            list_of_scores+=x.score
        if len(list_of_scores):
            return max(list_of_scores)
        else:
            print("You don't have a history yet")


    def get_lowest_number_of_attempts(self, player:Player):
        list_numbers=[]
        list=self.find_player_history(player)
        for history in list:
            list_numbers.append(history.number_of_attempts)
        if len(list_numbers):
            return min(list_numbers)
        else:
            print("You don't have a history yet")

        
