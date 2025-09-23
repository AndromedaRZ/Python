# Program konversi satuan (berat, suhu, panjang) menggunakan function

import os, suhu, berat
os.system("clear")

title = "│ PROGRAM KONVERSI SATUAN │"
print(f"┌{'─'*(len(title) - 2)}┐")
print(title)
print(f"└{'─'*(len(title) - 2)}┘")

while True:
    print()
    print("==== JENIS KONVERSI SATUAN ====")
    print('''1. Konversi Suhu
2. Konversi Berat
3. Konversi Panjang
4. Keluar''')
    choice = input("Pilih konversi satuan [1-3]: ")
    
# ================================================================================================================================
# Jika user memilih konversi satuan suhu    
    if choice == '1':
        print("\n=== Pilih satuan suhu yang ingin dikonversikan ===")
        print('''1. Celius
2. Fahrenheit
3. Reamur
4. Kelvin''')
        choice2 = input("Pilih [1-4]: ")
        if choice2 == '1':
            suhu.celcius_conv()
        elif choice2 == '2':
            suhu.fahrenheit_conv()
        elif choice2 == '3':
            suhu.reamur_conv()
        elif choice2 == '4':
            suhu.kelvin_conv()
    
# ================================================================================================================================
# Jika user memilih konversi satuan berat
    if choice == '2':
        berat_awal = berat.berat_awal()
        berat_akhir = berat.berat_akhir(berat_awal)
        berat.berat_conv(berat_awal, berat_akhir)
    
# ================================================================================================================================
# Jika user memilih konversi satuan panjang   
    if choice == '3':
        continue
    
# ================================================================================================================================
# Jika user memilih untuk keluar program
    if choice == '4':
        break
    
print('Program Berhenti')