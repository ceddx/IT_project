from dao.PlayerDao import PlayerDao
from metier.player import Player
from view.signupview import SignIn

class PlayerService:
    '''
    Classe gérant les informations relatives aux joueurs.
    '''

    @staticmethod
    def create_player(name,email,password):
        player = Player(name,email,password)
        return PlayerDao().add_player(player)
