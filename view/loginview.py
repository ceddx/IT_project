from view.abstract_view import AbstractView
from PyInquirer import Separator, prompt, Validator, ValidationError
from view.session import Session
from metier.player import Player
from dao.PlayerDao import PlayerDao
from pprint import pprint

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
                'name': 'player name',
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
        player = PlayerDao().find
        if answer['cancel'] == 'Yes':
            return "Start view"


