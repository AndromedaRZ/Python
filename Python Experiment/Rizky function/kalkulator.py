# program kalkulator menggunakan function

while True:
    def aritmatika(**matematika):
        angka1 = matematika["angka1"]
        operasi = matematika["operasi"]
        angka2 = matematika["angka2"]
        
        if operasi == 1:
            return angka1 + angka2
        elif operasi == 2:
            return angka1 - angka2
        elif operasi == 3:
            return angka1 * angka2
        elif operasi == 4:
            return angka1 / angka2
            
    print('\n=== Program kalkulator menggunakan function ===')
    angka1 = float(input("Masukan angka pertama: "))
    print('''Operasi
1) Tambah (+)
2) Kurang (-)
3) Kali (*)
4) Bagi (/)''')
    operasi = int(input("Pilih operasi yang digunakan [1/4]: "))
    angka2 = float(input("Masukan angka kedua: "))
    if operasi == 4 and angka2 < 1:
        print(f'Angka tersebut tidak bisa dibagi!')
    elif operasi > 4:
        print("Masukan operasi yang valid!")
    else:
        hasil = aritmatika(angka1 = angka1, operasi = operasi, angka2 = angka2)
        print(f"Hasilnya adalah = {hasil}")
    
    konfirmasi = input("Ingin lanjut menghitung? [y/n]: ").lower()
    if konfirmasi == "y":
        continue
    else:
        break
