class History:
    '''
    Classe permettant de définir l'historique d'un joueur sur une partie jouée.
    '''
    def __init__(self, id_history, id_player, score, speed, difficulty, classement, article):
        '''
        Initialisation d'un historique.

        Paramètres :
        -------------
        id_history : int
            identifiant de l'historique
        id_player : int
            identifiant du joueur correspondant à l'historique
        score : int
            score du joueur
        speed : float
            vitesse du joueur pour trouver la bonne réponse
        difficulty : int
            difficulté de l'article à trouver
        classement : int
            rang du joueur dans le classement
        article : str
            titre de l'article cible
        '''
        self.id_history = id_history
        self.id_player = id_player
        self.score = score
        self.speed = speed
        self.difficulty = difficulty
        self.classement = classement
        self.article = article