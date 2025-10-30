class Servant:
    
    def __init__(self, name):
        # kali ini kita membuat semacam pool leveling
        self.hp_pool = [0,100,200,300,400,500]
        self.atk_pool = [0,10,20,30,40,50]
        self.armor_pool = [0,1,2,3,4,5]
        self.__name = name
        self.__exp = 0
        self.__level = 0
        
    def showInfo(self):
        print(f"{self.__name}")
        print(f"\tLevel {self.__level}")
        print(f"\tHP  : {self.__hp}")
        print(f"\tATK : {self.__atk}")
        print(f"\tDEF : {self.__armor}")
        
    
    # setter
    @property # decorator ini berguna agar kita bisa men-setting attribute yang ada di bawahnya
    def hp_pool(self):
        pass
    
    @property
    def atk_pool(self):
        pass
    
    @property
    def armor_pool(self):
        pass
    
    @property
    def levelUp(self):
        pass
    
    @property
    def gainExp(self):
        pass
    
    @hp_pool.setter # dengan menambahkan decorator @property, kita bisa membuat setter pada attribute tersebut agar bisa mengubah nilainya
    def hp_pool(self, input):
        self.__hp_pool = input
        
    @atk_pool.setter
    def atk_pool(self, input):
        self.__atk_pool = input
        
    @armor_pool.setter
    def armor_pool(self, input):
        self.__armor_pool = input
        
    @gainExp.setter
    def gainExp(self, input):
        self.__exp += input
        if self.__exp >= 100:
            self.levelUp = self.__exp // 100 # dibagi dan dibulatkan ke bawah
            self.__exp %= 100
            
    @levelUp.setter
    def levelUp(self, input):
        self.__level += input
        self.__hp = self.__hp_pool[self.__level]
        self.__atk = self.__atk_pool[self.__level]
        self.__armor = self.__armor_pool[self.__level]

class ServantSaber(Servant):
    
    def __init__(self, name):
        super().__init__(name) # mengambil __init__ dari super class Servant agar settingannya menjadi sama semua
        # sehingga kita juga bisa menyetting attribute dengan ketentuan yang sudah diatur di super class Servant tadi (yang menggunakan property dan setter tadi)
        self.hp_pool = [0,200,300,400,500,600]
        self.atk_pool = [0,20,30,40,50,60]
        self.armor_pool = [0,2,4,6,8,10]
        self.levelUp = 1
               
class ServantArcher(Servant):
    
    def __init__(self, name):
        super().__init__(name)
        # method ini berguna agar kita bisa meng-override method yang ada pada super class Servant
        self.hp_pool = [0,150,200,250,300,350]
        self.atk_pool = [0,50,80,110,140,170]
        self.armor_pool = [0,1,2,3,4,5]
        self.levelUp = 1
        
class ServantLancer(Servant):
    
    def __init__(self, name):
        super().__init__(name)
        self.hp_pool = [0,180,250,320,390,460]
        self.atk_pool = [0,30,50,70,90,110]
        self.armor_pool = [0,2,3.5,5,6.5,8]
        self.levelUp = 1