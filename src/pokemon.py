class Pokemon:
    def __init__(self, name, hit_points, attack_damage, move):
        self._name = name
        self._hit_points = hit_points
        self._attack_damage = attack_damage
        self._move = move
        self._type = None
        self._strong_against = []
        self._weak_against = []

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
    
    @property
    def type(self):
        return self._type
    
    @property
    def strong_against(self):
        return self._strong_against
    
    @property
    def weak_against(self):
        return self._weak_against
    
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