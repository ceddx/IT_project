from metier.article_generation import *
from metier.article import *
import wikipedia
'''
import sys
sys.path.append("C:/Users/lolom/Desktop/projet info/projet_info_2a/metier/article_generation.py")
'''

wikipedia.set_lang('fr')
art = ArticleGeneration()
nom = art.get_title()
article_wikipedia = wikipedia.page(nom)
liens = article_wikipedia.links
nb_vues = art.get_views()
contenu = article_wikipedia.summary

test = Article(nom, liens, nb_vues, contenu)