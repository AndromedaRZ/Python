class Hero:
    def __init__(self, name, health, attack):
        # private variabel
        self.__name = name
        self.__health = health
        self.__attack = attack
        
    # getter
    def getName(self):
        return self.__name
    
    def getHealth(self):
        return self.__health

    # setter
    def diserang(self,attackPower):
        self.__health -= attackPower
        
    def setAttPower(self,nilaiBaru):
        self.__attPower = nilaiBaru
    
# misalkan awal dari gamenya

guardian = Hero("guardian", 100, 50)

print(guardian.__dict__)

# saat gamenya sudah berjalan

guardian.__name = "knight" # jika kita berusaha merubah private variabel yang ada di atas, bukannya berubah tetapi malah membuat variabel yang baru
print(guardian.__dict__)

print(guardian.getName())
print(guardian.getHealth())
guardian.diserang(10)
print(guardian.getHealth())
