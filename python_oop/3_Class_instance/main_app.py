# Class variable dan Instance variable

class Servant():
    # class variable
    jumlah = 0 # variabel ini disebut class variable, dan berbeda dari instance variable
    # artinya variabel tersebut milik si class 'Servant'
    # class variabel juga sering disebut sebagai static variable
    
    
    def __init__(self, name, hp, atk, armor): # argument di dalamnya bisa kita katakan sebagai atribut dari object yang akan dibuat
        # instance variable
        self.name = name
        self.hp = hp
        self.atk = atk
        self.armor = armor
        Servant.jumlah += 1
        print("Membuat Servant dengan nama " + name)
        # ketika kita membuat object baru, maka baris ini akan terus mengulang sebanyak kita membuat objectnya
        
servant1 = Servant('Saber', 200, 20, 5)
print(Servant.jumlah)
servant2 = Servant('Archer', 120, 80, 1)
print(Servant.jumlah)
servant3 = Servant('Lancer', 150, 50, 3)
print(Servant.jumlah)