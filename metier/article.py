from dataclasses import replace
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
        article = ArticleGeneration()
        while t == False:
            t = article.validation()
            article.new_rdm()

        self.name_article = article.get_title()
        self.links = article.get_links()
        self.nb_views = article.get_views()
        self.summary = article.get_summary()
        self.content = article.get_content()
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
        test = re.search("\d+|janvier|février|mars|avril|mai|juin|juillet|août|septembre|octobre|novembre|décembre'", smth, re.IGNORECASE)
        if test != None:
            return True
        else :
            return False

    def frequents_words(self):

        liste = self.content.split()
        dico = {}
        for i in range (len(liste)):     
            dico[liste[i]]=liste.count(liste[i])
        dico = dict(sorted(dico.items(), key=lambda item: item[1],reverse=True))
        keys=list(dico.keys())
        for j in range (len(keys)):
            l=["le","la","les","de","des","et","lui","leur","leurs","il","elle","est","sont","son","sa","ses","ce","ces","de","en",":",'du','ou','par','pour','que','à','a','dans','ont','plus','qui','sur','une','au','même','se','ne','pas',]
            if(keys[j] in l):
                del dico[keys[j]]
        return dico
        
    def get_paragraph(self):
        summary= self.summary
        pertinent=' '
        for i in summary:
            pertinent=pertinent+summary

            if i == '/n':
                break
        return pertinent
    @staticmethod
    def blanked_paragraph(paragraph,title):
        if title in paragraph:
            paragraph = paragraph.replace(title,'X'*len(title))
    
    def get_clue(self):
        list_clues=[]
        l=self.categories
        list_categories = list(filter(lambda x: ('Article' not in x) and ('Catégorie' not in x) and ('Page' not in x) , l))
        list_portail = list(filter(lambda x: 'Portail' in x, l))
        for i in range(len(list_portail)):
            a=len("Portail:")
            b=len("/Articles liés")  
            element=list_portail[i] 
            list_portail[i]=element[a:-b] #reste un petit prob avec qql portails
            dict_freq_words = self.frequents_words()
            list_all_frequent_words=list(dict_freq_words.keys())
            list_frequent_words = list_all_frequent_words[:10]
            list_clues = list_categories + list_frequent_words +list_portail
            list_clues = list(filter(lambda x : self.name_article not in x,list_clues))
        return list_clues