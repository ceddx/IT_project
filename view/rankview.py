from view.abstract_view import AbstractView
from PyInquirer import prompt, Separator
from service.history_service import HistoryService
from metier.history import History

class RankView(AbstractView):
    '''
    Classe permettant d'afficher le classement des meilleurs scores.
    '''
    def __init__(self):
        self.classement_scores = \
            HistoryService.find_rank_scores() ;
        self.classement_vitesses = \
            HistoryService.find_rank_speeds() ;
        self.__questions = [
            {
                'type': 'list',
                'name': 'choice',
                'message': 'Here is the top 100 best scores.',
                'choices': [
                    'return to menu'
                    , 'try to do better'
                ]
            }
        ]

    def display_info(self):
        """
        Méthode qui va juste déterminer l'affichage en console.
        """
        pass

    def make_choice(self):
        """
        Méthode qui va gérer les choix de l'utilisateur et l'envoyer vers une autre page.
        """
        reponse = prompt(self.__questions)
        if reponse["choice"] == "return to menu":
            from view.start_view import StartView
            return StartView
        elif reponse["choice"] == "try to do better":
            from view.gameview import Gameview
            return Gameview
            
