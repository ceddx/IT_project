from metier.article_generation import *
from metier.article import *
import wikipedia
'''
import sys
sys.path.append("C:/Users/lolom/Desktop/projet info/projet_info_2a/metier/article_generation.py")
'''

wikipedia.set_lang('fr')

validation = False
while validation == False:
   art = ArticleGeneration()
   nom = art.get_title()
   nb_vues = art.get_views()
   liste = wikipedia.search(nom)
   if liste != []:
        if nom == liste[0]:
            validation = True
        else :
            nom = liste[0]
            validation = True

article_wikipedia = wikipedia.page(nom)
liens = article_wikipedia.links
contenu = article_wikipedia.summary
test = Article(nom, liens, nb_vues, contenu)
test.select_clue()
print(test.clue)




