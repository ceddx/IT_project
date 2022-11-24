from view.abstract_view import AbstractView
from PyInquirer import *
from view.session import Session
from dao.PlayerDao import PlayerDao
from werkzeug.security import check_password_hash


class LoginView(AbstractView):
    '''
    Classe permettant à un joueur enregistré de se connecter.
    '''
    def __init__(self):
        self.questions = [
            {
                'type': 'confirm',
                'name': 'cancel',
                'message': 'Do you want to cancel the operation?',
                'default': False
            },
            {
                'type': 'input',
                'name': 'playername',
                'message': 'Enter your player_name',
                'when': lambda answers: not answers['cancel']
            },
            {
                'type': 'password',
                'name': 'password',
                'message': 'Enter your password',
                'when': lambda answers: not answers['cancel']
            }
        ]

    def display_info(self):
        pass

    def make_choice(self):
        """
        Méthode qui va gérer les choix de l'utilisateur et l'envoyer vers une autre page.
        """
        answer= prompt(self.questions)
        if answer['cancel']:
            return "Start"
        player= PlayerDao().find_player_by_playername(answer['playername'])
        if player and (answer['playername']==player.name) and (check_password_hash(player.password,answer['password'])):
            Session().login_check=True
            Session().player_name =answer['playername']
            next_view = "Menu"
        else:
            next_view = 'RetryOrChange'
        return next_view