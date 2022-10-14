class Player:

    def __init__(self, id_player, name, email, password):
        self.id_player = id_player
        self.name = name
        self.email = email
        self._password = password

    