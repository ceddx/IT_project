from view.abstract_view import AbstractView
from view.startview import StartView
from metier.article import Article
from view.session import Session
from PyInquirer import *
from service.game_service import *

class Gameview(AbstractView):
    '''
    Classe permettant d'afficher les parties du jeu.
    '''
    def __init__(self):
        self.__questions = [
            {
                'type': 'list',
                'name': 'choix',
                'message': f'Hello {Session().player_name}',
                'choices': [
                    'jouer'
                    , 'retour',
                    'instructions'
                ]
            }

    ]
    def display_info(self):
        """
        Méthode qui va juste déterminer l'affichage en console.
        """
        print(f"Hello {Session().player.name}")

    def make_choice(self):
        """
        Méthode qui va gérer les choix de l'utilisateur et l'envoyer vers une autre page.
        """
        reponse = prompt(self.__questions)
        if reponse['choix'] == 'jouer':
            Gameview().play_game()
        elif reponse['choix'] == 'retour':
            return StartView()
        elif reponse['choix'] == 'instructions':
            print("Guess the random wikipedia Article, you can use hints but for each hint used you lower your score :c")

    def play_game(self):
        '''
        Méthode permettant de dérouler une partie.
        '''
        game = GameService()
        secret_article = game.article
        guess_count = 0
        hint_question = [{'type': 'list','name': 'help','message': 'Get a hint?', 'choices' : ['yes','no']}]
        first_clue= game.first_clue
        guess = input("Use this hint to guess the article: {} .".format(first_clue))
        score = Session().score
        while guess!= secret_article:
            reponse = prompt(hint_question)
            if reponse['help']== 'yes':
                first_clue = game.next_task(first_clue)[1]
                guess = input("Use this new hint to guess the article: {}".format(first_clue))
                print(first_clue)
            guess_count+=1
        
        print('You win')
        
        

    


            





