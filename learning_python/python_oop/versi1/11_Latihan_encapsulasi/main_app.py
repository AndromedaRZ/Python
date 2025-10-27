# python encapsulasi
'''
sekedar informasi
ncapsulasi berasal dari kata capsule (kapsul)

pada pembelajaran sebelumnya kita sudah membuat program sederhana
permainan saling serang menyerang antara Servant

untuk proyek berikutnya kita akan menambahkan fitur yang namanya 'experience'

pada object servant yang kita buat sebelumnya terdapat yang namanya attribute
seperti health, attack, dan armor dengan nilainya masing-masing
kita akan membuat nilai dari attribute tersebut akan bertambah
sesuai dengan 'experience' atau kenaikan level dari karakter di dalam permainan tersebut

kita akan membuat player tidak bisa melihat 'experience-nya' akan tetapi masih bisa melihat attribute yang lain seperti level, hp, atk, dan armor
'''


class Servant:
    
    # private class variable
    __jumlah = 0
    
    def __init__(self, name, hp, atk, armor):
        self.__name = name
        # ketika kita membuat sistem kenaikan stat melalui level
        # maka attribute yang ingin bisa dinaikkan statnya harus mempunyai nilai awal
        self.__hpStandard = hp
        self.__atkStandard = atk
        self.__armorStandard = armor
        self.__level = 1
        self.__exp = 0
        
        # atur nilai dari maximum attribute terlebih dahulu
        self.__hpMax = self.__hpStandard * self.__level
        self.__atk = self.__atkStandard * self.__level
        self.__armor = self.__armorStandard * self.__level
        
        # atur nilai dari current attribute
        self.__hp = self.__hpMax
        
        Servant.__jumlah += 1
        
        
    @property
    def info(self):
        return "{} level {}: \n\thealth = {}/{}\n\tattack = {}\n\tarmor  = {}".format(self.__name, self.__level, self.__hp, self.__hpMax, self.__atk, self.__armor)
    
    @property
    # setter untuk mengambil experience
    def gainExp(self):
        pass
    
    @gainExp.setter
    def gainExp(self, addExp):
        self.__exp += addExp
        if self.__exp >= 100:
            print(self.__name, 'level up!')
            self.__level += 1
            self.__exp -= 100
            
            # nantinya nilai maximum dari attributenya akan bertambah
            self.__hpMax = self.__hpStandard * self.__level
            self.__atk = self.__atkStandard * self.__level
            self.__armor = self.__armorStandard * self.__level
    
    def attack(self, enemy):
        self.gainExp = 50
        
    
assassin = Servant('Assassin', 130, 50, 2)
saber = Servant('Saber', 200, 20, 5)
print(assassin.info)
# print(assassin.__dict__)


assassin.attack(saber)
assassin.attack(saber)
assassin.attack(saber)
# print(assassin.__dict__)
# ketika kita mengecek stat-nya menggunakan __dict__
# maka hasilnya nilai exp-nya akan bertambah sesuai method yang kita atur
print(assassin.info)

