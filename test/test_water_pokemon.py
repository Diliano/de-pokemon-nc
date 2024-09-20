from src.water_pokemon import WaterPokemon
from src.pokemon import Pokemon
import pytest

@pytest.fixture
def squirtle():
    return WaterPokemon("Squirtle", 44, 16, "Surf")

class TestInstantiation:
    def test_new_instance_is_instance_of_class_water_pokemon(self, squirtle):
        assert isinstance(squirtle, WaterPokemon)

    def test_water_pokemon_is_child_of_pokemon_class(self, squirtle):
        assert issubclass(type(squirtle), Pokemon)

    def test_water_pokemon_is_instantiated_with_water_type(self, squirtle):
        assert squirtle.type == "water"

    def test_water_pokemon_is_instantiated_with_strong_against_property(self, squirtle):
        assert squirtle.strong_against == ["fire"]

    def test_water_pokemon_is_instantiated_with_weak_against_property(self, squirtle):
        assert squirtle.weak_against == ["grass"]