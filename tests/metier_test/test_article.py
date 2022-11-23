import unittest
from test_article_generation import *
from metier.article import Article
import re

class Test_Article(unittest.TestCase):


    def test_frequent_words(self):
        Art = Article(MockGenerator())
        test = "Je suis en train d'écrire un texte lambda en regroupant plusieurs fois le même mot aléatoirement, ainsi selon comme par exmple Friends parce que Friends c'est une série vraiment cool et comme ca on va voir si Friends apparaît bien comme mot le plus fréquent je le redis quelques fois au cas ou Friends Friends Friends Friends Friends"
        Art.content = test
        l = Art.frequents_words()
        liste_frequent =[]
        for valeur in l.keys():
            liste_frequent.append(valeur)
        reversed(liste_frequent)
        self.assertEqual(liste_frequent[0],'Friends')
        self.assertEqual('ainsi' in liste_frequent,False)
    
    def test_get_clue(self):
        Art = Article(MockGenerator())
        clue = Art.get_clue()
        self.assertEqual(len(clue)>9,True)
    
#    def test_blank_paragraph(self):


if __name__ == '__main__':
    unittest.main()


