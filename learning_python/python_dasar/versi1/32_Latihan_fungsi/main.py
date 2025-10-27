'''latihan fungsi'''

import os

# Program menghitung luas dan persegi panjang

# membuat header program
# os.system("clear")

# print(f"{'PROGRAM MENGHITUNG LUAS':^40}")
# print(f"{'DAN KELILING PERSEGI PANJANG':^40}")
# print(f"{'-'*40}")

# # mengambil input user
# PANJANG = int(input("Masukkan nilai panjang: "))
# LEBAR = int(input("Masukkan nilai lebar: "))

# # program menghitung luas
# LUAS = PANJANG * LEBAR
# KELILING = 2 * (PANJANG + LEBAR)

# # tampilkan hasil
# print(f'Hasil perhitungan luas = {LUAS}^2')
# print(f"Hasil perhitungan keliling = {KELILING}^3")

'''
Program yang dibuat di atas adalah salah satu contoh ketika kita tidak membuatnya menggunakan fungsi.
Berikutnya kita akan membuat program yang sama dengan menggunakan 'fungsi'
'''

# fungsi juga bisa kita artikan sebagai 'def'

def header():
    '''fungsi header'''
    os.system("clear")

    print(f"{'PROGRAM MENGHITUNG LUAS':^40}")
    print(f"{'DAN KELILING PERSEGI PANJANG':^40}")
    print(f"{'-'*40}")

def input_user():
    '''fungsi input user'''
    panjang = int(input("Masukkan nilai panjang: "))
    lebar = int(input("Masukkan nilai lebar: "))
    return panjang, lebar

def hitung_luas(panjang, lebar):
    '''fungsi menghitung luas'''
    return panjang * lebar

def hitung_keliling(panjang, lebar):
    '''fungsi menghitung keliling'''
    return 2 * (panjang + lebar)

def display(message, value):
    '''fungsi display'''
    print(f"Hasil perhitungan {message} = {value}")

# program utama
while True:
    header() # untuk memanggil fungsi header()

    # ketika kita memanggil def input_user(), isinya adalah menampilkan perintah input untuk user dan bisa dilihat pada baris kode
    # di dalam fungsi tersebut dan ketika kita melihat baris kode di bawah ini
    # nantinya masing-masing hasil dari input tersebut akan masuk ke dalam dua constant yang berbeda
    PANJANG, LEBAR = input_user()
    LUAS = hitung_luas(PANJANG, LEBAR) # lalu gunakan constant tadi untuk menjalankan fungsi hitung luas dan keliling
    KELILING = hitung_keliling(PANJANG, LEBAR) # sambil diperhatikan posisi argument di setiap fungsi dan setiap pemanggilan fungsi

    display("Luas", LUAS)
    display("Keliling", KELILING)

    isContinue = input("Apakah lanjut? (y/n): ")
    if isContinue == 'n':
        break

print('Program selesai, terima kasih!')