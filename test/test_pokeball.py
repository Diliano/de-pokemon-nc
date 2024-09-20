from src.pokeball import Pokeball
import pytest

@pytest.fixture
def pokeball():
    return Pokeball()

class TestInstantiation:
    def test_pokeball_instance_is_instance_of_pokeball_class(self, pokeball):
        assert isinstance(pokeball, Pokeball)

    def test_pokeball_is_instantiated_with_pokemon_property_none(self, pokeball):
        assert pokeball.pokemon == None