from src.pokemon import Pokemon
from src.fire_pokemon import FirePokemon
from src.water_pokemon import WaterPokemon
from src.grass_pokemon import GrassPokemon
from src.normal_pokemon import NormalPokemon
import types
import pytest

@pytest.fixture
def pokemon():
    return Pokemon("Test", 50, 50, "Test")

@pytest.fixture
def fire_pokemon():
    return FirePokemon("Charmander", 44, 17, "Flamethrower")

@pytest.fixture
def water_pokemon():
    return WaterPokemon("Squirtle", 44, 16, "Surf")

@pytest.fixture
def grass_pokemon():
    return GrassPokemon("Bulbasaur", 45, 16, "Razor leaf")

@pytest.fixture
def normal_pokemon():
    return NormalPokemon("Eevee", 55, 18, "Headbutt")

class TestInstantiation:
    def test_new_instance_is_an_instance_of_class_pokemon(self, pokemon):
        assert isinstance(pokemon, Pokemon)

    def test_is_instantiated_with_given_name(self, pokemon):
        assert pokemon.name == "Test"

    def test_is_instantiated_with_given_hit_points(self, pokemon):
        assert pokemon.hit_points == 50

    def test_is_instantiated_with_given_attack_damage(self, pokemon):
        assert pokemon.attack_damage == 50

    def test_is_instantiated_with_given_move(self, pokemon):
        assert pokemon.move == "Test"

class TestUseMoveMethod:
    def test_use_move_method_is_a_method(self, pokemon):
        assert isinstance(pokemon.use_move, types.MethodType)

    def test_use_move_method_returns_a_formatted_message(self, pokemon):
        assert pokemon.use_move() == "Test used Test!"

class TestTakeDamageMethod:
    def test_take_damage_method_is_a_method(self, pokemon):
        assert isinstance(pokemon.take_damage, types.MethodType)

    def test_take_damage_method_reduces_health_by_given_amount(self, pokemon):
        pokemon.take_damage(15)
        assert pokemon.hit_points == 35

    def test_take_damage_method_does_not_reduce_hit_points_beyond_0(self, pokemon):
        pokemon.take_damage(70)
        assert pokemon.hit_points == 0

    def test_take_damage_method_raises_value_error_given_negative_damage(self, pokemon):
        with pytest.raises(ValueError) as excinfo:
            pokemon.take_damage(-5)
        assert str(excinfo.value) == "Damage cannot be negative!"

class TestHasFaintedMethod:
    def test_has_fainted_method_is_a_method(self, pokemon):
        assert isinstance(pokemon.has_fainted, types.MethodType)

    def test_has_fainted_method_returns_true_if_hit_points_are_zero(self, pokemon):
        pokemon.take_damage(50)
        assert pokemon.has_fainted() == True

    def test_has_fainted_method_returns_false_if_hit_points_are_more_than_zero(self, pokemon):
        pokemon.take_damage(15)
        assert pokemon.has_fainted() == False

class TestGetMultiplierMethod:
    def test_get_multiplier_method_returns_1_point_5_if_existing_pokemon_is_strong_against_given_pokemon(self, fire_pokemon, grass_pokemon):
        assert fire_pokemon.get_multiplier(grass_pokemon) == 1.5

    def test_get_multiplier_method_returns_0_point_5_if_existing_pokemon_is_weak_against_given_pokemon(self, fire_pokemon, water_pokemon):
        assert fire_pokemon.get_multiplier(water_pokemon) == 0.5
    
    def test_get_multiplier_method_returns_1_if_existing_pokemon_is_neither_strong_or_weak_against_given_pokemon(self, normal_pokemon, water_pokemon):
        assert normal_pokemon.get_multiplier(water_pokemon) == 1