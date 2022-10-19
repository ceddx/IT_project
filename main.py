from article_generation import ArticleGeneration 
from article import Article
import wikipedia

wikipedia.set_lang('fr')
art = ArticleGeneration()
nom = art.get_title()
article_wikipedia = wikipedia.page(nom)
liens = article_wikipedia.links
nb_vues = art.get_views()
contenu = article_wikipedia.summary

article = Article(nom, liens, nb_vues, contenu)
print(article.name_article)

