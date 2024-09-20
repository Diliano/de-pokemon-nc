from src.pokemon import Pokemon
from src.fire_pokemon import FirePokemon
from src.water_pokemon import WaterPokemon
from src.grass_pokemon import GrassPokemon
from src.normal_pokemon import NormalPokemon
import types
import pytest

@pytest.fixture
def generic_pokemon():
    return Pokemon("Test", 50, 50, "Test")

@pytest.fixture
def charmander():
    return FirePokemon("Charmander", 44, 17, "Flamethrower")

@pytest.fixture
def squirtle():
    return WaterPokemon("Squirtle", 44, 16, "Surf")

@pytest.fixture
def bulbasaur():
    return GrassPokemon("Bulbasaur", 45, 16, "Razor leaf")

@pytest.fixture
def eevee():
    return NormalPokemon("Eevee", 55, 18, "Headbutt")

class TestInstantiation:
    def test_new_instance_is_an_instance_of_class_pokemon(self, generic_pokemon):
        assert isinstance(generic_pokemon, Pokemon)

    def test_is_instantiated_with_given_name(self, generic_pokemon):
        assert generic_pokemon.name == "Test"

    def test_is_instantiated_with_given_hit_points(self, generic_pokemon):
        assert generic_pokemon.hit_points == 50

    def test_is_instantiated_with_given_attack_damage(self, generic_pokemon):
        assert generic_pokemon.attack_damage == 50

    def test_is_instantiated_with_given_move(self, generic_pokemon):
        assert generic_pokemon.move == "Test"

class TestUseMoveMethod:
    def test_use_move_method_is_a_method(self, generic_pokemon):
        assert isinstance(generic_pokemon.use_move, types.MethodType)

    def test_use_move_method_returns_a_formatted_message(self, generic_pokemon):
        assert generic_pokemon.use_move() == "Test used Test!"

class TestTakeDamageMethod:
    def test_take_damage_method_is_a_method(self, generic_pokemon):
        assert isinstance(generic_pokemon.take_damage, types.MethodType)

    def test_take_damage_method_reduces_health_by_given_amount(self, generic_pokemon):
        generic_pokemon.take_damage(15)
        assert generic_pokemon.hit_points == 35

    def test_take_damage_method_does_not_reduce_hit_points_beyond_0(self, generic_pokemon):
        generic_pokemon.take_damage(70)
        assert generic_pokemon.hit_points == 0

    def test_take_damage_method_raises_value_error_given_negative_damage(self, generic_pokemon):
        with pytest.raises(ValueError) as excinfo:
            generic_pokemon.take_damage(-5)
        assert str(excinfo.value) == "Damage cannot be negative!"

class TestHasFaintedMethod:
    def test_has_fainted_method_is_a_method(self, generic_pokemon):
        assert isinstance(generic_pokemon.has_fainted, types.MethodType)

    def test_has_fainted_method_returns_true_if_hit_points_are_zero(self, generic_pokemon):
        generic_pokemon.take_damage(50)
        assert generic_pokemon.has_fainted() == True

    def test_has_fainted_method_returns_false_if_hit_points_are_more_than_zero(self, generic_pokemon):
        generic_pokemon.take_damage(15)
        assert generic_pokemon.has_fainted() == False

class TestGetMultiplierMethod:
    def test_get_multiplier_method_returns_1_point_5_if_existing_pokemon_is_strong_against_given_pokemon(self, charmander, bulbasaur):
        assert charmander.get_multiplier(bulbasaur) == 1.5

    def test_get_multiplier_method_returns_0_point_5_if_existing_pokemon_is_weak_against_given_pokemon(self, charmander, squirtle):
        assert charmander.get_multiplier(squirtle) == 0.5
    
    def test_get_multiplier_method_returns_1_if_existing_pokemon_is_neither_strong_or_weak_against_given_pokemon(self, eevee, squirtle):
        assert eevee.get_multiplier(squirtle) == 1