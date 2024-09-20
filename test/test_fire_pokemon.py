from src.fire_pokemon import FirePokemon
from src.pokemon import Pokemon
import pytest

@pytest.fixture
def charmander():
    return FirePokemon("Charmander", 44, 17, "Flamethrower")

class TestInstantiation:
    def test_new_instance_is_instance_of_class_fire_pokemon(self, charmander):
        assert isinstance(charmander, FirePokemon)

    def test_fire_pokemon_is_child_of_pokemon_class(self, charmander):
        assert issubclass(type(charmander), Pokemon)

    def test_fire_pokemon_is_instantiated_with_fire_type(self, charmander):
        assert charmander.type == "fire"

    def test_fire_pokemon_is_instantiated_with_strong_against_property(self, charmander):
        assert charmander.strong_against == ["grass"]

    def test_fire_pokemon_is_instantiated_with_weak_against_property(self, charmander):
        assert charmander.weak_against == ["water"]