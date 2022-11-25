from view.abstract_view import AbstractView
from PyInquirer import *
from dao.historydao import HistoryDao
from dao.PlayerDao import PlayerDao
from view.session import Session

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
                    'History',
                    Separator(),
                     'Statistics'
                ]
            }
        ]

    def display_info(self):
        pass

    def make_choice(self):
        answer=prompt(self.questions)
        player=PlayerDao().find_player_by_playername(Session().player_name)
        if answer['history']=='History':
            history=HistoryDao().find_player_history(player)
            if history==[]:
                print("You don't have a history yet")
            else:
                for x in history:
                    
                    dict_history={}
                    dict_history["score"]= x.score
                    dict_history["attempts"]=x.number_of_attempts
                    dict_history["article"]=x.article
                    print(dict_history)

        if answer['history']=='Statistics':
            best_score= HistoryDao().get_best_score(player)
            if best_score is not None:
                print("Your best score is: ", best_score)
            lowest_number_of_attempts= HistoryDao().get_lowest_number_of_attempts(player)
            if lowest_number_of_attempts is not None:
                print("Your lowest number of attempts is: ", lowest_number_of_attempts)
        return "Menu"
                    
                
                


        