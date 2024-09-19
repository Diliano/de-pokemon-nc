class Pokemon():
    def __init__(self, name, hit_points, attack_damage, move):
        self.__name = name

    @property
    def name(self):
        return self.__name