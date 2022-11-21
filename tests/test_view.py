import unittest
from view.gameview import Gameview

        
class Test(unittest.TestCase):
    def test_article_generation(self):
        game1= Gameview()
        game1.play_game()


if __name__ == "__main__":
    unittest.main()

