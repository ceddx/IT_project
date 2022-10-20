from dataclasses import replace
import requests
import random


class ArticleGeneration(object):

    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
    res = requests.get('https://wikimedia.org/api/rest_v1/metrics/pageviews/top/fr.wikipedia/all-access/2022/09/all-days',headers=headers)
    resj = (res.json())['items'][0]['articles']
    rdm = random.randint(0,len(resj)-1)

    def __init__(self, num_article = rdm, liste_article = resj):

        self.num_article = num_article
        self.liste_article = liste_article
    
    def get_title(self):

        titre = self.liste_article[self.num_article]['article']
        titre = titre.replace('_',' ')
        return titre

    def get_views(self):

        return self.liste_article[self.num_article]['views']

