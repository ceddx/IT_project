from view.abstract_view import AbstractView
from PyInquirer import Separator, prompt, Validator, ValidationError
from view.session import Session
from metier.player import Player
from pprint import pprint

class Validation(Validator):
    '''
    Classe permettant de vérifier que le mot de passe est bien celui associé au pseudo.
    '''
    def validate(self, player : Player, mdp):
        ok = player._password == mdp
        if not ok:
            raise ValidationError(
                message = 'Incorrect email or password')


class LoginView(AbstractView):
    '''
    Classe permettant à un joueur enregistré de se connecter.
    '''
    def __init__(self):
        self.__questions = [
            {
                'type': 'input',
                'name': 'email',
                'message': 'Enter your email',
            },
            {
                'type': 'input',
                'name': 'password',
                'message': 'Enter your password',
                'validate': Validation
            }
        ]

    def display_info(self):
        """
        Méthode qui va juste déterminer l'affichage en console.
        """
        print(f"Hello {Session().player.name}, you are now connected.")

    def make_choice(self):
        """
        Méthode qui va gérer les choix de l'utilisateur et l'envoyer vers une autre page.
        """
        answers = prompt(self.__questions)
        pprint(answers)
        from view.start_view import StartView
        return StartView()

