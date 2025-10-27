# Latihan fungsi

import os

# program menghitung luas dan keliling persegi panjang

# membuat header program
# os.system("clear")

# print(f'\n{'PROGRAM MENGHITUNG LUAS':^40}')
# print(f'{'DAN KELILING PERSEGI PANJANG':^40}')
# print('-'*40)

# mengambil input user
# LEBAR = int(input("Masukan nilai lebar: "))
# PANJANG = int(input("Masukan nilai panjang: "))

# program menghitung luas
# LUAS = PANJANG * LEBAR
# KELILING = 2 * ( PANJANG + LEBAR )

# tampilkan hasilnya
# print(f"Hasil perhitungan LUAS = {LUAS}")
# print(f"Hasil perhitungan KELILING = {KELILING}")

# fungsi header
def header():
    '''fungsi header'''
    os.system("clear")
    print(f'{'PROGRAM MENGHITUNG LUAS':^40}')
    print(f'{'DAN KELILING PERSEGI PANJANG':^40}')
    print('-'*40)

# fungsi mengambil input user
def input_user():
    '''fungsi untuk input user'''
    lebar = int(input("Masukan nilai lebar: "))
    panjang = int(input("Masukan nilai panjang: "))
    
    return lebar, panjang

# fungsi menghitung luas
def hitung_luas(lebar, panjang):
    '''fungsi luas'''
    return lebar * panjang

# fungsi menghitung keliling
def hitung_keliling(lebar, panjang):
    '''fungsi keliling'''
    return 2 * ( lebar + panjang )

# fungsi display
def display(message, value):
    '''fungsi display'''
    print(f"Hasil perhitungan {message} = {value}")
    
# Program utama
while True:
    header()
    
    opsi = input('''1) Luas
2) Keliling
Pilih perhitungan yang ingin dilakukan [1/2]: ''')
    
    LEBAR, PANJANG = input_user()
    
    if opsi == '1':
        LUAS = hitung_luas(LEBAR, PANJANG) 
        display("luas", LUAS)
        
    elif opsi == '2':
        KELILING = hitung_keliling(LEBAR, PANJANG)
        display("keliling", KELILING)
    
    else:
        print("input tidak valid")
        break
    
    isLanjut = input("Apakah masih ingin lanjut? (y/n): ")
    if isLanjut == 'n':
        break
    
print("Program selesai")


