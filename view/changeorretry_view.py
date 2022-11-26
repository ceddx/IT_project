from view.abstract_view import AbstractView
from PyInquirer import *


class ChangeOrRetryView(AbstractView):
    '''
    Classe gérant l'affichage en cas de mot de passe incorrect. Le joueur peut alors soit réessayer, soit rentrer un
    nouveau mot de passe, ou soit retourner au menu principal.
    '''

    def __init__(self):
        self.questions = [
            {
                'type': 'list',
                'name': 'change',
                'message': 'Incorrect PlayerName or password',
                'choices': [
                    'New password?',
                    Separator(),
                    'Try again',
                    Separator(),
                    'Back to Menu?'
                ]
            }
        ]

    def display_info(self):
        pass

    def make_choice(self):
        answer = prompt(self.questions)
        if answer['change'] == 'Back to Menu?':
            next_view = "Start"
        elif answer['change'] == "Try again":
            next_view = "Login"
        elif answer['change'] == "New password?":
            next_view = "Update"
        return next_view
