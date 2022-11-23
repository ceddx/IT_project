from util.singleton import Singleton

class Session(metaclass=Singleton):
    def __init__(self):
        """
        Définition des variables que l'on stocke en session
        Le syntaxe
        ref:type = valeur
        permet de donner le type des variables. Utile pour l'autocompletion.
        """
        self.login_check = False
        self.player_name= None
        #self.language: str=None
        self.score=0
        self.number_of_attempts= 0
        self.article= None
    