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
        player_name_inputed=answer['playername']
        password_inputed=answer['password']
        if answer['cancel']:
            return "Start"
        player= PlayerDao().find_player_by_playername(player_name_inputed)
        if player and player_name_inputed==player.name and check_password_hash(player.password,password_inputed):
            Session().login_check=True
            Session().player_name =answer['playername']
            next_view = "Menu"
        else:
            next_view = 'RetryOrChange'
        return next_view
        

