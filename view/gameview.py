from view.abstract_view import AbstractView
#from view.startview import StartView
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
        hint_question = [{'type': 'list','name': 'help','message': 'Get a hint?', 'choices' : ['yes','no', 'give up']}]
        first_clue= game.first_clue
        guess = input("Use this hint to guess the article: {} \n".format(first_clue))
        score = 100
        while guess!= secret_article.name_article and guess_count<10:
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
                print('Game over, the right answer is {}'.format(secret_article.name_article))
                Session.score=0
                return "Your score is 0"  
            guess_count+=1
        if score!=0 :
            print("You Win With A Score Of ",score)
        else :
            print("Game over")
        Session.score=score
        
        

    


            





