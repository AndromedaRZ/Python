# error
# syntax error akan terjadi ketika program yang dijalankan menjadi error
# karena penulisan yang salah pada kode program maupun perintahnya
# sedangkan runtime error akan terjadi ketika program yang kita tulis itu benar/berfungsi
# namun akan menjadi error ketika syarat perintah tersebut tidak terpenuhi
# contohnya ketika kita membuat program pembagian dengan angka 0, maka hasinya akan menjadi runtime error

# exception akan terjadi saat program mengalami error saat runtime
# contoh sederhana untuk menangkap exception
from math import nan

## contoh sederhana
# input_user = int(input("Masukkan angka: "))
# hasil = nan

# # gunakan 'try' dan 'except' secara berpasangan
# try:
#     hasil = 10 / input_user # ketika perintah di baris try bisa berjalan, maka try akan mengeksekusinya
# except:
#     print("Input tidak boleh 0") # akan tetapi ketika perintah di baris try mengalami runtime error, maka except akan tereksekusi
    
# print(f"hasil = {hasil}")

## contoh di aplikasi

while(True):
    angka = int(input("Masukkan angka pembagi: "))
    try:
        hasil = 10 / angka # ketika baris ini terjadi runtime error karena membagi angka 0, maka sistem akan langsung mengeksekusi 'except'
        print(f'Hasil = {hasil}') # jadi, perintah pada baris di bawahnya tidak akan tereksekusi
        isDone = input("Lanjutkan? [Y/n] ").lower()
        if isDone == 'n':
            break
    except:
        print("Pembagi nol, silahkan masukkan input lagi")
        
print('Akhir dari program')

# contoh aplikasi untuk membuat data_tes.txt

try:
    with open("data_tes.txt", 'r') as file:
        print(file.read())
except:
    print("file data_tes.txt tidak ditemukan, membuat file baru") # sama halnya seperti contoh di atas
    with open("data_tes.txt", 'w', encoding='utf-8') as file: # baris except akan langsung tereksekusi ketika 'try' mengalami runtime error
        file.write("file baru") # akan tetapi ketika filenya sudah dibuat pada baris 'except'
        # maka sistem akan mengeksekusi 'try' karena syaratnya sudah terpenuhi dan tidak mengalami runtime error
            
print("Akhir dari program 2")