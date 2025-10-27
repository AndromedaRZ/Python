# multiple inheritance

class A:
    
    def method_A(self):
        print("Ini adalah method A")

class Sesuatu(A):
    pass

class B:
    
    def method_B(self):
        print("Ini adalah method B")

# kita akan mencoba membuat sub class yang meng-inheritance banyak super class
class Sesuatu_multiple(A, B):
    pass


objek = Sesuatu() # walaupun object ini hanya memanggil sub class Sesuatu
objek.method_A() # ia tetap bisa menggunakan method yang ada pada super class A, karena inheritnya berasal dari super class A

objek_2 = Sesuatu_multiple() # kita tinggal menggunakan sub classnya dan menjadikannya object
objek_2.method_A() # kemudian kita bisa menjalankan method yang ada di super class A maupun super class B
objek_2.method_B()

# kalau begitu, apa kegunaan dari multiple inheritance ini?
# bisa dilihat baris kode di bawah

class Team():
    def setTeam(self, team):
        self.team = team
        
    def showTeam(self):
        print(self.team)

class Class_Servant:
    def setTipe(self, tipe):
        self.tipe = tipe

    def showTipe(self):
        print(self.tipe)

class Servant(Team, Class_Servant):
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp
               
ucup = Servant('Ucup', 100)
ucup.setTeam('merah')
ucup.setTipe('Saber')
# dengan membuat program seperti contoh di atas
# penjelasananya yakni class 'Servant' adalah sebuah sub class dan meng-inherit dari super class 'Team' dan 'Class_Servant'
# sehingga kita bisa menggunakan method yang ada di dalam super class 'Team' dan juga 'Class_Servant'

ucup.showTeam()
ucup.showTipe()