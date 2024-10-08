# Guess the Wikipedia article

![forthebadge](https://img.shields.io/badge/Build%20by-%20ENSAIEN-blue?style=for-the-badge)
![forthebadge](https://img.shields.io/badge/Groupe%2017-green?style=for-the-badge)


This application is group 17's Python project. This game is called "Guess the Wikipedia article", it is a mix between two famous games : "The Philosopher" and "The Pyramid".
It is a simple game you get a clue each turn to guess which is the title of the Wikipedia article randomly selected. Your score starts at 100 and you will get -10 for each clue used 


## Installation

You need an internet connection and access to the PostgreSQL database before playing.

Python 3.13 is recommended. From the project directory, create and activate a virtual environment:

```powershell
py -3.13 -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

The dependencies are listed in [requirements.txt](requirements.txt).

### Database configuration

Copy the database configuration into a `.env` file at the project root:

```text
HOST=...
PORT=...
DATABASE=...
USER=...
PASSWORD=...
```

The PostgreSQL server must be reachable from your network or VPN. The database tables can be created with [init_dbase.sql](init_dbase.sql).


## Start

Run the game from the activated virtual environment:

```powershell
python main.py
```

Players can play without logging in, or create an account to view their history and statistics.

## Made with

* [Python](https://www.python.org/) - programming language
* [PostgreSQL](https://www.postgresql.org/) - service linking our programme and database

## Author
* Mohamed ASSILI pseudo [@meda6li](https://gitlab.com/meda6li)
* Cédric GRANDVAUX pseudo [@ceddx](https://gitlab.com/ceddx)
* Wajih HAMMOUDA pseudo [@W_101001](https://gitlab.com/W_101001)
* Lorenzo MATHIEU pseudo [@Stenaxo](https://gitlab.com/Stenaxo)
* Tissine PICHON pseudo [@Tissine](https://gitlab.com/Tissine)
