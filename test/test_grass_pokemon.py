from src.grass_pokemon import GrassPokemon
from src.pokemon import Pokemon
import pytest

@pytest.fixture
def bulbasaur():
    return GrassPokemon("Bulbasaur", 45, 16, "Razor leaf")

class TestInstantiation:
    def test_new_instance_is_instance_of_class_grass_pokemon(self, bulbasaur):
        assert isinstance(bulbasaur, GrassPokemon)

    def test_grass_pokemon_is_child_of_pokemon_class(self, bulbasaur):
        assert issubclass(type(bulbasaur), Pokemon)

    def test_grass_pokemon_is_instantiated_with_grass_type(self, bulbasaur):
        assert bulbasaur.type == "grass"

    def test_grass_pokemon_is_instantiated_with_strong_against_property(self, bulbasaur):
        assert bulbasaur.strong_against == ["water"]

    def test_grass_pokemon_is_instantiated_with_weak_against_property(self, bulbasaur):
        assert bulbasaur.weak_against == ["fire"]