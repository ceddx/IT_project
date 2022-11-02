from metier.article import Article
from metier.article_generation import ArticleGeneration
import unittest
"""
import sys
sys.path.append("C:/Users/lolom/OneDrive/Bureau/PI/projet_info_2a/metier/article_generation.py")
"""
"""

class Test(unittest.TestCase):
    def test_article_generation(self):
        print ( "Choose one of the following option:")
        print ( "1: Play")
        print ( "2: Quit")
        option_number = int(input())
        article = Article()
        name_article = article.name_article
        clue= article.name_article
        if option_number == 1:
            print ( "Type the article name guess:")
            print (f"Clue: {clue}")
            name_guess = input() 
            if name_guess == name_article: 
                print ("WELL DONE BRO/SIS") 
            else: 
                print ("WASTED")
        elif option_number ==2:
            print ( "Bye See you later <3")


if __name__ == "__main__":
    unittest.main()

"""

test = Article()
print(test.get_clue())    


