from view.abstract_view import AbstractView
from PyInquirer import *

class ChangeOrRetryView(AbstractView):
    def __init__(self):
        self.questions = [
            {
                'type': 'list',
                'name': 'change',
                'message': 'Incorrect PlayerName or password',
                'choices': [
                    'New password?',
                    Separator(),
                    'Try again',
                    Separator(),
                    'Back to Menu?'
                ]
            }
        ]

    def display_info(self):
        pass

    def make_choice(self):
        answer = prompt(self.questions)
        if answer['change'] == 'Abandonner':
            next_view = "Start"
        if answer['change'] == "Réessayer":
            next_view = "Login"
        if answer['change']== "New password?":
            next_view = "Update"
        return next_view