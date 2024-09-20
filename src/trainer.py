from src.pokeball import Pokeball

class BeltFullError(Exception):
    def __init__(self):
        self.message = "All of the Pokeballs on the belt already contain a Pokemon"
        super().__init__(self.message)

class Trainer:
    def __init__(self):
        self._belt = (Pokeball(), Pokeball(), Pokeball(), Pokeball(), Pokeball(), Pokeball())

    @property
    def belt(self):
        return self._belt
    
    def throw_pokeball(self, pokemon):
        if all(not pokeball.is_empty() for pokeball in self._belt):
            raise BeltFullError
        for pokeball in self._belt:
            if pokeball.is_empty():
                pokeball.catch(pokemon)
                break