'''
Apa itu Polymorphism?
- Polymorphism berasal dari bahasa yunani yang berarti "banyak bentuk" (poly = banyak, morph = bentuk)
- Dalam OOP, polymorphism adalah kemampuan objects yang berbeda untuk merespons methods call yang sama dengan cara yang berbeda

Analogi Sederhana Polymorphism
- Bayangkan kita punya remote control universal:
- tombol "PLAY" yang sama bisa:
TV: Mulai memutar channel
DVD Player: Mulai memutar Disc
Speaker: Mulai memutar musik
Game Console: Mulai game
- Satu interface yang sama (tombol PLAY), tapi behaviour atau perilaku berbeda tergantung device-nya

Konsep Dasar Polymorphism
- Method Overriding, subclass bisa override method dari parent class dengan implementasi berbeda
- Duck Typing, "Jika berjalan seperti bebek dan bersuara seperti bebek, maka itu adalah bebek"
- Python tidak peduli tipe object, yang penting object punya method yang dibutuhkan 
'''

class Hewan:
    def __init__(self, name):
        self.name = name
        
    def suara(self):
        print(f"{self.name} bersuara")
        
        
class Anjing(Hewan):
    def suara(self): # override method
        print(f"{self.name} guk! guk!")
        
class Kucing(Hewan):
    def suara(self): # override method
        print(f"{self.name} meow meow")
        
class Sapi(Hewan):
    def suara(self): # override method
        print(f"{self.name} moo! moo!")

hewan_list = [
    Anjing("Anjing"),
    Kucing("Kucing"),
    Sapi("Sapi")
]

for hewan in hewan_list:
    hewan.suara() # menggunakan method yang sama tetapi beda fungsi setiap classnya


class Mobil:
    def start(self):
        return "mesin mobil menyala"
    
class Motor:
    def start(self):
        return "mesin motor menyala"
    
class Pesawat:
    def start(self):
        return "mesin pesawat menyala"
    
# function yang polymorphic
def operasikan_kendaraan(kendaraan):
    print(kendaraan.start()) # apapun objectnya jika memiliki method start maka akan tetap dijalankan 


# polymorphism dengan duck typing
kendaraan_list = [
    Mobil(),
    Motor(),
    Pesawat()
]

for kendaraan in kendaraan_list:
    operasikan_kendaraan(kendaraan)
    
'''
Operator Overloading
- Python memungkinkan kita override operators (+,-,*,==,dll) dengan magic methods, jadi kita bisa menggunakan methods di bawah ini untuk menggunakan operator
__add__ untuk +
__sub__ untuk -
__mul__ untuk *
__eq__ untuk ==
__lt__ untuk <
__le__ untuk <=
__gt__ untuk >
__ge__ untuk >=
__ne__ untuk !=
'''