import unittest
from view.gameview import Gameview
class Test(unittest.TestCase):
    def test_gameview(self):
        game= Gameview()
        game.play_game()
        


if __name__ == "__main__":
    unittest.main()