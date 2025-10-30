# membuat encapsulasi untuk class Servant

class Servant:
    
    # private class variable
    __jumlah = 0
    
    def __init__(self, name):
        self.__name = name
        Servant.__jumlah += 1
        
    # method ini hanya berlaku untuk object, tidak berlaku kepada class
    def getJumlah(self):
        return Servant.__jumlah
    
    # method ini tidak berlaku untuk object tapi berlaku untuk class, karena tidak ada parameter 'self'
    def getJumlah2():
        return Servant.__jumlah
    
    # berikutnya kita aka nmembuat method yang berlaku untuk object dan class juga
    # kita akan gunakan yang namanya static method (decorator)
    @staticmethod # ini disebut decorator
    def getJumlah3():
        return Servant.__jumlah # akan menempel ke object dan classnya
    
    @classmethod # decorator yang bisa mengambil argument
    def getJumlah3(cls): # cls bisa diisi argument dari object maupun class
        return cls.__jumlah
         
        
saber = Servant('Saber')

print(saber.getJumlah()) # method yang hanya bisa kita gunakan untuk object
print(Servant.getJumlah2()) # method yang hanya bisa kita gunakan untuk class

archer = Servant('Archer')

print(saber.getJumlah3()) # menggunakan decorator
print(Servant.getJumlah3()) # menggunakan decorator

lancer = Servant('Lancer')

print(saber.getJumlah3())
