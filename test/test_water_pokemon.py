from src.water_pokemon import WaterPokemon
from src.pokemon import Pokemon
import pytest

@pytest.fixture
def water_pokemon():
    return WaterPokemon("Squirtle", 44, 16, "Surf")

class TestInstantiation:
    def test_new_instance_is_instance_of_class_water_pokemon(self, water_pokemon):
        assert isinstance(water_pokemon, WaterPokemon)

    def test_water_pokemon_is_child_of_pokemon_class(self, water_pokemon):
        assert issubclass(type(water_pokemon), Pokemon)

    def test_water_pokemon_is_instantiated_with_water_type(self, water_pokemon):
        assert water_pokemon.type == "water"

    def test_water_pokemon_is_instantiated_with_strong_against_property(self, water_pokemon):
        assert water_pokemon.strong_against == ["fire"]

    def test_water_pokemon_is_instantiated_with_weak_against_property(self, water_pokemon):
        assert water_pokemon.weak_against == ["grass"]