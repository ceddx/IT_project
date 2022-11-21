from metier.article import Article
from metier.article_generation import ArticleGeneration
import unittest
from view.abstract_view import AbstractView
from view.gameview import Gameview
from view.historyview import History
from view.loginview import LoginView
from view.session import Session
from view.signupview import SignUp
from view.startview import StartView
from view.updateview import UpdateView
import requests

dict_view = {
        "Start " : StartView,
        "Login " : LoginView,
        "Sign Up": SignupView,
        "history": HistoryView,
        "update":UpdateView,
        "Play Game":Gameview,
        "Rank":RankView
    }

if __name__ == "__main__" :
    view = StartView()
    while view != None:
        view.display_info()
        next = view.make_choice()
        if next == "Quit":
            view = None
        else:
            view = dict_view[next]()