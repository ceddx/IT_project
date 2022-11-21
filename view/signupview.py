from pprint import pprint
import regex
from PyInquirer import  prompt
from prompt_toolkit.validation import ValidationError, Validator
from view.abstract_view import AbstractView
from view.session import Session
from werkzeug.security import generate_password_hash

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

class SignupView(AbstractView):
    '''
    Classe permettant d'afficher le menu de notre application permettant à un joueur de se créer un compte.
    '''
    def __init__(self):
        self.__questions = [
            {
                'type': 'input',
                'name': 'PlayerName',
                'message': 'What\'s your ID',
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
            },
            {
                'type': 'input',
                'name': 'Quit',
                'message': 'Return to the main menu?',
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
        if reponse['PlayerName'] in PlayerDao().find_all_players(): 
            print("Player name already used, try a different one")
            return "Sign Up"
        if reponse['email'] in PlayerDao().get_emails() : 
            print("email adress already used, try a different one")
            return "Sign Up"
        if  reponse['id']=="" or  reponse['mail']=="" or reponse['mdp']=="":
            print("Fill in all the fields")
            next_view = "Sign Up"
        else:
            new_player = Player(reponse['PlayerName'], reponse['email'],generate_password_hash(reponse['mdp']))
            PlayerDao().add_user(new_user)
            Session().is_connected = True
            Session().player_name = reponse['PlayerName']
            next_view = "Start"
        return next_view
