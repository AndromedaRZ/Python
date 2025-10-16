'''
Object Oriented Programming (OOP)

Programming Paradigma (cara berpikir):
1. Structural - Prosedural Programming
Ciri-ciri structural:
- programnya akan dieksekusi secara beruturan dari atas ke bawah

2. Objected - Oriented Programming
Ciri-ciri objected:

'''


class Servant:
    def __init__(self, input_nama, input_attack_power, input_health_power, input_armor):
        self.name = input_nama
        self.attack = input_attack_power
        self.health = input_health_power
        self.armor = input_armor
        

servant1 = Servant("saber", 80, 150, 80)
servant2 = Servant("archer", 100, 100, 50)
servant3 = Servant("assassin", 120, 100, 30)

print(servant1.__dict__) # servant1 setara atau sama dengan dengan 'self'
print(servant2.__dict__)
print(servant3.__dict__)
