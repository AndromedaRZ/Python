class Servant:
    
    def __init__(self, inputName, inputHealth, inputAttack, inputArmor): # init artinya initialization
        # print("Halo", x) # baris ini akan tereksekusi ketika kita baru pertama kali membuat sebuah object
        # self ini juga berguna untuk kita menambahkan sebuah argument ke dalamnya
        self.name = inputName
        self.health = inputHealth
        self.attack = inputAttack
        self.armor = inputArmor
        # __init__ juga akan otomatis terpanggil ketika class 'Servant' digunakan untuk membuat object baru
        
servant1 = Servant('Saber', 200, 20, 5)
# servant1 == self
# servant1 masuk ke dalam fungsi __init__ sebagai input argument 'self'
servant2 = Servant('Lancer', 150, 50, 3)
servant3 = Servant('Ucup', 1000, 100, 0)

print(servant1.name) # untuk menampilan atribut spesifik
print(servant2.health) # atribut spesifik yang ingin diambil bisa dilihat pada pembuatan instance variabel di dalam class Servant
print(servant3.armor)

print(servant1.__dict__) # dengan menggunakan __dict__, kita bisa melihat semua atribut dari servant1 sebagai dictionary
print(servant2.__dict__)
print(servant3.__dict__)
print(servant1.name, servant1.health)


class Person:
    
    def __init__(self, name, age): # ini disebut __init__() method
        self.name = name
        self.age = age
        

person1 = Person('ricky', 19)
print(person1) # ketika kita hanya memanggil dengan cara seperti ini
# maka outputnya akan menunjukkan bahwa itu adalah object

print(person1.name) # dengan menambahkan argument menggunakan titik
# kita bisa membuatnya menampilkan nilai yang kita inginkan
print(person1.age)
