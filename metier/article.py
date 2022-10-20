import re

class Article(object):

    '''
    Classe permettant de générer les articles, les indices et leur validation.
    '''

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

        
    
    def select_clue(self):

        """
        Méthode permettant de selectionner les indices
        """
        summary = self.content
        sp = summary.split()
        i = 0
        indices = []
        count = 0

        while i < len(self.content) or len(indices)<=10:
            if ((sp[i] in self.links) == True) and ((sp[i] in indices) == False) and (sp[i] != self.name_article):
                if len(sp[i])<=4:
                    tester = self.is_date_or_number(sp[i])
                    if (tester == True) and len(sp[i])>2 and count <3: 
                        indices.append(sp[i])
                        count += 1
                        i += 1
                else :
                    indices.append(sp[i])
                    i += 1

        self.clue = indices
        return self.clue
    
    def is_date_or_number(self, smth):
        
        test = re.match("[0-9]",smth)
        if test != None:
            return True
        else :
            return False
