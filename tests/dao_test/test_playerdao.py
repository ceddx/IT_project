from unittest import TestCase
from dao.PlayerDao import PlayerDao
from metier.player import Player

class TestPlayerDao(TestCase):
    def test_add_player(self):
        # GIVEN
        player_dao = PlayerDao()
        player=Player(1,"bertarnd","bertrand@gmail.com","ok")
        # WHEN
        created = player_dao.add_player(player)

        # THEN
        self.assertTrue(created)
