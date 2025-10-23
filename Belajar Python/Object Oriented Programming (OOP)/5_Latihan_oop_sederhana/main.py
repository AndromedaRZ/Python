'''
Membuat game sederhana, pertarungan sederhana
'''

class Hero:
    
    def __init__(self,name,health,attackPower,defense):
        self.name = name
        self.health = health
        self.attack = attackPower
        self.defense = defense
    
    # membuat 2 method untuk 'menyerang' dan 'diserang'
    def serang(self, lawan): # membuat 2 argumen untuk penyerang dan yang diserang
        print(self.name + ' menyerang ' + lawan.name)
        lawan.diserang(self, self.attack)
        
    def diserang(self, lawan, attackPower_lawan):
        print(self.name + ' diserang ' + lawan.name)
        damage = attackPower_lawan/self.defense
        print('kerusakan diterima : ' + str(damage))
        self.health -= damage
        print('health ' + self.name + ' tersisa ' + str(self.health))
        
        
        
magical_girl = Hero('magical girl', 50, 25, 5)
wizard_boy = Hero('wizard boy', 100, 20, 10)

magical_girl.serang(wizard_boy)
print("\n")
wizard_boy.serang(magical_girl)
