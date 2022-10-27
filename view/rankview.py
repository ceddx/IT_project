from view.abstract_view import AbstractView
from PyInquirer import prompt, Separator
from service.history_service import HistoryService

class RankView(AbstractView):
    '''
    Classe permettant d'afficher le classement des meilleurs scores.
    '''
    def __init__(self):
        self.classement = \
            HistoryService.find_classement() ;

    def display_info(self):
        pass

    def make_choice(self):
        pass