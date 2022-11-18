import unittest

class Test(unittest.TestCase):
    def test_article_generation(self):
        article = ArticleGeneration(0, [{"article":"Cookie_(informatique)","views":177667567,"rank":1}])
        titre = article.get_title()
        print(titre)


if __name__ == "__main__":
    unittest.main()