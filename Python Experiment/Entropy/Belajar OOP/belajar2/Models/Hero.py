
from . import Character

class Knight(Character):
    def __init__(self, name):
        Character.__init__(self, name, 'Knight')
        self.hp_pool = [0,200,300,400,500,600]
        self.atk_pool = [0,20,30,40,50,60]
        self.armor_pool = [0,2,4,6,8,10]
        self.levelUp = 1

class Archer(Character):
    def __init__(self, name):
        super().__init__(name, 'Archer')
        self.hp_pool = [0,150,200,250,300,350]
        self.atk_pool = [0,40,60,80,100,120]
        self.armor_pool = [0,1,2,3,4,5]
        self.levelUp = 1


class Sorcerer(Character):
    def __init__(self, name):
        super().__init__(name, 'Sorcerer')
        self.hp_pool = [0,180,240,300,360,420]
        self.atk_pool = [0,30,45,60,75,90]
        self.armor_pool = [0,1.5,3,4.5,6,7.5]
        self.levelUp = 1