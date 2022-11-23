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
        self.questions = [
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
        print(f"Hello {Session().player_name}")

    def make_choice(self):
        """
        Méthode qui va gérer les choix de l'utilisateur et l'envoyer vers une autre page.
        """
        reponse = prompt(self.questions)
        if reponse['choix'] == 'jouer':
            Gameview().play_game()
            return "SaveHistory"
        elif reponse['choix'] == 'retour':
            return "Menu"
        elif reponse['choix'] == 'instructions':
            print("Guess the random wikipedia Article, you can use hints but for each hint used you lower your score :c")
            return "PlayGame"

    def play_game(self):
        '''
        Méthode permettant de dérouler une partie.
        '''
        game = GameService()
        secret_article = game.article
        Session().article=secret_article
        attempts = 0
        hint_question = [{'type': 'list','name': 'help','message': 'Get a hint?', 'choices' : ['yes','no', 'give up']}]
        first_clue= game.first_clue
        guess = input("Use this hint to guess the article: {} \n".format(first_clue))
        score = 100
        while guess!= secret_article.name_article and attempts<10:
            reponse = prompt(hint_question)
            if reponse['help']== 'yes':
                first_clue = game.next_task(first_clue)[1]
                score-=10
                print("your current score is ", score)
                guess = input("Use this new hint to guess the article: {} \n".format(first_clue))
                if guess == secret_article.name_article:
                    break

            if reponse['help'] == 'no':
                guess = input("Another chance!")
                if guess == secret_article.name_article:
                    break
            if reponse['help'] == 'give up':
                score=0
                print("Your score is 0")
                break
            attempts+=1
        if score!=0 :
            print("You Win With A Score Of ",score)
        else :
            print('Game over, the right answer is {}'.format(secret_article.name_article))
        Session().score=score
        Session().number_of_attempts = attempts
        

        
        

    


            





