class History:
    '''
    Classe permettant de définir l'historique d'un joueur sur une partie jouée.
    '''
    def __init__(self,*args):
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
        if len(args)==5:
            if isinstance(args[0],int):
                self.id_history=args[0]
            if isinstance(args[1],int):
                self.id_player=args[1]
            if isinstance(args[2],int):
                self.score=args[2]
            if isinstance(args[3],int):
                self.speed=args[3]
            if isinstance(args[4],int):
                self.article=args[4]
        else:
            if isinstance(args[0],int):
                self.id_player=args[0]
            if isinstance(args[1],int):
                self.score=args[1]
            if isinstance(args[2],int):
                self.speed=args[2]
            if isinstance(args[3],int):
                self.article=args[3]
