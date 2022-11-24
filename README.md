# Find the Wikipedia page

![forthebadge](https://img.shields.io/badge/Build%20by-%20ENSAIEN-blue?style=for-the-badge)
![forthebadge](https://img.shields.io/badge/Groupe%2017-green?style=for-the-badge)


This application is Informatic project of groupe 17. This is a game called "Find the Wikipedia page", it is a mix between two famous game : "Le phylosophe" and "La Pyramide".
It is a simple game you choose the language and the difficulty you want played. Then you get a several clue to guess which is the title of the Wikipedia sheet randomly selected. You can ask other clue if you cannot find the title.
You will obtain a score according to your number of try and number of clue you receive.


## To start

You have to find somes steps before to play to this beautiful game.
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

You have to executated command ``python -m main`` main.py and everything will be done in the terminal

## Made with

* [Python](https://www.python.org/) - programming language
* [PostgreSQL](https://www.postgresql.org/) - service linking our programme and database

## Author
* **Mohamed ASSILI** _pseudo_ [@meda6li](https://gitlab.com/meda6li)
* **Cédric GRANDVAUX** _pseudo_ [@ceddx](https://gitlab.com/ceddx)
* **Wajih HAMMOUDA** _pseudo_ [@W_101001](https://gitlab.com/W_101001)
* **Lorenzo MATHIEU** _pseudo_ [@Stenaxo](https://gitlab.com/Stenaxo)
* **Tissine PICHON** _pseudo_ [@Tissine](https://gitlab.com/Tissine)
