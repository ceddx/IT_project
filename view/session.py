from util.singleton import Singleton

class Session(metaclass=Singleton):
    def __init__(self):
        """
        Définition des variables que l'on stocke en session
        Le syntaxe
        ref:type = valeur
        permet de donner le type des variables. Utile pour l'autocompletion.
        """
        self.player_name: str = None
        self.email: str = None
        self.user_mdp: str = None
        self.language: str=None
        self.login_check: str = None
        self.score: str=None
        self.difficulty: str = None
        self.clue: str = None
        self.history : list = []
    