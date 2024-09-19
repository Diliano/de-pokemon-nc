from src.pokemon import Pokemon

class FirePokemon(Pokemon):
    def __init__(self, name, hit_points, attack_damage, move):
        super().__init__(name, hit_points, attack_damage, move)
        self._type = "fire"
        self._strong_against = ["grass"]
        self._weak_against = ["water"]