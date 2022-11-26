import os
import dotenv
import psycopg2
from psycopg2.extras import RealDictCursor
from util.singleton import Singleton


class DBConnection(metaclass=Singleton):
    """
    Classe technique permettant de n'ouvrir qu'une seule connection avec la base de données.
    """

    def __init__(self):
        '''
        Initialisation des paramètres et ouverture de la connexion.
        '''
        dotenv.load_dotenv(override=True)
        # Open the connection.
        self.__connection = psycopg2.connect(
            host=os.environ["HOST"],
            port=os.environ["PORT"],
            database=os.environ["DATABASE"],
            user=os.environ["USER"],
            password=os.environ["PASSWORD"],
            cursor_factory=RealDictCursor)

    @property
    def connection(self):
        """
        Méthode renvoyant la connexion ouverte avec la base de données.

        Return :
        ---------
        connection : connection
            la connexion ouverte
        """
        return self.__connection
