import re
from metier.article_generation import ArticleGeneration

class Article(object):

    '''
    Classe permettant de générer les articles, les indices et leur validation.
    '''
    
    def __init__(self, clue = []) :

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
        
        t = False
        while t == False:
            article = ArticleGeneration()
            t = article.validation()

        self.name_article = article.get_title()
        self.links = article.get_links()
        self.nb_views = article.get_views()
        self.content = article.get_summary()
        self.categories = article.get_categories()
        self.clue = clue
        
    
    def select_clue(self): 
    # Ne fonctionne pas encore mais ca ne saurait tarder, le problème vient de la manière 
    # dont sont nommés les liens hypertextes, ils prennent le nom de l'article vers lequel ils dirigent.

        """
        Méthode permettant de sélectionner les indices.
        """
        summary = self.content
        sp = summary.split()
        i = 0
        indices = []
        count = 0

        while i < len(sp):
            if ((sp[i] not in indices) == True) and (sp[i] != self.name_article):
                if len(sp[i])<=4:
                    tester = self.is_date_or_number(sp[i])
                    if (tester == True) and len(sp[i])>2 and count <3: 
                        #Faire en sorte d'avoir au maximum 3 dates pour ne pas avoir que ca en indice
                        indices.append(sp[i])
                        count += 1
                       
                else :
                    indices.append(sp[i])
                    
            i += 1

        self.clue = [*set(indices)]
        return self.clue


    def is_date_or_number(self, smth):
        
        """
        Paramètres:
        --------------------------------
        smth: string
            L'objet à tester

        Returns:
        --------------------------------   
        bool : True or False
        """
        # Utilisation d'expression régulière pour faciliter la recherche
        test = re.match("[0-9]",smth)
        if test != None:
            return True
        else :
            return False
