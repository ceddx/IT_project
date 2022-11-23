from view.abstract_view import AbstractView
from PyInquirer import prompt, Separator
from service.history_service import HistoryService
from metier.history import History

class HistoryView(AbstractView):
    '''
    Classe permettant d'afficher l'historique d'un joueur.
    '''
    def __init__(self):
        self.questions = [
            {
                'type': 'list',
                'name': 'history',
                'message': 'Here is your history.',
                'choices': [
                    'history',
                    Separator(),
                     'Statistics'
                ]
            }
        ]

    def display_info(self):
        pass

    def make_choice(self):
        answer=prompt(self.__questions)

        