from src.pokemon import Pokemon

class WaterPokemon(Pokemon):
    def __init__(self, name, hit_points, attack_damage, move):
        super().__init__(name, hit_points, attack_damage, move)
        self._type = "water"
        self._strong_against = ["fire"]
        self._weak_against = ["grass"]