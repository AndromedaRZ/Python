# Meng-override sebuah method

class Servant:
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp
        
    def showInfo(self, tipe):
        print("Ini adalah showInfo di dalam super class 'Servant' tanpa override method")
        print(f"{self.name} HP: {self.hp}")
        
class Servant_saber(Servant):
    def __init__(self, name):
        super().__init__(name, 200)
        
    def showInfo(self):
        super().showInfo('Saber')
        # jika kita menggunakan cara ini, maka outputnya akan sama seperti showInfo yang ada pada __init__ di dalam super class
        
        
class Servant_archer(Servant):
    def __init__(self, name):
        super().__init__(name, 150)
        
    def showInfo(self):
        print("\nIni adalah showInfo di dalam sub class 'Servant_archer' yang akan meng-override method")
        print(f"{self.name}\n\tServant class: Archer\n\tHP: {self.hp}")
        # kita juga bisa membuat method yang hampir sama, nantinya showInfo yang ini akan tereksekusi dan menimpa showInfo yang ada pada __init__ di dalam super class
        # pada saat kita baru pertama kali membuat object 'Servant_archer' ini
        # bisa diartikan kita menimpa fungsi atau method yang ada di super class (override)
        
        
artoria = Servant_saber('Artoria')
gilgamesh = Servant_archer('Gilgamesh')

artoria.showInfo()
gilgamesh.showInfo()