from view.abstract_view import AbstractView
from PyInquirer import  prompt
from pprint import pprint
from view.start_view import StartView
from metier.article import Article
from session import Session
from PyInquirer import Inquirer, prompt, ValidationError

class Gameview(AbstractView):
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
        begin,hint_message=False
        i=0
        score=20  ####score 
        guess=""
        begin = Inquirer.confirm(message="Begin the game?", default=True).execute()
        if begin :
            game_article=Article()
            list_of_hints=game_article.select_clue()
            while i < len(list_of_hints):
                hint_message = Inquirer.confirm(message="Get a hint?",default = True).execute()
                if hint_message :
                     score-=1
                     print(list_of_hints[i])
                guess = Inquirer.text(message="Make a guess",multiline=True).execute()
                if guess == game_article.name:
                     print("Congratulation you won the game")
                     break
                else:
                    print("Try again")
                    score-=2
                    i+=1
                    if guess == game_article.name:
                        print("Congratulation you won the game")
                        break
        Session().score=score
        return score
            





