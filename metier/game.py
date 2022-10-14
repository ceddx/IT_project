class Game:
    '''
    Classe modélisant une partie du jeu.
    '''
    def __init__(self, language, difficulty, clues, answer):
        '''
        Initialisation d'une partie.

        Paramètres :
        -------------
        language : str
            langue du jeu et de l'article à deviner
        difficulty : int
            difficulté de l'article à trouver
        clues : list
            liste des indices qui seront proposés au joueur pour deviner le titre de l'article
        answer : str
            titre de l'article à trouver, correspond à la réponse que doit donner le joueur pour gagner
        '''
        self.language = language
        self.difficulty = difficulty
        self.clues = clues
        self.answer = answer