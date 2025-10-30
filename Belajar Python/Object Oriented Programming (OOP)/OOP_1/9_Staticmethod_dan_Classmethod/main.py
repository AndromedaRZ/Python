class Hero:
    
    # private class variabel
    __jumlah = 0
    
    def __init__(self, name):
        self.name = name
        Hero.__jumlah += 1
    
    # method ini hanya berlaku untuk objek, tidak bisa mengambil nilai dari private class
    def getJumlah(self):
        return Hero.__jumlah
    
    # method ini tidak berlaku untuk objek tetapi berlaku untuk class
    def getJumlah1():
        return Hero.__jumlah
    
    # method static (decorator), method ini akan menempel ke objek dan classnya
    @staticmethod
    def getJumlah2():
        return Hero.__jumlah
    
    @classmethod
    def getJumlah3(cls):
        return cls.__jumlah
    
knight = Hero('knight')
# print(knight.getJumlah())
# print(Hero.getJumlah1())
print(Hero.getJumlah2())
archer = Hero('archer')
print(knight.getJumlah2())
guardian = Hero('guardian')
print(knight.getJumlah3())
