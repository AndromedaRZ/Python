'''
konsep oop menggunakan encapculasi

encasulapsi:
semua variabel bersifat encapsulasi
cara mengambil datanya harus menggunakan getter & setter
getter = digunakan untuk mengambil variabel
setter = digunakan untuk mensetting (mengatur) variabel

> contoh getter:
misalnya kita membuat sebuah game saling serang menyerang
dan membuat object 'nama' dengan menggunakan private variable
maka 'nama' tersebut tidak boleh berubah nilainya selama program atau gamenya berjalan
# alasan 'nama' ini dibuat private juga agar tidak bisa diubah dengan mudah dari luar

> contoh setter:
misalnya kita membuat sebuah game saling serang menyerang
maka 'health' karakter yang kita gunakan tidak boleh berkurang sampai lebih kecil dari 0 dan menyebabkan mines

'''

class Servant:
    
    def __init__(self, name, hp, atk):
        self.__name = name
        self.__hp = hp
        self.__atk = atk
        
    # getter
    def getName(self):
        return self.__name
    
    def getHealth(self):
        return self.__hp
    
    # setter
    def attacked(self, atk_value):
        self.__hp -= atk_value # melakukan perhitungan di belakang layar untuk mengubah hp-nya
            
    def atk_value(self, atk_baru):
        self.__atk = atk_baru
        
        
        
        
# awal dari game
berserker = Servant('berserker', 220, 50)

print(berserker.__dict__) # bisa kita lihat semuanya adalah private variable

# game berjalan

# print(berserker.__name) # hasilnya akan error
print(berserker.getName())
# cara yang boleh dilakukan untuk menampilkan datanya adalah dengan menggunakan getter seperti di atas

print(berserker.getHealth())
berserker.attacked(10)
print(berserker.getHealth())
# cara yang boleh digunakan untuk mengubah nilai datanya adalah dengan menggunakan setter seperti di atas

# encapsulasi berguna untuk membantu kita mengurangi bug pada program yang kita buat
# memudahkan kita untuk memaintain setiap object
# mencegah penggunaan variable yang terlalu banyak