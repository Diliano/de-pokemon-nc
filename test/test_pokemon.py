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

class TestUseMoveMethod():
    def test_use_move_method_is_a_method(self):
        my_pokemon = Pokemon("Bulbasaur", 45, 16, "Razor leaf")
        assert isinstance(my_pokemon.use_move, types.MethodType)

    def test_use_move_method_returns_a_formatted_message(self):
        my_pokemon = Pokemon("Bulbasaur", 45, 16, "Razor leaf")
        assert my_pokemon.use_move() == "Bulbasaur used Razor leaf!"