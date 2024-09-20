class Pokeball:
    def __init__(self):
        self._pokemon = None

    @property
    def pokemon(self):
        return self._pokemon