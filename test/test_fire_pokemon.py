from src.fire_pokemon import FirePokemon
from src.pokemon import Pokemon

class TestInstantiation:
    def test_new_instance_is_instance_of_class_fire_pokemon(self):
        my_pokemon = FirePokemon("Charmander", 44, 17, "Flamethrower")
        assert isinstance(my_pokemon, FirePokemon)

    def test_fire_pokemon_is_child_of_pokemon_class(self):
        my_pokemon = FirePokemon("Charmander", 44, 17, "Flamethrower")
        assert issubclass(type(my_pokemon), Pokemon)

    def test_fire_pokemon_is_instantiated_with_fire_type(self):
        my_pokemon = FirePokemon("Charmander", 44, 17, "Flamethrower")
        assert my_pokemon.type == "fire"