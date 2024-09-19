from src.water_pokemon import WaterPokemon
from src.pokemon import Pokemon

class TestInstantiation:
    def test_new_instance_is_instance_of_class_water_pokemon(self):
        my_pokemon = WaterPokemon("Squirtle", 44, 16, "Surf")
        assert isinstance(my_pokemon, WaterPokemon)

    def test_water_pokemon_is_child_of_pokemon_class(self):
        my_pokemon = WaterPokemon("Squirtle", 44, 16, "Surf")
        assert issubclass(type(my_pokemon), Pokemon)

    def test_water_pokemon_is_instantiated_with_water_type(self):
        my_pokemon = WaterPokemon("Squirtle", 44, 16, "Surf")
        assert my_pokemon.type == "water"

    def test_water_pokemon_is_instantiated_with_strong_against_property(self):
        my_pokemon = WaterPokemon("Squirtle", 44, 16, "Surf")
        assert my_pokemon.strong_against == ["fire"]

    def test_water_pokemon_is_instantiated_with_weak_against_property(self):
        my_pokemon = WaterPokemon("Squirtle", 44, 16, "Surf")
        assert my_pokemon.weak_against == ["grass"]