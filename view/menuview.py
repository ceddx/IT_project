from view.abstract_view import AbstractView
from PyInquirer import *
from  view.session import Session

class MenuView(AbstractView):
    '''
    Classe permettant l'affichage du menu principal du jeu. À partir de ce menu, le joueur peut commencer une partie,
    consulter son historique, de déconnecter ou bien quitter le jeu.
    '''
    def __init__(self):
        self.questions = [
            {
                'type': 'list',
                'name': 'menu',
                'message': 'Choose an option ',
                'choices': [
                    'My history',
                    Separator(),
                    'Play',
                    Separator(),
                    'Logout',
                    Separator(),
                    'Quit'
                ]
            }
        ]

    def display_info(self):
        pass

    def make_choice(self):
        answer = prompt(self.questions)
        if answer['menu'] == 'My history':
            next_view= "History"
        elif answer['menu'] == 'Play':
            next_view = "PlayGame"
        elif answer['menu'] == 'Quit':
            next_view = "Quit"
        elif answer['menu']=='LogOut':
            Session().login_check = False
            Session().player_name = None
            next_view = "StartView"
        return next_view

