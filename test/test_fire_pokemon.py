from src.fire_pokemon import FirePokemon
from src.pokemon import Pokemon
import pytest

@pytest.fixture
def fire_pokemon():
    return FirePokemon("Charmander", 44, 17, "Flamethrower")

class TestInstantiation:
    def test_new_instance_is_instance_of_class_fire_pokemon(self, fire_pokemon):
        assert isinstance(fire_pokemon, FirePokemon)

    def test_fire_pokemon_is_child_of_pokemon_class(self, fire_pokemon):
        assert issubclass(type(fire_pokemon), Pokemon)

    def test_fire_pokemon_is_instantiated_with_fire_type(self, fire_pokemon):
        assert fire_pokemon.type == "fire"

    def test_fire_pokemon_is_instantiated_with_strong_against_property(self, fire_pokemon):
        assert fire_pokemon.strong_against == ["grass"]

    def test_fire_pokemon_is_instantiated_with_weak_against_property(self, fire_pokemon):
        assert fire_pokemon.weak_against == ["water"]