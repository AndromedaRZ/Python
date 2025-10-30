# inheritance
# atau dalam bahasa indonesia artinya pewarisan
# sesuatu yang diwariskan/diturunkan

'''
Misalnya ketika kita membuat program seperti ini:

class1 -> disebut sebagai super class
class2 -> disebut sebagai sub class

Contoh 1:

Kita mempunyai super class yaitu Servant

lalu kita membuat lagi class lain yang akan dijadikan sub class
seperti Saber, Lancer, Archer, Berseker, Assassin, Caster

sub class mewariskan sesuatu yang dimiliki oleh super class

Contoh 2:
Kita mempunyai class Tombol sebagai super class
lalu sub classnya ada Tombol transparan, tombol solid, tombol touch

Fungsi simpel dari inheritance adalah agar kita bisa menghindari pengulangan
'''

class Servant: # super class
    
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp
        
        
class Servant_saber(Servant): # masukkan super class di dalam kurung sehingga membuatnya menjadi parameter pada saat kita membuat sub class
    # dengan begitu sifat dari 'Servant_saber' akan menjadi sama seperti super class-nya yaitu Servant
    pass

class Servant_archer(Servant): # sub class
    pass

class Servant_lancer(Servant): # sub class
    pass

class Servant_rider(Servant): # sub class
    pass

class Servant_assasssin(Servant): # sub class
    pass

class Servant_berserker(Servant): # sub class
    pass

# 'Servant_saber' dan 'Servant_archer' adalah sub class
# kedua sub class tersebut adalah inheritance dari super class yang bernama 'Servant'

# misalnya kita membuat kodenya seperti ini
# akan tetapi kita ingin membuat Artoria menjadi Servant Saber
artoria = Servant('Artoria', 200)
arthur = Servant_saber('Arthur', 180)
# jadi, arthur adalah Servant_saber yang mendapatkan warisan dari Servant
# dia juga mempunyai variable yang sama seperti Servant

gilgamesh = Servant_archer('Gilgamesh', 150)
lancelot = Servant_berserker('Lancelot', 200)


print(artoria.name)

print(arthur.name)

print(gilgamesh.name)
print(lancelot.__dict__)