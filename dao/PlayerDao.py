class PlayerDao:
    def __init__(self):
        pass
    def find_all_players(self):
        l=[]
        connection = DBConnection().connection
        with connection.cursor() as cursor :
                cursor.execute("SELECT * FROM Player")
                observation = cursor.fetchone()
                while observation is not None:
                    l.append(observation)
                    observation = cursor.fetchone()
        return l


    def get_names(self):
        l=[]
        connection = DBConnection().connection
        with connection.cursor() as cursor :
                cursor.execute("SELECT name FROM Player")
                observation = cursor.fetchone()
                while observation is not None:
                    l.append(observation)
                    observation = cursor.fetchone()
        return l
    def get_emails(self):
        l=[]
        connection = DBConnection().connection
        with connection.cursor() as cursor :
                cursor.execute("SELECT email FROM Player")
                observation = cursor.fetchone()
                while observation is not None:
                    l.append(observation)
                    observation = cursor.fetchone()
        return l
    def find_player_by_id(self,id):
        connection = DBConnection().connection
        with connection.cursor() as cursor :
                cursor.execute("SELECT id_player FROM Player where id_player=%(id)s",{"id":id})
                observation = cursor.fetchone()
        return observation
    def find_player_by_name(self,name):
        connection = DBConnection().connection
        with connection.cursor() as cursor :
                cursor.execute("SELECT name FROM Player where name=%(name)s",{"name":name})
                observation = cursor.fetchone()
        return observation
    def update_player(self):
        pass
    def add_player(self):
        connection = DBConnection().connection
        with connection.cursor() as cursor :
            curseur.execute("SELECT id_player FROM Player ORDER BY DESC")
            last_id=cursor.fetchone()
            Player.id+=last_id
        with connection.cursor() as cursor :
            curseur.execute("INSERT into Player (id_player,name,email,password)"
                            "VALUES (%(id_player)s, %(name)s, %(email)s),%(password)s"
                            ,{"id_player":Player.id,
                              "name":Player.name,
                              "email":Player.email,
                              "password":Player.password
                            })
            observation = cursor.fetchone()
            
        return Player


