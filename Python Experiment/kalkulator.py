# program kalkulator sederhana

print("====Kalkulator Sederhana====")
angka1 = int(input("Masukkan angka pertama: "))
angka2 = int(input("Masukkan angka kedua: "))

print("1. Tambah")
print("2. Kurang")
print("3. Kali")
print("4. Bagi")
pilih = int(input("Pilih operasi yang ingin digunakan [1/2/3/4]: "))


if pilih == 1:
    hasil = angka1 + angka2
    print(f"Hasilnya adalah: {hasil}")
elif pilih == 2:
    hasil = angka1 - angka2
    print(f"Hasilnya adalah : {hasil}")
elif pilih == 3:
    hasil = angka1 * angka2
    print(f"Hasilnya adalah: {hasil}")
elif pilih == 4:
    hasil = angka1 / angka2
    print(f"Hasilnya adalah: {hasil}")
else:
    print("Pilihan tidak valid, silahkan mulai ulang programnya")
    