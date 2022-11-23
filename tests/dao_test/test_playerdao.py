from dao.PlayerDao import PlayerDao
from metier.player import Player
import unittest
from unittest import TestCase

class TestPlayerDao(TestCase):
    def test_add_player(self):
        # GIVEN
        player_dao = PlayerDao()
        player=Player("Mohamed","mohamedassili2@gmail.com","12345")
        # WHEN
        created = player_dao.add_player(player)
        # THEN
        self.assertTrue(created)
        self.assertIsNotNone(player.id_player)
        print(player.id_player)
    def test_find_player_by_id(self):
        player_dao=PlayerDao()
        player=player_dao.find_player_by_id(1)
        self.assertEqual(1,player.id_player)
    def test_find_all_players(self):
        player_dao=PlayerDao()
        list_of_players=player_dao.find_all_players
        print(len(list_of_players))
    def test_update_player(self):
        pass
    if __name__ == '__main__':
        unittest.main()
