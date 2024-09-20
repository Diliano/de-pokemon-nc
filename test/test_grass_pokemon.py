from src.grass_pokemon import GrassPokemon
from src.pokemon import Pokemon
import pytest

@pytest.fixture
def grass_pokemon():
    return GrassPokemon("Bulbasaur", 45, 16, "Razor leaf")

class TestInstantiation:
    def test_new_instance_is_instance_of_class_grass_pokemon(self, grass_pokemon):
        assert isinstance(grass_pokemon, GrassPokemon)

    def test_grass_pokemon_is_child_of_pokemon_class(self, grass_pokemon):
        assert issubclass(type(grass_pokemon), Pokemon)

    def test_grass_pokemon_is_instantiated_with_grass_type(self, grass_pokemon):
        assert grass_pokemon.type == "grass"

    def test_grass_pokemon_is_instantiated_with_strong_against_property(self, grass_pokemon):
        assert grass_pokemon.strong_against == ["water"]

    def test_grass_pokemon_is_instantiated_with_weak_against_property(self, grass_pokemon):
        assert grass_pokemon.weak_against == ["fire"]