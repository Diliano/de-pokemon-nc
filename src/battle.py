class Battle:
    def __init__(self, pokemon_1, pokemon_2):
        self._pokemon_1 = pokemon_1
        self._pokemon_2 = pokemon_2

    @property
    def pokemon_1(self):
        return self._pokemon_1
    
    @property
    def pokemon_2(self):
        return self._pokemon_2