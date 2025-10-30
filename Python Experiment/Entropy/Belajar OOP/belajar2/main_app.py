
from Models import Hero, Enemy

char_name = input("Masukkan nama untuk karakter kamu: ").capitalize()
print("\nPilih kelas untuk karakter kamu")
print("1. Knight")
print("2. Archer")
print("3. Sorcerer")
char_class = input("Pilihan kamu: ")

match char_class:
    case '1':
        hero1 = Hero.Knight(char_name)
    case '2':
        hero1 = Hero.Archer(char_name)
    case '3':
        hero1 = Hero.Sorcerer(char_name)
        
hero1.showInfo()

print(hero1.getArmor)
tambah = 170
hero1.gainExp = tambah
print(tambah // 100)
print(tambah % 100)
hero1.showInfo()


print("\nSiapa yang ingin kamu lawan?")
print("1. Goblin")
print("2. Skeleton")
print("3. Necromancer")
print("4. Berserker")
enemy_pick = input("Pilihan kamu: ")

# hp_amount = int(input("Masukkan jumlah HP musuh: "))
# atk_amount = int(input("Masukkan jumlah ATK musuh: "))
# def_amount = int(input("Masukkan jumlah DEF musuh: "))

match enemy_pick:
    case '1':
        enemy1 = Enemy.Goblin('Goblin')
    case '2':
        enemy1 = Enemy.Skeleton('Skeleton')
    case '3':
        enemy1 = Enemy.Necromancer('Necromancer')
    case '4':
        enemy1 = Enemy.Berserker('Berserker')

print()
enemy1.showEnemyInfo()
print()
