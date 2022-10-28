from view.abstract_view import AbstractView
from PyInquirer import prompt, Separator
from service.history_service import HistoryService
from metier.history import History

class updateView(AbstractView):
    '''
    Classe permettant à un joueur de modifier ses informations.
    '''