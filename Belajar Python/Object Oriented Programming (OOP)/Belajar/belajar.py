class Character:
    
    def __init__(self, name, health, energy):
        self.name = name
        self.health = health
        self.energy = energy
        print("player created")
    
    def attack(self):
        print(f"{self} attack")
        
aisa = Character("Aisa", 100, 50)
    
    