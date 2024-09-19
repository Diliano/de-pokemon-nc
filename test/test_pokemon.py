from src.pokemon import Pokemon
import types

class TestInstantiation:
    def test_new_instance_is_an_instance_of_class_pokemon(self):
        my_pokemon = Pokemon("Bulbasaur", 45, 16, "Razor leaf")
        assert isinstance(my_pokemon, Pokemon)

    def test_is_instantiated_with_given_name(self):
        my_pokemon = Pokemon("Bulbasaur", 45, 16, "Razor leaf")
        assert my_pokemon.name == "Bulbasaur"

    def test_is_instantiated_with_given_hit_points(self):
        my_pokemon = Pokemon("Bulbasaur", 45, 16, "Razor leaf")
        assert my_pokemon.hit_points == 45

    def test_is_instantiated_with_given_attack_damage(self):
        my_pokemon = Pokemon("Bulbasaur", 45, 16, "Razor leaf")
        assert my_pokemon.attack_damage == 16

    def test_is_instantiated_with_given_move(self):
        my_pokemon = Pokemon("Bulbasaur", 45, 16, "Razor leaf")
        assert my_pokemon.move == "Razor leaf"

class TestUseMoveMethod:
    def test_use_move_method_is_a_method(self):
        my_pokemon = Pokemon("Bulbasaur", 45, 16, "Razor leaf")
        assert isinstance(my_pokemon.use_move, types.MethodType)

    def test_use_move_method_returns_a_formatted_message(self):
        my_pokemon = Pokemon("Bulbasaur", 45, 16, "Razor leaf")
        assert my_pokemon.use_move() == "Bulbasaur used Razor leaf!"

class TestTakeDamageMethod:
    def test_take_damage_method_is_a_method(self):
        my_pokemon = Pokemon("Bulbasaur", 45, 16, "Razor leaf")
        assert isinstance(my_pokemon.take_damage, types.MethodType)

    def test_take_damage_method_reduces_health_by_given_amount(self):
        my_pokemon = Pokemon("Bulbasaur", 45, 16, "Razor leaf")
        my_pokemon.take_damage(15)
        assert my_pokemon.hit_points == 30

    def test_take_damage_method_does_not_reduce_hit_points_beyond_0(self):
        my_pokemon = Pokemon("Bulbasaur", 45, 16, "Razor leaf")
        my_pokemon.take_damage(50)
        assert my_pokemon.hit_points == 0

    def test_take_damage_method_returns_message_given_negative_damage(self):
        my_pokemon = Pokemon("Bulbasaur", 45, 16, "Razor leaf")
        assert my_pokemon.take_damage(-5) == "Damage cannot be negative!"

class TestHasFaintedMethod:
    def test_has_fainted_method_is_a_method(self):
        my_pokemon = Pokemon("Bulbasaur", 45, 16, "Razor leaf")
        assert isinstance(my_pokemon.has_fainted, types.MethodType)

    def test_has_fainted_method_returns_true_if_hit_points_are_zero(self):
        my_pokemon = Pokemon("Bulbasaur", 45, 16, "Razor leaf")
        my_pokemon.take_damage(45)
        assert my_pokemon.has_fainted() == True

    def test_has_fainted_method_returns_false_if_hit_points_are_more_than_zero(self):
        my_pokemon = Pokemon("Bulbasaur", 45, 16, "Razor leaf")
        my_pokemon.take_damage(15)
        assert my_pokemon.has_fainted() == False