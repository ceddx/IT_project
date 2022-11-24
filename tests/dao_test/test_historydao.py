from dao.historydao import HistoryDao
from metier.history import History
from metier.player import Player
from unittest import TestCase
import unittest

class TestHistoryDao(TestCase):
    def test_add_history(self):
        history_dao=HistoryDao()
        history=History(1,60,3,'nom article')
        print(history.article)

        created=history_dao.add_history(history)
        self.assertTrue(created)
        self.assertIsNotNone(history.id_history)
    
    def test_find_player_history(self):

        history_dao=HistoryDao()
        player=Player(1,"Simo","Assili@ensai.fr","5679KK")

        list=history_dao.find_player_history(player)
        print(list)
        print(len(list))

    if __name__ == '__main__':
        unittest.main()