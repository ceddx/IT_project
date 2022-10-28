from abc import ABC, abstractmethod

from view.session import Session


class AbstractView(ABC):
    """
    Classe abstraite qui permet de gérer toutes les vues.
    """

    @abstractmethod
    def display_info(self):
        """
        Méthode qui va juste déterminer l'affichage en console.
        """
        pass

    @abstractmethod
    def make_choice(self):
        """
        Méthode qui va gérer les choix de l'utilisateur et l'envoyer vers une autre page.
        """
        pass
