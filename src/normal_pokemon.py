from src.pokemon import Pokemon

class NormalPokemon(Pokemon):
    def __init__(self, name, hit_points, attack_damage, move):
        super().__init__(name, hit_points, attack_damage, move)
        self._type = "normal"