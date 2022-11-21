import unittest
import wikipediaapi
import re
import random

class MockGenerator(object):
    iter = 0
    random.seed(69)
    dico = [
        {'article': 'Cookie_(informatique)', 'views': 177667567, 'rank': 1}, 
        {'article': 'Wikipédia:Accueil_principal', 'views': 18276169, 'rank': 2}, 
        {'article': 'Spécial:Recherche', 'views': 3956071, 'rank': 3}, 
        {'article': 'Élisabeth_II', 'views': 3314995, 'rank': 4}, 
        {'article': 'Jeffrey_Dahmer', 'views': 1837040, 'rank': 5}, 
        {'article': 'Google_Traduction', 'views': 1362929, 'rank': 6}, 
        {'article': 'Charles_III_(roi_du_Royaume-Uni)', 'views': 1173483, 'rank': 7}, 
        {'article': 'George_VI', 'views': 869683, 'rank': 8}, 
        {'article': 'Philip_Mountbatten', 'views': 741374, 'rank': 9}, 
        {'article': 'Margaret_du_Royaume-Uni', 'views': 702948, 'rank': 10}
            ]
    
    def __init__(self, liste_article = dico, num_article = 0):

        self.num_article = num_article
        self.liste_article = liste_article

    def next(self):
        self.num_article +=1

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


        '''
        Méthode permettant de récupérer une liste avec tous les liens hypertextes de la page.

        Returns :
        --------------------------------
        liste : list
        La liste de liens hypertextes de la page
        '''
        wiki_wiki = wikipediaapi.Wikipedia('fr')
        page = wiki_wiki.page(self.get_title())
        links = page.links
        liste = []
        for title in sorted(links.keys()):
            liste.append(title)
        return liste


        '''
        Méthode permettant de récupérer le sommaire de la page
        Returns :
        --------------------------------
        page.summary : str
        Le sommaire de la page
        '''

        wiki_wiki = wikipediaapi.Wikipedia('fr')
        page = wiki_wiki.page(self.get_title())
        return page.summary

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

class Test_Ag(unittest.TestCase):   
    
    def test_get_title(self):

        '''
        Fonction permettant de tester la méthode "get_title" qui donne le titre d'un article.
        '''
  
        
        article = MockGenerator()

        titre = article.get_title()        
        self.assertEqual("Cookie (informatique)", titre)
        article.next()

        titre = article.get_title()        
        self.assertEqual("Wikipédia:Accueil principal", titre)
        article.next()

        titre = article.get_title()        
        self.assertEqual('Spécial:Recherche', titre)
        article.next()

        titre = article.get_title()        
        self.assertEqual('Élisabeth II', titre)
        article.next()

        titre = article.get_title()        
        self.assertEqual('Jeffrey Dahmer', titre)
        article.next()

        titre = article.get_title()        
        self.assertEqual('Google Traduction', titre)
        article.next()

        titre = article.get_title()        
        self.assertEqual('Charles III (roi du Royaume-Uni)', titre)
        article.next()

        titre = article.get_title()        
        self.assertEqual('George VI', titre)
        article.next()

        titre = article.get_title()        
        self.assertEqual('Philip Mountbatten', titre)
        article.next()

        titre = article.get_title()        
        self.assertEqual('Margaret du Royaume-Uni', titre)
        article.next()

    def test_get_view(self):
        '''
    Fonction permettant de tester la méthode "get_views" qui donne le nombre de vues d'un article.
        '''
    
        article = MockGenerator()

        nb = article.get_views()        
        self.assertEqual(177667567 , nb)

    def test_validation(self):
        '''
        Méthode permettant de vérifier si l'article et jouable ou non.
            '''
        article = MockGenerator()

        val = article.validation()
        self.assertEqual(True, val)
    
    

if __name__ == '__main__':
    unittest.main()

