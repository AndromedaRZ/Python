# latihan membuat game sederhana

'''
Konsep:
Misalnya kita mempunyai 2 servant

setiap servant memiliki attributenya masing-masing

servant1 = nama, health, attack, defense
servant2 = nama, health, attack, defense

berikutnya ada method
seperti servant1 menyerang servant2 dan servant2 yang diserang dan bertahan
begitupun sebaliknya

kita akan buat programnya seperti ini:
ketika servant1 'menyerang' servant2, maka otomatis servant2 akan mengalami yang namanya 'diserang'
jadi method 'diserang' akan aktif secara otomatis ketika servant1 menggunakan method 'menyerang' terhadap servant2

dan nantinya ketika servant2 diserang, status attribute health powernya akan berkurang sebanyak attack power yang dimiliki oleh servant1
'''

class Servant:
    
    # menginisialisasi pembuatan servant
    # __init__ bisa diartikan memberikan attribute ke dalam object yang akan dibuat nantinya
    def __init__(self, name, hp, atk, defence):
        self.name = name
        self.hp = hp
        self.atk = atk
        self.defence = defence
        
    def attack(self, enemy): # karena semua yang ada di python adalah object, kita bisa menjadikannya sebagai parameter/argument
        print(self.name + ' menyerang ' + enemy.name) # objectnya adalah enemy dan 'name' untuk menampilkan namanya
        enemy.attacked(self, self.atk)
        
    def attacked(self, enemy, atk_lawan):
        print(self.name + ' diserang ' + enemy.name)
        atk_value = atk_lawan / self.defence
        print(self.name + ' menerima kerusakan', atk_value)
        self.hp -= atk_value
        print('Hp ' + self.name + ' tersisa', self.hp)
        
        
saber = Servant('Saber', 200, 20, 5)
archer = Servant('Archer', 130, 80, 1)

saber.attack(archer) # masukkan object sebagai argument
# dengan begitu kita bisa membuat object saling berinteraksi satu sama lain dengan method di atas

print()
archer.attack(saber)