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
            curseur.execute("INSERT into History (id_player,name,email,password)"
                            "VALUES (%(id_player)s, %(name)s, %(email)s),%(password)s"
                            ,{"id_player":Player.id,
                              "name":Player.name,
                              "email":Player.email,
                              "password":Player.password
                            })
            observation = cursor.fetchone()
    def get_best_vitesse(self):
        pass
    def get_best_score(self):
        pass
    def update_score(self):
        pass