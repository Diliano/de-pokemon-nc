from src.normal_pokemon import NormalPokemon
from src.pokemon import Pokemon
import pytest

@pytest.fixture
def normal_pokemon():
    return NormalPokemon("Eevee", 55, 18, "Headbutt")

class TestInstantiation:
    def test_new_instance_is_instance_of_class_normal_pokemon(self, normal_pokemon):
        assert isinstance(normal_pokemon, NormalPokemon)

    def test_normal_pokemon_is_child_of_pokemon_class(self, normal_pokemon):
        assert issubclass(type(normal_pokemon), Pokemon)

    def test_normal_pokemon_is_instantiated_with_normal_type(self, normal_pokemon):
        assert normal_pokemon.type == "normal"

    def test_normal_pokemon_is_instantiated_with_default_parent_strong_against_property(self, normal_pokemon):
        assert normal_pokemon.strong_against == []

    def test_normal_pokemon_is_instantiated_with_default_parent_weak_against_property(self, normal_pokemon):
        assert normal_pokemon.weak_against == []