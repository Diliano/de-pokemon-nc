class Pokemon:
    def __init__(self, name, hit_points, attack_damage, move):
        self.__name = name
        self.__hit_points = hit_points
        self.__attack_damage = attack_damage
        self.__move = move

    @property
    def name(self):
        return self.__name
    
    @property
    def hit_points(self):
        return self.__hit_points
    
    @property 
    def attack_damage(self):
        return self.__attack_damage
    
    @property
    def move(self):
        return self.__move