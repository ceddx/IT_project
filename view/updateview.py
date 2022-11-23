from view.abstract_view import AbstractView
from PyInquirer import *
from werkzeug.security import generate_password_hash
from dao.PlayerDao import PlayerDao
from metier.player import Player

class UpdateView(AbstractView):
    '''
    Classe permettant à un joueur de modifier son mot de passe.
    '''
    def __init__(self):
        self.questions = [
            {
                'type': 'confirm',
                'name': 'cancel',
                'message': 'cancel the operation',
                'default': False
            },
            {
                'type': 'input',
                'name': 'PlayerName',
                'message': 'Enter your PlayerName',
                'when': lambda answers: not answers['cancel']
            },
            {
                'type': 'password',
                'name': 'password',
                'message': 'Enter your new password.',
                'when' : lambda answers: not answers['cancel']
            }
        ]

    def display_info(self):
        pass

    def make_choice(self):
        """
        Méthode qui va gérer les choix de l'utilisateur et l'envoyer vers une autre page.
        """
        answer=prompt(self.questions)
        player = PlayerDao().find_player_by_playername(answer['PlayerName'])
        if answer['cancel']:
            return "Start"
        if answer['PlayerName'] =="" or answer['password'] =="":
            print("Fill in all the fields")
            return "Update"
        else:
            player_updated=Player(player.id_player,player.name,player.email,generate_password_hash(player.password))
            if PlayerDao().update_player(player_updated):
                print("Your password is updated")
                
        return "Login"
        
    
        
        