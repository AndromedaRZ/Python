
class Servant:
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp
        
    def showInfo(self):
        print(f"Status servant {self.name}\nHealth: {self.hp}")
        
# class Servant_saber(Servant):
#     def __init__(self, name):
#         self.name = name
#         self.hp = 200
# kode untuk servant saber di atas kita buat dengan cara mengulang
# sebenarnya kita bisa menghindari pengulangan tersebut (mencegah agar tidak ada kode dengan fungsi yang sama ditulis ulang)
        
class Servant_saber(Servant):
    def __init__(self, name): # jangan lupa, init akan tereksekusi pada saat pertama kali membuat object
        Servant.__init__(self, name, 200)
        # kita bisa menggunakan cara di atas untuk mencegah pengulangan kode
        # '__init__' di atas berasal dari super class 'Servant'
        # akan tetapi parameter 'self'nya berasal dari sub class 'Servant_saber'
        super().showInfo() # kita bisa melakukan hal yang sama pada method yang lain
        
        Servant.showInfo(self) # kita juga bisa menggunakan cara ini
        

class Servant_archer(Servant): # masukkan 'Servant' sebagai argument agar kita bisa memanggil __init__ dari super class 'Servant' tersebut
    def __init__(self, name):
        # cara kedua yang bisa digunakan untuk mencegah perulangan adalah menggunakan 'super()' yang berarti super class
        # atau method dari super class
        super().__init__(name, 150) # artinya kita memanggil __init__ dari super class yaitu 'Servant'
        # super class yang ingin kita panggil kita jadikan sebagai argument pada saat pembuatan sub class
        super().showInfo()


artoria = Servant_saber('Artoria')
gilgamesh = Servant_archer('Gilgamesh')
    