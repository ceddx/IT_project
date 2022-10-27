from view.abstract_view import AbstractView
from PyInquirer import  prompt
from pprint import pprint
from view.start_view import StartView
<<<<<<< HEAD
import Article,article_generation
=======
from metier.article import Article
from session import Session
from PyInquirer import Inquirer, prompt, Validator, ValidationError

>>>>>>> 55283c1ce7bb4b1e2d639ae142994f836e70cc08
class gameview(AbstractView):
    def __init__(self):
        self.__questions = [
            {
                'type': 'list',
                'name': 'choix',
                'message': f'Bonjour {Session().player_name}',
                'choices': [
                    'jouer'
                    , 'retour',
                    'instructions'
                ]
            }
    ]
    def display_info(self):
        print(f"Hello {Session().player.name}")
    def make_choice(self):
        reponse = prompt(self.__questions)
        if reponse['choix'] == 'jouer':
            play_game()
        elif reponse['choix'] == 'retour':
            return StartView()
        elif reponse['choix'] == 'instructions':
            print("Guess the random wikipedia Article, you can use hints but for each hint used you lower your score :c")
    def play_game(self):
        begin,hint_message=false
        i=0
        guess=""
        begin = inquirer.confirm(message="Begin the game?", default=True).execute()
        if begin :
            game_article=Article()
            list_of_hints=game_article.select_clue()
            while i < len(list_of_hints):
                hint_message = inquirer.confirm(message="Get a hint?",default = True).execute()
                if hint_message :
                     print(list_of_hints[i])
                guess = inquirer.text(message="Make a guess",multiline=True).execute()
                if guess == game_article.name:
                     print("Congratulation you won the game")
                     break
                else:
                    print("Try again")
                    i+=1
                    
            





