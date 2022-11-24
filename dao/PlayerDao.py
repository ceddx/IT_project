from dao.db_connection import DBConnection
from metier.player import Player
from util.singleton import Singleton



class PlayerDao(metaclass=Singleton):
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
        list_of_players = []

        with DBConnection().connection as connection:
            with connection.cursor() as cursor:
                cursor.execute("SELECT * FROM Players")
                res = cursor.fetchall()
        if res:
            for row in res:
                player = Player(
                    row['id_player'],
                    row["player_name"],
                    row["email"],
                    row['pass_word'])
                list_of_players.append(player)
        return list_of_players

    def get_all_players_name(self):
        '''
        Méthode renvoyant la liste des noms de tous les joueurs enregistrés.

        Return :
        ---------
        l : list
            liste de noms
        '''
        list_of_players_name = []
        l=self.find_all_players()
        for x in l:
            list_of_players_name+=x.name
        return list_of_players_name

    def get_all_emails(self):
        '''
        Méthode renvoyant la liste des adresses email de tous les joueurs enregistrés.

        Return :
        ---------
        l : list
            liste d'emails
        '''
        list_of_players_email = []
        l = self.find_all_players()
        for x in l:
            list_of_players_email+=x.email
        return list_of_players_email
        

    def find_player_by_id(self, id):
        '''
        Méthode renvoyant les informations d'un joueur enregistré à partir de son identifiant.

        Paramètre :
        ------------
        id : int
            identifiant du joueur en question

        Return :
        ---------
        player : Player
            joueur correspondant à l'identifiant donné
        '''
        with DBConnection().connection as connection:
            with connection.cursor() as cursor:
                cursor.execute(
                    "SELECT * FROM Players WHERE id_player=%(id)s", {"id": id})
                observation = cursor.fetchone()
            player = None
        if observation:
            player = Player(
                observation['id_player'],
                observation["player_name"],
                observation["email"],
                observation['pass_word'])
        return player
    
    def find_player_by_playername(self, player_name :str):
        '''
        Méthode renvoyant la liste des informations d'un joueur enregistré à partir de son nom.

        Paramètre :
        ------------
        player_name : str
            nom du joueur en question

        Return :
        ---------
        player : Player
            joueur correspondant au nom donné
        '''
        with DBConnection().connection as connection:
            with connection.cursor() as cursor :
                cursor.execute(
                    "SELECT * from Players WHERE player_name=%(player_name)s ;"
                , {"player_name" : player_name})
                res = cursor.fetchone()
       
        player1=None
        
        if res :
            
            player1=Player(res["id_player"],
            res["player_name"],
            res["email"],
            res['pass_word'])
           
        return player1

    def update_player(self, player: Player) -> bool:
        '''
        Méthode permettant de modifier les informations d'un joueur.

        Paramètre :
        ------------
        player : Player
            joueur dont on veut modifier les informations

        Return :
        ---------
        updated : Bool
            booléen valant True si la modification a bien été effectuée, False si le joueur n'est pas enregistré
        '''
        updated = False
        player1 = PlayerDao().find_player_by_id(player.id_player)
        if player1 is None:
            return updated
        with DBConnection().connection as connection:
            with connection.cursor() as cursor:
                cursor.execute("UPDATE Players SET"
                            " player_name = %(player_name)s"
                            ",email = %(email)s"
                            ",pass_word = %(password)s"
                            " WHERE id_player = %(id_player)s;",
                            {"player_name": player.name,
                                "email": player.email,
                                "password": player.password,
                                "id_player": player.id_player})
                if cursor.rowcount:
                    updated = True
        return updated

    def add_player(self, player: Player) -> bool:
        '''
        Méthode permettant d'ajouter un joueur dans la base de données.

        Paramètre :
        ------------
        Player : Player
            joueur que l'on veut insérer dans la base de données

        Return :
        ---------
        created : bool
            booléen valant Tru si le joueur a bien été créé 

        '''
        created = False
        with DBConnection().connection as connection:
            with connection.cursor() as cursor:
                cursor.execute(
                    "INSERT into Players(player_name,email,pass_word)"\
                    "VALUES (%(player_name)s, %(email)s,%(password)s)"\
                    "RETURNING id_player", {
                        "player_name": player.name, "email": player.email, "password": player.password})
                res = cursor.fetchone()
        if res:
            player.id_player = res["id_player"]
            created = True
        return created