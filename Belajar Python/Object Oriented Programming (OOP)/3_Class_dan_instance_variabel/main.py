'''
Object Oriented Programming (OOP)

Programming Paradigma (cara berpikir):
1. Structural - Prosedural Programming
Ciri-ciri structural:
- programnya akan dieksekusi secara beruturan dari atas ke bawah

2. Objected - Oriented Programming
Ciri-ciri objected:

'''


class Servant: # template
    # class variabel
    jumlah = 0
     
    
    def __init__(self, input_nama, input_attack_power, input_health_power, input_armor):
        # instance variabel, adalah variabel-variabel milik Servant (servant1, servant2, servant3)
        self.name = input_nama
        self.attack = input_attack_power
        self.health = input_health_power
        self.armor = input_armor
        Servant.jumlah += 1
        print("membuat servant dengan nama " + input_nama)
        

servant1 = Servant("saber", 80, 150, 80)
print(Servant.jumlah)
servant2 = Servant("archer", 100, 100, 50)
print(Servant.jumlah)
servant3 = Servant("assassin", 120, 100, 30)
print(Servant.jumlah)
