class PokeballFullError(Exception):
    def __init__(self):
        self.message = "The Pokeball already contains a Pokemon"
        super().__init__(self.message)

class Pokeball:
    def __init__(self):
        self._pokemon = None

    @property
    def pokemon(self):
        return self._pokemon
    
    def catch(self, pokemon):
        if self._pokemon is None:
            self._pokemon = pokemon
        else:
            raise PokeballFullError
        
    def is_empty(self):
        return self._pokemon is None