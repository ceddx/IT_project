import requests
import random
import wikipediaapi
import re
from util.singleton import Singleton
import unidecode




class ArticleGeneration(metaclass=Singleton): 
    """
    Classe qui permet de générer un article, de récupérer ses propriétés et de le valider
    """
    mois = str(random.randint(1,9))
    annee = str(random.randint(2016,2022))
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
    res = requests.get(
        'https://wikimedia.org/api/rest_v1/metrics/pageviews/top/fr.wikipedia/all-access/'+annee+'/0'+mois+'/all-days',
        headers=headers)
    resj = (res.json())['items'][0]['articles']
    rdm = random.randint(0,len(resj)-1)


    def __init__(self, num_article=rdm, liste_article=resj):
        '''
        Génère un article.

        Paramètres :
        -------------
        num_article : int
            Le numéro de l'article dans la liste
        liste_article : liste
            La liste des articles disponibles
        '''

        self.num_article = num_article
        self.liste_article = liste_article

    def get_title(self):
        '''
        Méthode permettant de récupérer le titre de la page.

        Returns :
        --------------------------------
        titre : str
        Le titre de la page
        '''

        titre = self.liste_article[self.num_article]['article']
        if '_' in titre:
            titre = titre.replace('_', ' ')
        return str(titre)

    def get_views(self):
        '''
        Méthode permettant de récupérer le nombre de vues de la page
        Returns :
        --------------------------------
        nb_vues : int
        Le nombre de vue de la page
        '''
        
        nb_vues = self.liste_article[self.num_article]['views']
        return nb_vues

    def validation(self):
        '''
        Méthode permettant de vérifier si l'article et jouable ou non.

        Returns :
        --------------------------------
        True si les conditions sont remplies
        False sinon
        '''

        wiki_wiki = wikipediaapi.Wikipedia('fr')
        page = wiki_wiki.page(self.get_title())
        return page.exists()

    def get_categories(self):
        '''
        Méthode permettant de récupérer les catégories et portails de la page
        Returns :
        --------------------------------
        liste : list
        Les catégories de la page
        '''

        wiki_wiki = wikipediaapi.Wikipedia('fr')
        page = wiki_wiki.page(self.get_title())
        categories = page.categories
        liste = []
        for title in sorted(categories.keys()):
            if re.search('Catégorie:Page utilisant', title) is None:
                cat = title[10:]
                liste.append(cat)

        return liste

    def get_content(self):
        '''
        Méthode permettant de récupérer le contenu de la page
        Returns :
        --------------------------------
        page_content : str
        Le contenu de la page
        '''
        wiki_wiki = wikipediaapi.Wikipedia(
            language='fr',
            extract_format=wikipediaapi.ExtractFormat.WIKI)
        p_wiki = wiki_wiki.page(self.get_title())
        page_content = p_wiki.text

        return page_content

    def new_rdm(self):
        '''
        Méthode renvoyant un nouveau nombre aléatoire.
        '''

        nrdm = rdm = random.randint(0,999)
        while nrdm == self.num_article:
            nrdm = random.randint(0, 999)
        self.num_article = nrdm

    def normalize_string(self, string):
        '''
        Enlève les accents et ç en les remplaçant par les caractères associés.
    
        Parameter
        ----------
        string : str
            La chaîne à normaliser
        
        Return
        -------
        string : str
            La chaîne de caractère normalisée.
        
        '''
        
        string = unidecode.unidecode(string)
        string = string.lower()
        
        return string
    
    def find_sql(string):
        '''
        Repère les commandes SQL
    
        Parameter
        ----------
        string : str
            La chaîne à vérifier
        
        Return
        -------
        string : str
            La chaîne de caractère normalisée.
        
        '''
        sql = []
        for word in string.split():
            if word.lower() == 'select' or word.lower() == 'from' or word.lower() == 'where' or word.lower() == 'drop':
                sql.append(word)
        return sql

    