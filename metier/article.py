import wikipedia
import wikipediaapi



class Article(object):

    rd = wikipedia.page(wikipedia.random(1))
    titre = rd.title
    liens = rd.links
    nb_vues = 0
    Contenu = rd.summary

    def __init__(self, name_article = titre, links = liens) :
        self.links = links
        self.name_article = name_article


Test = Article()
print(Article.titre)