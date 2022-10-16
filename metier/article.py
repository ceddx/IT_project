from pyexpat import features
from urllib.robotparser import RequestRate
import wikipedia
import requests



class Article(object):
    '''
    Classe permettant de générer les articles, les indices et leur validation.
    '''
    wikipedia.set_lang('fr')
    rd = wikipedia.page(wikipedia.random(1))
    titre = rd.title
    liens = rd.links
    nb_vues = 0
    contenu = rd.summary

    def __init__(self, name_article = titre, links = liens, nb_views = nb_vues, content = contenu, clue = []) :
        """
        Création de l'article.

        Paramètres:
        --------------------------------
        name_article : string
            Titre de l'article wikipedia
        links : list
            Ensemble des liens hypertextes de la page
        nb_views : int
            Nombre de vues de la page
        Content : string
            Le sommaire de la page wikipedia
        Clue : liste
            Les indices pour trouver la page contenus dans une liste
        """

        self.name_article = name_article
        self.links = links
        self.nb_views = nb_views
        self.content = content
        self.clue = clue
    
    def article_validation(self):

        '''
        Méthode permettant de vérifier si l'article et jouable ou non'.

        Returns :
        --------------------------------
        True si les conditions sont remplies
        False sinon
        '''
#Mettre une variable pour la diffiulté à la place de <10
        if len(self.links) < 10:
            return False
        else : 
            self.select_clue()
            if len(self.clue)<5:
                return False
            else : 
                return True
    
    def select_clue(self):

        """
        Méthode permettant de selectionner les indices
        """
        summary = self.content
        sp = summary.split()
        i = 0
        clue = []
        while i < len(sp):
            if ((sp[i] in self.links) == True) and ((sp[i] not in self.clue) == True):
                clue.append(sp[i])
            i += 1
        self.clue = clue

"""t = False
while t == False:
    a = Article()
    t = a.article_validation()

print(a.clue)"""

res = requests.get('https://wikimedia.org/api/rest_v1/metrics/pageviews/top/fr.wikipedia/all-access/2022/10/15')


