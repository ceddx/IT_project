from dataclasses import replace
import re
import random
from metier.article_generation import ArticleGeneration


class Article(object):

    '''
    Classe permettant de générer les articles, les indices et leur validation.
    '''

    def __init__(self, clue=[]):
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
        # Utilisation d'expressions régulières pour faciliter la recherche
        test = re.search(
            "\\d+|janvier|février|mars|avril|mai|juin|juillet|août|septembre|octobre|novembre|décembre'",
            smth,
            re.IGNORECASE)
        if test is not None:
            return True
        else:
            return False

    def frequents_words(self):
        '''
        Méthode permettant de trouver les mots pertinents les plus fréquents d'un article. On ne retient pas
        les mots de 4 caractères et moins, ainsi que d'autres mots de liaison.

        Returns :
        -------------
        dico : dict
            dictionnaire contenant les mots les plus fréquents et leur nombre d'apparition
        '''
        liste = self.content.split()
        dico = {}
        for i in range(len(liste)):
            dico[liste[i]] = liste.count(liste[i])
        dico = dict(
            sorted(
                dico.items(),
                key=lambda item: item[1],
                reverse=True))
        keys = list(dico.keys())
        for j in range(len(keys)):

            if (len(keys[j]) < 5):
                del dico[keys[j]]
            l = [
                'comme',
                'après',
                "qu'il",
                "qu'elle",
                'avoir',
                'Après',
                'depuis',
                'Depuis',
                'plusieurs']
            if (keys[j] in l):
                del dico[keys[j]]
        return dico

    def get_paragraph(self):
        '''
        Méthode permettant de retourner le premier paragraphe du résumé d'un article.

        Returns :
        -----------
        pertinent : str
            premier paragraphe de l'article
        '''
        summary = self.summary
        pertinent = ' '
        for i in summary:
            pertinent = pertinent + summary

            if i == '/n':
                break
        return pertinent

    @staticmethod
    def blanked_paragraph(paragraph, title):
        '''
        Méthode qui cache le titre de l'article dans le premier paragraphe.

        Paramètres :
        ------------
        pargraph : str
            le paragraphe où il faut masquer le titre
        title : str
            titre de l'article qui ne doit pas apparaître dans le paragraphe
        '''
        if title in paragraph:
            paragraph = paragraph.replace(title, 'X' * len(title))

    def get_clue(self):
        '''
        Méthode permettant d'obtenir la listes des indices qui pourront être donnés à un joueur pour qu'il
        devine le titre d'un article.

        Returns :
        ------------
        list_clues : list
            liste des indices à donner
        '''
        list_clues = []
        l = self.categories
        list_categories = list(filter(filtrer, l))
        list_portail = list(filter(lambda x: 'Portail' in x, l))
        for i in range(len(list_portail)):
            a = len("Portail:")
            b = len("/Articles liés")
            element = list_portail[i]
            list_portail[i] = element[a:-b]
        dict_freq_words = self.frequents_words()
        list_all_frequent_words = list(dict_freq_words.keys())
        list_frequent_words = list_all_frequent_words[:10]
        list_clues = list_categories + list_frequent_words + list_portail
        article_name = self.name_article
        article_name_list = article_name.split()
        if len(article_name_list) >= 2:
            list_clues = list(
                filter(
                    lambda x: (
                        article_name_list[0] not in x) and (
                        article_name_list[1] not in x),
                    list_clues))
        list_clues = list(filter(filtrer, list_clues))
        random.shuffle(list_clues)
        return list_clues


def filtrer(s):
    del_words = [
        'article'.casefold(),
        'biographie/articles liés/c'.casefold(),
        'catégorie'.casefold(),
        'wikipédia:'.casefold(),
        'page'.casefold()]
    s = s.casefold()
    return all(del_w not in s for del_w in del_words)
