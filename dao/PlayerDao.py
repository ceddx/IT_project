from db_connection import DBConnection

class PlayerDao:
    '''
    Classe qui gère le lien avec la base de données stockant les informations relatives aux joueurs.
    '''
    def __init__(self):
        pass
   
    def find_all_players(self):
        '''
        Méthode permettant de renvoyer l'ensemble des informations de l'ensemble des joueurs.

        Return :
        ---------
        l : list
            liste contenant l'ensemble des informations des joueurs
        '''
        l=[]
        with DBConnection().connection as connection:
            with connection.cursor() as cursor :
                cursor.execute("SELECT * FROM Player")
                observation = cursor.fetchone()
                while observation is not None:
                    l.append(observation)
                    observation = cursor.fetchone()
        return l

    def get_names(self):
        '''
        Méthode renvoyant la liste des noms de tous les joueurs enregistrés.

        Return :
        ---------
        l : list
            liste de noms
        '''
        l=[]
        with DBConnection().connection as connection:
            with connection.cursor() as cursor :
                cursor.execute("SELECT name FROM Player")
                observation = cursor.fetchone()
                while observation is not None:
                    l.append(observation)
                    observation = cursor.fetchone()
        return l

    def get_emails(self):
        '''
        Méthode renvoyant la liste des adresses email de tous les joueurs enregistrés.

        Return :
        ---------
        l : list
            liste d'emails
        '''
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
        '''
        Méthode renvoyant la liste des informations d'un joueur enregistré à partir de son identifiant.

        Paramètre :
        ------------
        id : int
            identifiant du joueur en question

        Return :
        ---------
        observation : list
            liste des informations du joueur
        '''
        connection = DBConnection().connection
        with connection.cursor() as cursor :
                cursor.execute("SELECT * FROM Player WHERE id_player=%(id)s",{"id":id})
                observation = cursor.fetchone()
        return observation

    def find_player_by_name(self,name):
        '''
        Méthode renvoyant la liste des informations d'un joueur enregistré à partir de son nom.

        Paramètre :
        ------------
        name : str
            nom du joueur en question

        Return :
        ---------
        observation : list
            liste des informations du joueur
        '''
        connection = DBConnection().connection
        with connection.cursor() as cursor :
                cursor.execute("SELECT * FROM Player WHERE name=%(name)s",{"name":name})
                observation = cursor.fetchone()
        return observation

    def update_player(self):
        '''
        Méthode permettant de mettre à jour les informations d'un joueur déjà enregistré.
        '''
        pass

    def add_player(Player):
        '''
        Méthode permettant d'ajouter un joueur dans la base de données.

        Paramètre :
        ------------
        Player : Player
            joueur que l'on veut insérer dans la base de données
        '''
        connection = DBConnection().connection
        with connection.cursor() as cursor :
            cursor.execute("SELECT id_player FROM Player ORDER BY DESC")
            last_id=cursor.fetchone()
            Player.id_player+=last_id
        with connection.cursor() as cursor :
            cursor.execute("INSERT into Player (id_player,name,email,password)"
                            "VALUES (%(id_player)s, %(name)s, %(email)s),%(password)s"
                            ,{"id_player":Player.id_player,
                              "name":Player.name,
                              "email":Player.email,
                              "password":Player.password
                            })            

