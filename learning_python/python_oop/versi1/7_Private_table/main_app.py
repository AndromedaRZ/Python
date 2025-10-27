# private variable

# artinya sebuah variable yang tidak bisa kita akses
# private variable terletak di object yang private
# biasanya private variable diperlukan untuk encapsulapsi

class Servant:
    
    # class variable
    jumlah = 0
    
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp
        
        # variable instance private
        self.__private = 'private'
        
        # variable instance protected
        self._protected = 'protected'
        
        # private dan protected variable disarankan hanya digunakan di dalam classnya saja
        # tidak disarankan untuk mengubah nilainya

archer = Servant('archer', 130)

print(archer.__dict__) # semua variabel pada output ini bersifat public dan bisa kita akses
# private dan protected variable akan sedikit terlihat ketika kita print sebuah objectnya menggunakan '__dict__'

# print(archer.__private) -> kode error
# tapi akan menjadi error ketika kita ingin mengaksesnya secara langsung

print(archer.__dict__)

print(archer._protected) # untuk protected variable kita bisa mengaksesnya secara langsung
