class AlreadyFaintedError(Exception):
    def __init__(self):
        self.message = "A Pokemon has already fainted - time to rest!"
        super().__init__(self.message)

class Battle:
    def __init__(self, pokemon_1, pokemon_2):
        self._pokemon_1 = pokemon_1
        self._pokemon_2 = pokemon_2
        self._pokemon_1_turn = True

    @property
    def pokemon_1(self):
        return self._pokemon_1
    
    @property
    def pokemon_2(self):
        return self._pokemon_2
    
    @property
    def pokemon_1_turn(self):
        return self._pokemon_1_turn
    
    def take_turn(self):
        if self._pokemon_1.has_fainted() or self._pokemon_2.has_fainted():
            raise AlreadyFaintedError
        if self._pokemon_1_turn:
            damage = int(self._pokemon_1.attack_damage * self._pokemon_1.get_multiplier(self._pokemon_2))
            self._pokemon_2.take_damage(damage)
        else:
            damage = int(self._pokemon_2.attack_damage * self._pokemon_2.get_multiplier(self._pokemon_1))
            self._pokemon_1.take_damage(damage)
        self._pokemon_1_turn = not self._pokemon_1_turn

    def get_winner(self):
        if self._pokemon_1.has_fainted():
            return self._pokemon_2
        elif self._pokemon_2.has_fainted():
            return self._pokemon_1
        else:
            return None