class Hero:
    
    def __init__ (self, name, health, attack, defense):
        self.name = name
        self.__health = health
        self.__attack = attack
        self.__defense = defense
        # self.info = "name {} :\n\thealth: {} \n\tattack: {}".format(self.__name, self.__health, self.__attack)
    
    # encapsulasi biasa
    def getHealth(self):
        return self.__health
    
    # decorator properti, mengubah method menjadi variabel
    @property
    def info(self):
        # return self.__into
        return "name {} :\n\thealth: {} \n\tattack: {}".format(self.name, self.__health, self.__attack)
    
    @property
    def defense(self):
        pass

    @defense.getter
    def defense(self):
        return self.__defense
    
    @defense.setter
    def defense(self, input):
        self.__defense = input
    
    @defense.deleter
    def defense(self):
        print("defense didelete")
        self.__defense = None
    
knight = Hero('knight', 100, 10, 5)

print("merubah info")
print(knight.info)
knight.name = 'guardian'
print(knight.info)

print("\ngetter dan setter untuk __defense") 
print(knight.defense)       
print(knight.__dict__)

knight.defense = 20
print(knight.defense)       
print(knight.__dict__)

print("\ndelete defense")
del knight.defense
print(knight.__dict__)