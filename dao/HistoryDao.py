from db_connection import DBConnection

class HistoryDao:
    def __init__(self):
        pass
    def find_player_history(self,id,name):
        connection = DBConnection().connection
        with connection.cursor() as cursor :
                cursor.execute("SELECT id_player,name FROM History where id_player=%(id)s OR name=%(name)s",{"id":id,"name":name})
                observation = cursor.fetchone()
        return observation

    def add_history(history):
        connection = DBConnection().connection
        with connection.cursor() as cursor :
            curseur.execute("SELECT id_player FROM History ORDER BY DESC")
            last_id=cursor.fetchone()
            id_history+=last_id
        with connection.cursor() as cursor :
            curseur.execute("INSERT into History (id_history,id_player,score,speed,difficulty,article_name)"
                            "VALUES (%(id_history)s, %(id_player)s, %(score)s),%(speed)s,%(difficulty)s,%(article_name)s"
                            ,{"id_history":History.id_history,
                              "id_player":History.id_player,
                              "score":History.score,
                              "speed":History.speed,
                              "difficulty":History.difficulty,
                              "article_name":History.article_name
                            })
            observation = cursor.fetchone()
        return history
    def get_best_vitesse(self):
        connection = DBconnection().connection
        with connection.cursor() as cursor:
            
    def get_best_score(self):
        pass
    def update_score(self):
        pass