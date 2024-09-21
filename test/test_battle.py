from src.battle import Battle, AlreadyFaintedError
from src.fire_pokemon import FirePokemon
from src.water_pokemon import WaterPokemon
from src.grass_pokemon import GrassPokemon
from src.normal_pokemon import NormalPokemon
import pytest

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
    def test_instance_is_instantiated_with_two_given_pokemon(self, charmander, squirtle):
        battle = Battle(charmander, squirtle)
        assert battle.pokemon_1 == charmander
        assert battle.pokemon_2 == squirtle

    def test_instance_is_instantiated_with_pokemon_1_turn_property(self, charmander, squirtle):
        battle = Battle(charmander, squirtle)
        assert battle.pokemon_1_turn is True

class TestTakeTurnMethod:
    def test_take_turn_method_starts_with_pokemon_1(self, charmander, squirtle):
        battle = Battle(charmander, squirtle)
        assert battle.pokemon_1_turn is True

    def test_take_turn_method_calculates_and_deals_damage(self, charmander, squirtle):
        battle = Battle(charmander, squirtle)
        battle.take_turn()
        assert squirtle.hit_points == 36

    def test_take_turn_method_switches_attacker_after_each_call(self, charmander, squirtle):
        battle = Battle(charmander, squirtle)
        assert battle.pokemon_1_turn is True
        battle.take_turn()
        assert battle.pokemon_1_turn is False

    def test_take_turn_method_handles_multiple_turns(self, charmander, squirtle):
        battle = Battle(charmander, squirtle)
        battle.take_turn()
        assert squirtle.hit_points == 36
        battle.take_turn()
        assert charmander.hit_points == 20
        battle.take_turn()
        assert squirtle.hit_points == 28

    def test_take_turn_method_raises_already_fainted_exception_if_a_pokemon_has_already_fainted(self, charmander, squirtle):
        battle = Battle(charmander, squirtle)
        battle.take_turn()
        assert squirtle.hit_points == 36
        battle.take_turn()
        assert charmander.hit_points == 20
        battle.take_turn()
        assert squirtle.hit_points == 28
        battle.take_turn()
        assert charmander.hit_points == 0
        with pytest.raises(AlreadyFaintedError) as excinfo:
            battle.take_turn()
        assert str(excinfo.value) == "A Pokemon has already fainted - time to rest!"

class TestGetWinnerMethod:
    def test_get_winner_method_returns_winning_pokemon_if_other_has_fainted(self, charmander, squirtle, bulbasaur, eevee):
        battle = Battle(charmander, squirtle)
        battle.take_turn()
        assert squirtle.hit_points == 36
        battle.take_turn()
        assert charmander.hit_points == 20
        battle.take_turn()
        assert squirtle.hit_points == 28
        battle.take_turn()
        assert charmander.hit_points == 0
        assert battle.get_winner() == battle.pokemon_2

        battle = Battle(bulbasaur, eevee)
        battle.take_turn()
        assert eevee.hit_points == 39
        battle.take_turn()
        assert bulbasaur.hit_points == 27
        battle.take_turn()
        assert eevee.hit_points == 23
        battle.take_turn()
        assert bulbasaur.hit_points == 9
        battle.take_turn()
        assert eevee.hit_points == 7
        battle.take_turn()
        assert bulbasaur.hit_points == 0
        assert battle.get_winner() == battle.pokemon_2

    def test_get_winner_method_returns_none_if_neither_pokemon_has_fainted(self, charmander, squirtle):
        battle = Battle(charmander, squirtle)
        battle.take_turn()
        assert squirtle.hit_points == 36
        battle.take_turn()
        assert charmander.hit_points == 20
        assert battle.get_winner() is  None