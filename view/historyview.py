from view.abstract_view import AbstractView
from PyInquirer import prompt, Separator
from service.history_service import HistoryService
from metier.history import History

class HistoryView(AbstractView):
    '''
    Classe permettant d'afficher l'historique d'un joueur.
    '''
    def __init__(self):
        self.__questions = [
            {
                'type': 'list',
                'name': 'choice',
                'message': 'Here is your history.',
                'choices': [
                    'return to menu'
                    , 'try to improve my stats'
                ]
            }
        ]

    def display_info(self):
        """
        Méthode qui va juste déterminer l'affichage en console.
        """
        print(AbstractView.session.history)

    def make_choice(self):
        """
        Méthode qui va gérer les choix de l'utilisateur et l'envoyer vers une autre page.
        """
        reponse = prompt(self.__questions)
        if reponse["choice"] == "return to menu":
            from view.start_view import StartView
            return StartView
        elif reponse["choice"] == "try to improve my stats":
            from view.gameview import Gameview
            return Gameview