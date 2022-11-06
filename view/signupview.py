from pprint import pprint
import regex
from PyInquirer import  prompt
from prompt_toolkit.validation import ValidationError, Validator
from view.abstract_view import AbstractView
from view.session import Session

class PasswordValidator(Validator):
    '''
    Classe permettant de vérifier qu'un mot de passse est valide.
    '''
    def validate(self, document):
        ok = regex.match(
            "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{10,}$", document.text)
        if not ok:
            raise ValidationError(
                message='Please enter a valid password',
                cursor_position=len(document.text)) 
            ###vérif de majuscule et au moins 10 caractères pas vérifié

class SignIn(AbstractView):
    '''
    Classe permettant d'afficher le menu de notre application permettant à un joueur de se créer un compte.
    '''
    def __init__(self):
        self.__questions = [
            {
                'type': 'input',
                'name': 'name',
                'message': 'What\'s your name',
            },
            {
                'type': 'input',
                'name': 'email',
                'message': 'What\'s your email',
            },
            {
                'type': 'password',
                'name': 'password',
                'message': 'What\'s your password. Your password should be '\
                    'at least 10 characters, with at least one capital letter ' \
                    'one number and one special character',
                'validate': PasswordValidator
            }
        ]

    def display_info(self):
        """
        Méthode qui va juste déterminer l'affichage en console.
        """
        print(f"Hello {Session().player.name}")

    def make_choice(self):
        """
        Méthode qui va gérer les choix de l'utilisateur et l'envoyer vers une autre page.
        """
        answers = prompt(self.__questions)
        pprint(answers)
        from view.start_view import StartView
        return StartView()

