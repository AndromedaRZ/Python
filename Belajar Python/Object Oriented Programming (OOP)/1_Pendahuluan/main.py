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
    pass


servant1 = Servant() # object / instance (instansiate)
servant2 = Servant()
servant3 = Servant()

servant1.name = 'saber' # menaruh atribut nama
servant1.health = 100 # menaruh atribut health

servant2.name = 'archer'
servant2.health = 200

servant3.name = 'assassin'
servant3.health = 150

print(servant1)
print(servant1.__dict__) # melihat atribut apa saja yang ada di dalam object
print(servant1.name) # mengkases salah satu atribut dari object (atribut nama)
