# getter dan setter

class Servant:
    
    def __init__(self, name, hp, armor):
        # private variable diawali dua garis bawah '__'
        self.name = name
        self.__hp = hp
        self.__armor = armor
        # self.info = 'name {} : \n\thealth: {}'.format(self.__name, self.__hp)
        
    @property # mengubah sebuah method menjadi seperti variable
    def info(self):
        return f'name {self.name} : \n\thealth: {self.__hp}'
    
    
    # @property ini disebut decorator
    @property
    def armor(self):
        pass
    
    @armor.getter
    def armor(self):
        return self.__armor
    
    @armor.setter
    def armor(self, input):
        self.__armor = input
        
    @armor.deleter
    def armor(self):
        print("armor dihapus")
        self.__armor = None
        
    
saber = Servant('saber', 200, 5)

print(saber.info)
# hasil di atas akan tetap sama saja ketika menggunakan property

# print(saber.__dict__)
# ketika kita mencoba print menggunakan __dict__
# maka hasilnya info tadi tidak akan terlihat walaupun menggunakan __dict__

saber.name = 'artoria' # karena variable name tidak bersifat private, jadi kita bisa mengubah nilainya
print(saber.info) # maka hasilnya akan berbeda seperti sebelumnya karena sudah kita ubah

print('getter dan setter untuk __armor:')
print(saber.armor)

saber.armor = 50 # cara mengubah datanya sama seperti cara mengubah nilai pada variabel biasa kalau kita menggunakan cara encapsulasi decorator getter dan setter
# walaupun sebelumnya variable 'name.__armor' bersifat private dan tidak bisa diubah
# dengan menambahkan @property dan decorator lainnya, kita bisa melakukan perubahan pada nilanya
# cara ini adalah hal yang diperbolehkan ketika ingin mengubah nilai pada private variable

print(saber.armor)

print('delete armor')
del saber.armor
print(saber.__dict__)