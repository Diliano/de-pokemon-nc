class Pokemon:
    def __init__(self, name, hit_points, attack_damage, move):
        self._name = name
        self._hit_points = hit_points
        self._attack_damage = attack_damage
        self._move = move

    @property
    def name(self):
        return self._name
    
    @property
    def hit_points(self):
        return self._hit_points
    
    @property 
    def attack_damage(self):
        return self._attack_damage
    
    @property
    def move(self):
        return self._move
    
    def use_move(self):
        return f"{self._name} used {self._move}!"
    
    def take_damage(self, damage):
        if damage < 0:
            return "Damage cannot be negative!"
        
        if damage > self._hit_points:
            self._hit_points = 0
        else:
            self._hit_points -= damage

    def has_fainted(self):
        return self._hit_points == 0