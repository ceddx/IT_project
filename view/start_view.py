from PyInquirer import prompt
from view.abstract_view import AbstractView
from view.session import Session


class StartView(AbstractView):

    def __init__(self):
        self.__questions = [
            {
                'type': 'list',
                'name': 'choix',
                'message': f'Bonjour {Session().player_name}',
                'choices': [
                    'se créer un compte'
                    , 'se connecter'
                    , 'jouer sans se connecter'

                ]
            }
        ]

    def display_info(self):
        """
        Méthode qui va juste déterminer l'affichage en console.
        """
        with open('graphical_assets/banner.txt', 'r', encoding="utf-8") as asset:
            print(asset.read())

    def make_choice(self):
        """
        Méthode qui va gérer les choix de l'utilisateur et l'envoyer vers une autre page.
        """
        reponse = prompt(self.__questions)
        if reponse['choix'] == 'se créer un compte':
            from view.signupview import SignupView
            return SignupView()
        elif reponse['choix'] == 'se connecter':
            from view.loginview import loginView
            return loginView()
        elif reponse['choix'] == 'jouer sans se connecter':
            from view.gameview import GameView
            return GameView()
