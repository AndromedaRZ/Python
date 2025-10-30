class Character:
    
    def __init__(self, name, role):
        self.__name = name
        self.hp_pool = [0,100,200,300,400,500]
        self.atk_pool = [0,10,20,30,40,50]
        self.armor_pool = [0,1,2,3,4,5]
        self.__exp = 0
        self.__level = 0
        self.__role = role
        self.__currentHp = 0
        
        
        
# getter
    def showInfo(self):
        print(f"{self.__name}")
        print(f"   Level {self.__level}")
        print(f"   Class {self.__role}")
        print(f"   HP  : {self.__currentHp}/{self.__maxHp}")
        print(f"   ATK : {self.__atk}")
        print(f"   DEF : {self.__armor}")
 
    def showEnemyInfo(self):
        print(f"{self.__name}")
        print(f"   HP  : {self.__currentHp}/{self.__maxHp}")
        print(f"   ATK : {self.__atk}")
        print(f"   DEF : {self.__armor}")


    def take_damage(self, amount):
        damage = amount / self.__armor
        if damage < 0:
            damage = 0
        self.__currentHp -= damage
        if self.__currentHp < 0:
            self.__currentHp = 0
        print(f"{self.__name} menerima {damage} damage! (HP: {self.__currentHp}/{self.__maxHp})")
        return damage

    def attack(self, target):
        print(f"{self.__name} menyerang {target.__name}!")
        return target.take_damage(self.__atk)

    @property
    def getName(self):
        pass
    
    @getName.getter
    def getName(self):
        return self.__name
        

# --------------------------------------------------------------
    # @property
    # def currentHp(self):
    #     pass
        
    # @currentHp.setter
    # def currentHp(self, input):
    #     self.currentHp = input
        


# --------------------------------------------------------------
    # dengan menggunakan decorator (property) seperti ini, kita bisa menggunakan getter dan setter
    # untuk Hero
    @property
    def hp_pool(self):
        pass
    
    @hp_pool.setter # sifatnya diubah menjadi seperti variabel
    def hp_pool(self, input):
        self.__hp_pool = input
    
    # untuk Enemy

# --------------------------------------------------------------  
    # untuk Hero
    @property
    def atk_pool(self):
        pass
    
    @atk_pool.setter
    def atk_pool(self, input):
        self.__atk_pool = input

# --------------------------------------------------------------
    # untuk Hero
    @property
    def armor_pool(self):
        pass
    
    @armor_pool.setter
    def armor_pool(self, input):
        self.__armor_pool = input
    
    @armor_pool.getter
    def getArmor(self):
        return self.__armor_pool
# --------------------------------------------------------------
    # untuk Hero
    @property
    def gainExp(self):
        pass
    
    @gainExp.setter
    def gainExp(self, input):
        self.__exp += input
        if self.__exp >= 100:
            self.levelUp = self.__exp // 100 # dibagi dan dibulatkan ke bawah
            self.__exp %= 100
            
# --------------------------------------------------------------
    # untuk Hero
    @property
    def levelUp(self):
        pass
        
    @levelUp.setter
    def levelUp(self, input):
        self.__level += input
        self.__maxHp = self.__hp_pool[self.__level]
        self.__currentHp = self.__maxHp
        self.__atk = self.__atk_pool[self.__level]
        self.__armor = self.__armor_pool[self.__level]
        
# --------------------------------------------------------------