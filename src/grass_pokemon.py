from src.pokemon import Pokemon

class GrassPokemon(Pokemon):
    def __init__(self, name, hit_points, attack_damage, move):
        super().__init__(name, hit_points, attack_damage, move)
        self._type = "grass"
        self._strong_against = ["water"]
        self._weak_against = ["fire"]