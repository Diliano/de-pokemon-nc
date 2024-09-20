from src.trainer import Trainer, BeltFullError
from src.pokeball import Pokeball
from src.fire_pokemon import FirePokemon
import pytest

@pytest.fixture
def trainer():
    return Trainer()

@pytest.fixture
def charmander():
    return FirePokemon("Charmander", 44, 17, "Flamethrower")

class TestInstantiation:
    def test_new_instance_is_instance_of_trainer_class(self, trainer):
        assert isinstance(trainer, Trainer)

    def test_new_instance_is_instantiated_with_belt_property_containing_six_pokeballs(self, trainer):
        assert len(trainer.belt) == 6
        for pokeball in trainer.belt:
            assert isinstance(pokeball, Pokeball)

class TestThrowPokeballMethod:
    def test_throw_pokeball_method_uses_a_pokeball_to_catch_a_given_pokemon(self, trainer, charmander):
        trainer.throw_pokeball(charmander)
        assert any(pokeball.pokemon == charmander for pokeball in trainer.belt)
        
    def test_throw_pokeball_method_raises_belt_full_exception_if_no_available_pokeballs(self, trainer, charmander):
        trainer.throw_pokeball(charmander)
        trainer.throw_pokeball(charmander)
        trainer.throw_pokeball(charmander)
        trainer.throw_pokeball(charmander)
        trainer.throw_pokeball(charmander)
        trainer.throw_pokeball(charmander)
        with pytest.raises(BeltFullError) as excinfo:
            trainer.throw_pokeball(charmander)
        assert str(excinfo.value) == "All of the Pokeballs on the belt already contain a Pokemon"