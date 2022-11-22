from pprint import pprint
from PyInquirer import  prompt
from view.abstract_view import AbstractView
from view.session import Session
from dao.PlayerDao import PlayerDao
from metier.player import Player
from werkzeug.security import generate_password_hash


class SignupView(AbstractView):
    '''
    Classe permettant d'afficher le menu de notre application permettant à un joueur de se créer un compte.
    '''
    def __init__(self):
        self.questions = [
            {
                'type': 'input',
                'name': 'PlayerName',
                'message': 'What\'s your PlayerName',
                'when': lambda answers: not answers['quit']
            },
            {
                'type': 'input',
                'name': 'email',
                'message': 'What\'s your email',
                'when': lambda answers: not answers['quit']
            },
            {
                'type': 'password',
                'name': 'password',
                'message': 'What\'s your password.',
                'when': lambda answers: not answers['quit']
            },
            {
                'type': 'confirm',
                'name': 'quit',
                'message': 'Turn Back ?',
                'default': False

            },
        ]

    def display_info(self):
        """
        Méthode qui va juste déterminer l'affichage en console.
        """
        print(f"Hello {Session().player.name}")

    def make_choice(self):
        """
        On vérifie que l'identifiant choisi et que l'adresse mail entrée sont uniques
        On oblige l'utilisateur à remplir tout les champs
        """
        reponse = prompt(self.questions)
        if reponse['Quit']:
            return "Start"
        if reponse['PlayerName'] in PlayerDao().get_all_players_name(): 
            print("Player name already used, try a different one")
            return "SignUp"
        if reponse['email'] in PlayerDao().get_all_emails() : 
            print("email adress already used, try a different one")
            return "SignUp"
        if  reponse['id']=="" or  reponse['mail']=="" or reponse['mdp']=="":
            print("Fill in all the fields")
            next_view = "SignUp"
        else:
            new_player = PlayerDao(reponse['PlayerName'], reponse['email'],generate_password_hash(reponse['mdp']))
            PlayerDao().add_player(new_player)
            Session().login_check = True
            Session().player_name = reponse['PlayerName']
            next_view = "Menu"
        return next_view
