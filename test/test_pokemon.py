from src.pokemon import Pokemon

class TestInstantiation:
    def test_new_instance_is_an_instance_of_class_pokemon(self):
        my_pokemon = Pokemon("Bulbasaur", 45, 16, "Razor leaf")
        assert isinstance(my_pokemon, Pokemon)