# Type hint pada fungsi
# atau memberi petunjuk kepada user fungsi dari suatu fungsi yang dibuat

'''
bentuk standar fungis yang sudah dipelajari
def nama_fungsi(parameter):
      print(parameter ** 2)

nama_fungsi(1)
nama_fungsi("rizky")
nama_fungsi(True)


fungsi di atas akan mengalami error karena fungsi tersebut digunakan untuk memangkatkan suatu bilangan, jadi jika dimasukan string seperti contoh di atas akan mengalami error'''

# penggunaan type hints

import string

# fungsi untuk memangkatkan dua suatu bilangan
def pangkat_dua(argumen:int) -> int: # (int sebelah kanan argumen) menandakan bahwa input fungsi tersebut adalah integer, ( -> int ) sebagai pemberitahu bahwa outputnya adalah integer
    '''fungsi dengan hints'''
    hasil = argumen ** 2
    return hasil

print(pangkat_dua(6))

def display(argument:string):
    print(argument)
    
display('Ucup')

