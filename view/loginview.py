from view.abstract_view import AbstractView
from PyInquirer import *
from view.session import Session
from metier.player import Player
from dao.PlayerDao import PlayerDao
from pprint import pprint
from werkzeug.security import check_password_hash


class LoginView(AbstractView):
    '''
    Classe permettant à un joueur enregistré de se connecter.
    '''
    def __init__(self):
        self.__questions = [
            {
                'type': 'list',
                'name': 'cancel',
                'message': 'Do you want to cancel the operation?',
                'choices':['Yes','No']
            },
            {
                'type': 'input',
                'name': 'Playername',
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
        answer= prompt(self.__questions)
        player = PlayerDao().find_player_by_playername
        playername_inputed= answer['PlayerName']
        password_inputed = answer['password']
        if answer['cancel'] == 'Yes':
            return "Start"
        player= PlayerDao().find_player_by_playername(playername_inputed)
        if player and playername_inputed==player.name and check_password_hash(player.password,password_inputed):
            Session().login_check=True
            Session().player_name =playername_inputed
            next_view = "Menu"
        else:
            next_view = 'RetryOrChange'
        return next_view
        

