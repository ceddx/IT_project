from view.abstract_view import AbstractView
from PyInquirer import  prompt
from pprint import pprint
from view.start_view import StartView
import Article,article_generation
class gameview(AbstractView):

    def display_info(self):
        print(f"Hello {Session().player.name}")
    def make_choice(self):
        answers = prompt(self.__questions)
        pprint(answers)
        return StartView()
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
                    
            





