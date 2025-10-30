'''
Inheritance
'''

class Hero: # Hero disini sebagai super class
    
    def __init__(self, name, health):
        self.name = name
        self.health = health

# inheritance
class Hero_fighter(Hero): # sub class 1
    pass

class Hero_ranger(Hero): # sub class 2
    pass
        
guardian = Hero('guardian', 200)
berserker = Hero_fighter('berserker', 100)
archer = Hero_ranger('archer', 80)


print(guardian.name)
print(berserker.__dict__)
print(archer.__dict__)
