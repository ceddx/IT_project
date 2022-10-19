import wikipedia
from article_generation import ArticleGeneration

class Article(object):
    '''
    Classe permettant de générer les articles, les indices et leur validation.
    '''
    wikipedia.set_lang('fr')
    art = ArticleGeneration()
    nom = art.get_title()
    article_wikipedia = wikipedia.page(nom)
    liens = article_wikipedia.links
    nb_vues = art.get_views()
    contenu = article_wikipedia.summary


    def __init__(self, name_article : str , links : list, nb_views : int, content : str, clue = []) :
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
#Mettre une variable pour la difficulté à la place de <10
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
    
