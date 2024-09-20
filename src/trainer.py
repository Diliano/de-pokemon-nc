from src.pokeball import Pokeball

class Trainer:
    def __init__(self):
        self._belt = (Pokeball(), Pokeball(), Pokeball(), Pokeball(), Pokeball(), Pokeball())

    @property
    def belt(self):
        return self._belt