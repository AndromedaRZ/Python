'''
Programming paradigma -> Cara berpikir
---------------------
- Struktural -> Prosedural Programming
- Object-Oriented Programming

Apa ciri-cirinya?
- Prosedural diekseksui secara berurutan (perbaris)

OOP bisa memudahkan kita membuat kode program tanpa perlu mengkhawatirkan kondisi

objet-oriented artinya semuanya dianggap sebagai Object
dan di antara semua object tersebut bisa saling berinteraksi satu sama lain

OOP ini digunakan menggunakan template yang biasa kita sebut sebagai 'class'

contoh:
```
class Hero:
```

kita ibaratkan sedang membuat game

Karena Hero adalah template maka ia memiliki 2 buah nilai
1. Atribut -> misal nama, attack, defense, armor
2. Method -> Hal yang bisa dilakukan oleh Hero tersebut
    - menyerang()
    - bertahan()
    - bergerak()
    
contoh lainnya seperti ini:
Sebuah meja kita sebut 'Atribut' dan apapun yang kita lakukan terhadap meja tersebut entah itu membaliknya, menggesernya, maupun memindahkannya disebut 'Method'

Object akan mengambil semua kemungkinan dari Atribut dan Method yang kita buat
'''

class Servant: # templatenya
    pass


servant1 = Servant() # object/instance atau prosesnya
servant2 = Servant()
servant3 = Servant()

# misalnya ketika kita ingin memberi nama kepada hero tersebut
servant1.name = 'saber'
servant1.health = 200

servant2.name = 'lancer'
servant2.health = 150

servant3.name = 'ucup'
servant3.health = 1000

print(servant1.__dict__) # dengan menggunakan dict seperti ini
# kita bisa melihat data dari servant1

print(servant1) # hasilnya adalah si servant1 ini adalah object dari template Servant()
# dan maksud dari angka 0x00.... adalah memory address

print(servant1.name) # jika ingin mengakses datanya secara langsung

