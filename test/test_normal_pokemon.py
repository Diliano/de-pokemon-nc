from src.normal_pokemon import NormalPokemon
from src.pokemon import Pokemon
import pytest

@pytest.fixture
def eevee():
    return NormalPokemon("Eevee", 55, 18, "Headbutt")

class TestInstantiation:
    def test_new_instance_is_instance_of_class_normal_pokemon(self, eevee):
        assert isinstance(eevee, NormalPokemon)

    def test_normal_pokemon_is_child_of_pokemon_class(self, eevee):
        assert issubclass(type(eevee), Pokemon)

    def test_normal_pokemon_is_instantiated_with_normal_type(self, eevee):
        assert eevee.type == "normal"

    def test_normal_pokemon_is_instantiated_with_default_parent_strong_against_property(self, eevee):
        assert eevee.strong_against == []

    def test_normal_pokemon_is_instantiated_with_default_parent_weak_against_property(self, eevee):
        assert eevee.weak_against == []