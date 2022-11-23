from view.abstract_view import AbstractView
from PyInquirer import *
from metier.history import History
from view.session import Session
from dao.PlayerDao import PlayerDao
from dao.historydao import HistoryDao

class SaveHistoryView(AbstractView):
    def __init__(self):
        self.questions = [
            {
                'type': 'list',
                'name': 'saving',
                'message': 'What do you want to do next',
                'choices': [
                    'Replay',
                    Separator(),
                    'Back to menu',
                    Separator(),
                    'Quit'
                ]
            }
        ]
    def display_info(self):
        pass

    def make_choice(self):
        
        score= Session().score
        attempts= Session().number_of_attempts
        secret_article=Session().article
        #on sauvegarde l'historique si le joueur est connecté ( càd qu'il n'est pas en session invité)
        if Session().login_check==True:
            player= PlayerDao().find_player_by_playername(Session)
            history= History(player.id_player,score,attempts,secret_article)
            HistoryDao().add_history(history)

        Session().score=0
        Session().number_of_attempts=0
        Session().article= None

        answer=prompt(self.questions)
        if answer['saving']=='Replay':
            next_view= "PlayGame"
        if answer['saving']=='Back to menu':
            if Session().login_check==True:
                next_view="Menu"
            else:
                next_view="Start"
        else:
            next_view="Quit"
        return next_view

        



        


            
