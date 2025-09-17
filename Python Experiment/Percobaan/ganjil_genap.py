# Program ini digunakan untuk menentukan apakah angka yang dimasukkan oleh user termasuk ke dalam ganjil atau genap

# angka = int(input("Masukkan sebuah angka: "))

# if angka % 2 == 0:
#     print("Angka tersebut adalah genap")
# else:
#     print("Angka tersebut adalah ganjil")

# Game tebak angka

import random

# Angka acak antara 1 sampai 10
angka_rahasia = random.randint(1, 10)

# Maksimal 3 percobaan
for i in range(3):
    tebak = int(input("Tebak angka (1-10): "))
    
    if tebak == angka_rahasia:
        print("Tebakan kamu benar!")
        break
    else:
        print("Salah tebak!")
    

print(f"Angka yang benar adalah: {angka_rahasia}")
