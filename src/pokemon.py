class Pokemon:
    def __init__(self, name, hit_points, attack_damage, move):
        self.__name = name
        self.__hit_points = hit_points

    @property
    def name(self):
        return self.__name
    
    @property
    def hit_points(self):
        return self.__hit_points