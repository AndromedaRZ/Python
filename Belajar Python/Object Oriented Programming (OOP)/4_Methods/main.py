class Servant:
    # class variabel
    jumlah_servant = 0
    
    def __init__(self, inputName, inputHealth, inputAttack, inputArmor):
        # instance variabel
        self.name = inputName
        self.health = inputHealth
        self.attack = inputAttack
        self.armor = inputArmor
        Servant.jumlah_servant += 1
    
    # mendefinisikan method tanpa return dan tanpa argumen
    def siapa(self):
        print("nama ku adalah " + self.name) 
        
    # mendefinisikan method dengan argumen dan tanpa return
    def healthUp(self, up):
        self.health += up
        
    def attackUp(self, up):
        self.attack += 10
    
    # mendefinisikan method dengan return
    def getHealth(self):
        return self.health
    
    
servant1 = Servant('saber', 200, 100, 100)
servant2 = Servant('archer', 150, 150, 50)
servant3 = Servant('assassin', 200, 160, 50)

servant1.siapa()
servant1.healthUp(20)
servant1.attackUp(20)
print(servant1.getHealth())
print(servant1.attack)

# print(servant1.__dict__)
# print(servant2.__dict__)
# print(servant3.__dict__)


        