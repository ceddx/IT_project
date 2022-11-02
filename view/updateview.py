from view.abstract_view import AbstractView
from PyInquirer import prompt, Separator
from service.history_service import HistoryService
from metier.history import History
import regex
from prompt_toolkit.validation import ValidationError, Validator
from pprint import pprint
from view.session import Session


class PasswordValidator(Validator):
    def validate(self, document):
        ok = regex.match(
            "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{10,}$", document.text)
        if not ok:
            raise ValidationError(
                message='Please enter a valid password',
                cursor_position=len(document.text)) 

class UpdateView(AbstractView):
    '''
    Classe permettant à un joueur de modifier ses informations.
    '''
    def __init__(self):
        self.__questions = [
            {
                'type': 'input',
                'name': 'name',
                'message': 'Enter your new name',
            },
            {
                'type': 'input',
                'name': 'email',
                'message': 'Enter your new email',
            },
            {
                'type': 'password',
                'name': 'password',
                'message': 'Enter your new password. Your password should be '\
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