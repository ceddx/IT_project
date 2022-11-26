from PyInquirer import prompt
from view.abstract_view import AbstractView


class StartView(AbstractView):
    '''
    Classe permettant d'afficher le menu principal de notre application.
    '''

    def __init__(self):
        self.questions = [
            {
                'type': 'list',
                'name': 'choices',
                'message': 'Menu',
                'choices': [
                    'Sign Up', 'Log In', 'Play Without Logging In',
                    'Quit'
                ]
            }
        ]

    def display_info(self):
        with open('graphical_assets/banner.txt', 'r', encoding="utf-8") as asset:
            print(asset.read())

    def make_choice(self):
        """
        En utilisant les flèches vous pouvez soit se créer un compte, se connecter, jouer en session invité ou
        bien de quitter.

        """
        answer = prompt(self.questions)
        if answer['choices'] == 'Sign Up':
            next_view = "SignUp"
        elif answer['choices'] == 'Log In':
            next_view = "Login"
        elif answer['choices'] == 'Play Without Logging In':
            next_view = "PlayGame"
        elif answer['choices'] == 'Quit':
            next_view = "Quit"
        return next_view
