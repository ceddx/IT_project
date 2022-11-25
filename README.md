# Guess the Wikipedia article

This application is group 17's Python project. This is game is called "Guess the Wikipedia article", it is a mix between two famous game : "The Philosopher" and "The Pyramid".
It is a simple game you get a clue each turn to guess which is the title of the Wikipedia article randomly selected. Your score starts at 100 and you will get -10 for each clue used 
( which means you will lose after 10 clues)


## To start

You have to fill in somes steps before playing this game.
### Prerequisite 

You have to download these packages in this version
- InquirerPy==0.3.4
- prompt_toolkit==1.0.14
- psycopg2==2.9.5
- psycopg2_binary==2.9.4
- PyInquirer==1.0.3
- python-dotenv==0.21.0
- regex==2022.9.13
- requests==2.28.1
- Unidecode==1.3.6
- Werkzeug==2.2.2
- Wikipedia_API==0.5.4


### Installation

To install the application you have to copy text in init_dbase.sql and to past it in your posrgresql to create a public database.
Then you have to put your id in the file .env in password, database, user.
Your are ready to play!!

## Start

You have to execute command ``python -m main`` main.py and everything will be done in the terminal

## Made with

* [Python](https://www.python.org/) - programming language
* [PostgreSQL](https://www.postgresql.org/) - service linking our programme and database

## Author
* *Mohamed ASSILI* pseudo [@meda6li](https://gitlab.com/meda6li)
* *Cédric GRANDVAUX* pseudo [@ceddx](https://gitlab.com/ceddx)
* *Wajih HAMMOUDA* pseudo [@W_101001](https://gitlab.com/W_101001)
* *Lorenzo MATHIEU* pseudo [@Stenaxo](https://gitlab.com/Stenaxo)
* *Tissine PICHON* pseudo [@Tissine](https://gitlab.com/Tissine)