import wikipedia
import wikipediaapi



class Article(object):

    rd = wikipedia.page(wikipedia.random(1))
    titre = rd.title
    liens = rd.links
    nb_vues = 0
    contenu = rd.summary

    def __init__(self, name_article = titre, links = liens, nb_views = nb_vues, content = contenu) :
        self.links = links
        self.name_article = name_article
        self.links = links
        self.nb_views = nb_views
        self.content = content