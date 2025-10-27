from . import Character
    
class Goblin(Character):
    def __init__(self, name):
        super().__init__(name, 'Goblin')
        self.hp_pool = [0,100,200,300,400,500]
        self.atk_pool = [0,10,20,30,40,50]
        self.armor_pool = [0,1,2,3,4,5]
        self.levelUp = 1
        
class Skeleton(Character):
    def __init__(self, name):
        pass

class Necromancer(Character):
    def __init__(self, name):
        pass

class Berserker(Character):
    def __init__(self, name):
        pass
