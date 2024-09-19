from src.pokemon import Pokemon

class FirePokemon(Pokemon):
    def __init__(self, name, hit_points, attack_damage, move):
        super().__init__(name, hit_points, attack_damage, move)
        self.__type = "fire"
        self.__strong_against = ["grass"]

    @property
    def type(self):
        return self.__type
    
    @property
    def strong_against(self):
        return self.__strong_against