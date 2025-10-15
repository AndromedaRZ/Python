# method

'''
class = template (bisa dikatakan bentuknya masih abstrak)

lalu ada instance
dan object, untuk object ini baru berbentuk ril

Apa itu method?

Sebagai contoh, ketika kita membuat sebuah tombol menggunakan object

pada tombol tersebut menggunakan class 'Tombol' sebagai templatenya
lalu ada atribut lain seperti teks yang terlihat di tombolnya, ukuran tombol, dan warna tombol

dan yang terakhir adalah Method, bisa kita asumsukan method adalah apa yang akan terjadi ketika kita menekan tombolnya
Singkatnya, method menentukan apa yang akan terjadi dengan segala mungkin hal yang kita lakukan terhadap tombol tersebut seperti menekan tombolnya, atau kita membuat programnya agar object tersebut bisa berinteraksi dengan yang lain

Method yang berada di object terbagi menjadi 2:
1. client -> method interactive (interaksi dengan klien)
2. object interaction (interaksi dengan object yang lain)

Contohnya seperti yang ada di dalam game:
karakter -> bisa kita anggap sebagai object
1. Pergerakan karakter yang kita gunakan ditentukan oleh tombol yang kita pilih (interaksi dengan klien)
2. Interaksi karakter yang kita gunakan dengan karakter di game tersebut seperti menyerang karakter lain (interaksi dengan object yang lain)
'''

class Servant:
    # class variable
    jumlah_servant = 0
    
    def __init__(self, name, hp, atk, armor):
        # instance variable
        self.name = name
        self.health = hp
        self.attack = atk
        self.armor = armor
        Servant.jumlah_servant += 1
    
    # berikutnya adalah method
    # method adalah membuat 'apa yang kita inginkan terjadi pada object tersebut'
    # atau 'apa yang kita ingin object terebut lakukan'
    # bisa dikatakan agar object tersebut bisa berinteraksi atau diinteraksikan

    # cara membuat method hampir sama cara kita membuat function
    # karena method juga dikatakan sebagai 'fungsi di dalam class'
    
    # void function, method tanpa argument dan return
    def siapa(self):
        print("Namaku adalah " + self.name)
        
    # method dengan argument tanpa return
    def health_up(self, up):
        self.health += up
        
    # method dengan return (mengembalikan nilai)
    def getHealth(self):
        return self.health
    
    # maksud dari 'self' di atas adalah object-nya
    # kita juga bisa mengganti kata 'self' dengan kata yang lain tapi dengan fungsi yang serupa
        
servant1 = Servant('Saber', 200, 20, 5) # di dalam kurung adalah input atribut
servant2 = Servant('Archer', 150, 50, 3)

print(servant1.__dict__)
print(servant2.__dict__)

servant1.siapa() # cara menggunakan method di dalam object
servant1.health_up(20) # method ini bisa kita gunakan untuk menambahkan atribut
# <nama object/self>.<method(argument)>
# argument pada method bersifat opsional


print(servant1.health)
print(servant1.getHealth())