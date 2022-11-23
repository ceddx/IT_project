from view.abstract_view import AbstractView
from PyInquirer import prompt, Separator
from service.history_service import HistoryService
from metier.history import History
from view.session import Session
from dao.PlayerDao import PlayerDao
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
        if Session().login_check=True:
            player= PlayerDao().find_player_by_playername(Session)
            history= History(player.id_player,score,)


            
