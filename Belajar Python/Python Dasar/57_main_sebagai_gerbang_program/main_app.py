# __main__ adalah top level environment

# __name__ = "__main__" akan terjadi jika ada di file program utama

## __name__ pada file program utama
print(f'nilai __name__ pada main.py = {__name__}')

## __name__ pada file program eksternal
import fungsi

# deklarasi
def fungsi_kali(a:int, b:int)->int:
    '''fungsi kali'''
    return a * b

# fungsi utama
if __name__ == '__main__':
    angka1 = 5
    angka2 = 10
    hasil = fungsi_kali(angka1, angka2)
    print(f'hasil {angka1} kali {angka2} = {hasil}')
    
## import pacakge
import package

## import modul
from package import modul

hasil_tambah = modul.tambah(10, 5)
hasil_kurang = modul.kurang(10, 5)
print(f'hasil tambah = {hasil_tambah}')
print(f'hasil kurang = {hasil_kurang}')
