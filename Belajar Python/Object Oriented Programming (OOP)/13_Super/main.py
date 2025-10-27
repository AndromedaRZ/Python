class Hero:
    def __init__(self, name, health):
        self.name = name
        self.health = health
    
    def showInfo(self):
        print("{} : \thealth : {}".format(self.name, self.health))
    
class Hero_intelligent(Hero):
    def __init__(self, name):
        self.name = name
        # Hero.__init__(self, name, 100)
        super().__init__(name, 100) # mengambil __init__ yang ada di super class (di atas)
        super().showInfo()

class Hero_fighter(Hero):
    def __init__(self, name):
        super().__init__(name, 200) # mengambil __init__ yang ada di super class (di atas)
        super().showInfo()



einstein = Hero_intelligent('Einstein')
alpha = Hero_fighter('alpha')
