import random


class Character():
    
    # atribut dasar karakter
    def __init__(self, name, health, attackPower):
        self.name = name
        self.health = health
        self.maxHealth = health
        self.attackPower = attackPower
    
    # method untuk menyerang karakter lain
    def attack(self, lawan):
        attack_min = self.attackPower // 2
        damage = random.randint(attack_min, self.attackPower) # minimum damage yang dapat dihasilkan adalah attack karakter tersebut dibagi 2
        lawan.health -= damage
        if lawan.health < 0:
            lawan.health = 0
        print(f"\n{self.name} menyerang {lawan.name} dan memberikan {damage} damage\nsisa health {lawan.name} : {lawan.health}")
        
    # method untuk memastikan suatu karakter masih hidup
    def alive(self):
        return self.health > 0 # bernilai true jika health karakter lebih dari 0 (masih hidup)
    
    
class Player(Character):
    def __init__(self, name, health, attackPower):
        super().__init__( name, health, attackPower)
        
        mana = 30
        self.mana = mana
    
    # method untuk menyerang menggunakan keahlian khusus (skill)
    def use_skill(self, lawan):
        if self.mana < 10:
            print(f"\n{self.name} kehabisan mana dan tidak bisa menggunakan skill")
            return
        
        while True:
            print("\nPilih skill yang ingin digunakan")
            print("1. Serangan khusus")
            print("2. Sembuhkan diri")
            skill_action = input("Pilih skill [1-2]: ")
            
            if skill_action == '1':
                skill_name = "Serangan khusus"
                damage = self.attackPower * 2
                
                lawan.health -= damage
                self.mana -= 10
                print(f"\n{self.name} menggunakan skill {skill_name} dan memberikan {damage} damage!")
                return f"Mana tersisa: {self.mana}"
                
            elif skill_action == '2':
                skill_name = "Sembuhkan diri"
                heal_amount = 20
                self.mana -= 10
                self.health += heal_amount
                if self.health > self.maxHealth:
                    self.health = self.maxHealth
                
                print(f"\n{self.name} menyembuhkan diri sebanyak {heal_amount} health")
                return
            
            else:
                print("Input tidak valid")
                continue
        
        
        
        
        
class Enemy(Character):
    def __init__(self, name, health, attackPower):
        super().__init__(name, health, attackPower)           

        mana = 30
        self.mana = mana
        
    def enemy_heal(self):
        if self.mana < 10:
            print(f"\n{self.name} kehabisan mana dan tidak bisa menggunakan skill")
            return
        
        heal_amount = 20
        self.mana -= 10
        self.health += heal_amount
        if self.health > self.maxHealth:
            self.health = self.maxHealth
        print(f"\n{self.name} menyembuhkan diri sebanyak {heal_amount} health")
        
    def auto_attack(self, player):
        '''Musuh menyerang otomatis'''
        if self.alive():
            choice = random.randint(1,5)
            if choice == 1:
                self.enemy_heal()
            else:
                self.attack(player)
                

# fungsi untuk memulai pertarungan
def battle(player, enemy):

    print("========= PERTEMPURAN DIMULAI =========")
    
    
    while player.alive() and enemy.alive():
        
        print(f"\n{player.name} HP: {player.health} Mana: {player.mana} | {enemy.name} HP:{enemy.health} Mana: {enemy.mana}")
        print("--------------------------------------")
        print("1. Serang")
        print("2. Skill")
        action = input("Pilih aksi [1-2]: ")
        
        if action == '1':
            player.attack(enemy)
        elif action == '2':
            player.use_skill(enemy)
        else:
            print("Pilihan tidak valid!")
            continue
        
        if not enemy.alive():
            print(f"\n{enemy.name} berhasil dikalahkan, kamu menang!")
            break
        
        enemy.auto_attack(player)
        
        if not player.alive():
            print(f"\n{player.name} kalah, game over!")
            break
        
player = Player('knight', 100, 10)
bandit = Enemy('bandit', 100, 10)
        
battle(player, bandit)        
        
    