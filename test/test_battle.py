from src.battle import Battle
from src.fire_pokemon import FirePokemon
from src.water_pokemon import WaterPokemon
import pytest

@pytest.fixture
def fire_pokemon():
    return FirePokemon("Charmander", 44, 17, "Flamethrower")

@pytest.fixture
def water_pokemon():
    return WaterPokemon("Squirtle", 44, 16, "Surf")

class TestInstantiation:
    def test_instance_is_instantiated_with_two_given_pokemon(self, fire_pokemon, water_pokemon):
        battle = Battle(fire_pokemon, water_pokemon)
        assert battle.pokemon_1 == fire_pokemon
        assert battle.pokemon_2 == water_pokemon

