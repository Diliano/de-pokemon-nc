from src.pokeball import Pokeball, PokeballFullError
from src.fire_pokemon import FirePokemon
from src.water_pokemon import WaterPokemon
import pytest

@pytest.fixture
def pokeball():
    return Pokeball()

@pytest.fixture
def fire_pokemon():
    return FirePokemon("Charmander", 44, 17, "Flamethrower")

@pytest.fixture
def water_pokemon():
    return WaterPokemon("Squirtle", 44, 16, "Surf")

class TestInstantiation:
    def test_pokeball_instance_is_instance_of_pokeball_class(self, pokeball):
        assert isinstance(pokeball, Pokeball)

    def test_pokeball_is_instantiated_with_pokemon_property_none(self, pokeball):
        assert pokeball.pokemon is None

class TestCatchMethod:
    def test_catch_method_captures_and_stores_given_pokemon_if_pokeball_is_empty(self, pokeball, fire_pokemon):
        pokeball.catch(fire_pokemon)
        assert pokeball.pokemon == fire_pokemon

    def test_catch_method_raises_pokeball_full_exception_if_pokeball_has_pokemon_already(self, pokeball, fire_pokemon, water_pokemon):
        pokeball.catch(fire_pokemon)
        with pytest.raises(PokeballFullError) as excinfo:
            pokeball.catch(water_pokemon)
        assert str(excinfo.value) == "The Pokeball already contains a Pokemon"

class TestIsEmptyMethod:
    def test_is_empty_method_returns_true_if_pokeball_does_not_contain_a_pokemon(self, pokeball):
        assert pokeball.is_empty()

    def test_is_empty_method_returns_false_if_pokeball_contains_a_pokemon(self, pokeball, fire_pokemon):
        pokeball.catch(fire_pokemon)
        assert not pokeball.is_empty() 