from PyInquirer import Separator, prompt

from view.abstract_view import AbstractView
from view.session import Session




class StartView(AbstractView):

    def __init__(self):
        self.__questions = [
            {
                'type': 'list',
                'name': 'choix',
                'message': f'Bonjour {Session().user_name}',
                'choices': [
                    'Next'
                    , 'Checkbox example'
                    , 'Sign In example'

                ]
            }
        ]

    def display_info(self):
        with open('graphical_assets/banner.txt', 'r', encoding="utf-8") as asset:
            print(asset.read())

    def make_choice(self):
        reponse = prompt(self.__questions)
        if reponse['choix'] == 'Next':
            pass
        elif reponse['choix'] == 'Checkbox example':
            from view.checkbox_example_view import CheckBoxExampleView
            return CheckBoxExampleView()
        elif reponse['choix'] == 'Sign In example':
            from view.sign_in_example import SignInExample
            return SignInExample()

