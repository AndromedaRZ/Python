'''
Latihan Encapsulasi
'''

class Servant:
    
    # private class variabel
    __jumlah = 0
    
    def __init__(self, name, health, attack, defense):
        self.__name = name
        self.__healthStandar = health
        self.__attackStandar = attack
        self.__defenseStandar = defense
        self.__level = 1
        self.__exp = 0
        
        self.__healthMax = self.__healthStandar * self.__level # max health point yang dimiliki karakter
        self.__attackPower = self.__attackStandar * self.__level # total attack power yang dimiliki karakter
        self.__defense = self.__defenseStandar * self.__level # total defense yang dimiliki karakter
        
        self.__health = self.__healthMax # health point saat ini yang dimiliki karakter
        
        Servant.__jumlah += 1
        
    @property
    def info(self):
        return "{} : \n\tlevel = {}\n\thealth = {}/{}\n\tattack = {}\n\tdefense = {}".format(self.__name, self.__level, self.__health, self.__healthMax, self.__attackPower, self.__defense)
    
    @property
    def gainExp(self):
        pass
    
    # setter untuk servant level up
    @gainExp.setter
    def gainExp(self, addExp):
        self.__exp += addExp
        if (self.__exp >= 100):
            print(self.__name, 'level up')
            self.__level += 1
            self.__exp -= 100
            
            self.__healthMax = self.__healthStandar * self.__level # max health point yang dimiliki karakter
            self.__attackPower = self.__attackStandar * self.__level # total attack power yang dimiliki karakter
            self.__defense = self.__defenseStandar * self.__level # total defense yang dimiliki karakter
        
        
    def attack(self, lawan):
        self.gainExp = 50
    
saber = Servant("Saber", 200, 100, 50)
archer = Servant("Archer", 150, 150, 30)

print(saber.info)

saber.attack(archer)
saber.attack(archer)
saber.attack(archer)
print(saber.info)
print(saber.__dict__)