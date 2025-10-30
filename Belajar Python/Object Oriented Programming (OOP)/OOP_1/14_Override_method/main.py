class Hero:
    def __init__(self, name, health):
        self.name = name
        self.health = health
        
    def showInfo(self):
        print("showInfo di class Hero")
        print("{} health : {}".format(self.name, self.health))
        
class Hero_fighter(Hero):
    def __init__(self,name):
        super().__init__(name,200)
        
    # menimpa showInfo yang di atas, override
    def showInfo(self):
        print("showInfo di subclass Hero_fighter")
        print("{} \n\tclass: fighter \n\thealth: {}".format(self.name, self.health))
        
class Hero_medic(Hero):
    def __init__(self,name):
        super().__init__(name,300)
        
        
lucia = Hero_fighter('lucia')
liv = Hero_medic('liv')

lucia.showInfo()
liv.showInfo()
