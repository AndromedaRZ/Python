# fraksi karakter
class Faction:
    def setFaction(self, fraksi):
        self.fraksi = fraksi
        
    # def showFaction(self):
    #     return self.fraksi
        
# role karakter
class Role:
    def setRole(self, role):
        self.role = role
    
    # def showRole(self):
    #     return self.role


class Hero(Role, Faction):
    def __init__(self, name, health):
        self.name = name
        self.health = health
        
    def showChar(self):
        print("{} =\tfaction: {}\n\trole: {}".format(self.name, self.fraksi, self.role))
        
aisa = Hero('Aisa', 100)
aisa.setFaction("resistance")
aisa.setRole("ranger")


aisa.showChar()





