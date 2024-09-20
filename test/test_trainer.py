from src.trainer import Trainer
from src.pokeball import Pokeball
import pytest

@pytest.fixture
def trainer():
    return Trainer()

class TestInstantiation:
    def test_new_instance_is_instance_of_trainer_class(self, trainer):
        assert isinstance(trainer, Trainer)

    def test_new_instance_is_instantiated_with_belt_property_containing_six_pokeballs(self, trainer):
        assert len(trainer.belt) == 6
        for item in trainer.belt:
            assert isinstance(item, Pokeball)