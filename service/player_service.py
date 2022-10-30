class PlayerService:
    '''
    Classe gérant les informations relatives aux joueurs.
    '''

    def __init__(self):
        pass

    def login_check(self, id_player, password):
        '''
        Méthode permettant de vérifier qu'un joueur a entré le bon mot de passe pour se connecter.

        Paramètres :
        -------------
        id_player : int
            identifiant entré par le joueur
        password : str
            mot de passe entré par le joueur

        Returns :
        -----------
        login : Bool
            True si le mot de passe correspond à l'identifiant entré, False sinon.
        '''
        # À COMPLÉTER

    def sign_up(self):
        '''
        Méthode permettant à un joueur de se créer un compte.
        '''
        # À COMPLÉTER

    def update(self, id, new_email, new_name):
        '''
        Méthode permettant à un joueur de mettre à jour ses informations personnelles.

        Paramètres :
        ------------
        id : int
            identifiant du joueur dont les paramètres vont être modifiés
        new_email : str
            nouvelle adresse mail du joueur
        new_name : str
            nouveau nom associé au joueur
        '''
        # À COMPLÉTER
