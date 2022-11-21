from PyInquirer import prompt
from view.abstract_view import AbstractView
from view.session import Session
from view.signupview import SignupView
from view.loginview import loginView
from view.gameview import GameView



class StartView(AbstractView):
    '''
    Classe permettant d'afficher le menu principal de notre application.
    '''

    def __init__(self):
        self.__questions = [
            {
                'type': 'list',
                'name': 'choix',
                'message': f'Hello {Session().player_name}',
                'choices': [
                    'Sign Up'
                    , 'Log In'
                    , 'Play Without Logging In'
                ]
            }
        ]

    def display_info(self):
        
        print("Welcome to Pyramid and the Philosopher game")

    def make_choice(self):
        """
        Méthode qui va gérer les choix de l'utilisateur et l'envoyer vers une autre page.

        """
        reponse = prompt(self.__questions)
        if reponse['choix'] == 'Sign Up':
            next_view="Sign up"
        elif reponse['choix'] == 'Log In':
            next_view="Login"
        elif reponse['choix'] == 'Play Without Logging In':
            next_view="Play Game"
        else:
            next_view="Quit"
        return next_view