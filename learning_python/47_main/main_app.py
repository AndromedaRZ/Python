# __main__

# __main__ adalah top level code environment

# __name__ = "__main__"
# '__main__' hanya akan muncul pada program utama atau pada file kita menjalankan program terebut
# ketika __name__ berada di dalam file lain (file eksternal) dan kita mengimport file tersebut
# maka yang akan muncul bukanlah '__main__', melainkan nama dari file yang kita import tersebut


## __name__ pada file program utama
print(f"nilai __name__ pada main_app.py = '{__name__}'")

## __name__ pada file program eksternal
import fungsi

# lalu apa gunanya dari __main__ ini?

# contoh penggunaan __main__

# deklarasi
def fungsi_tambah(a: int, b:int) -> int:
    return a + b

# fungsi utama
if __name__ == '__main__':
    angka1 = 5
    angka2 = 10
    hasil = fungsi_tambah(angka1, angka2)
    print(f'hasil tambah = {hasil}')
    
## import package
import package