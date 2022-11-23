from unittest import TestCase
from dao.PlayerDao import PlayerDao
from metier.player import Player

class TestPlayerDao(TestCase):
    def test_add_player(self):
        # GIVEN
        player_dao = PlayerDao()
        player=Player("Mohamed","mohamedassili2@gmail.com","test")
        # WHEN
        created = player_dao.add_player(player)
        # THEN
        self.assertTrue(created)
        self.assertIsNotNone(player.id_player)
        print(player.id_player)
    def test_find_player_by_id(self):
        pass
    def test_find_all_players(self):
        pass
    def test_update_player(self):
        pass
