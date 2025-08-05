# program kalkulator sederhana menggunakan if, elif, dan else statement

while True:
    print("\n====Kalkulator Sederhana====")
    angka1 = int(float(input("Masukkan angka pertama: ")))
    print("\n1) Penjumlahan (+)")
    print("2) Pengurangan (-)")
    print("3) Perkalian   (*)")
    print("4) Pembagian   (/)")

    operasi = int(input("Pilih operasi yang ingin digunakan [1/2/3/4]: "))
    
    angka2 = int(input("\nMasukkan angka kedua: "))

    if operasi == 1:
        hasil = angka1 + angka2
        print(f"\nHasilnya adalah {hasil}")
    elif operasi == 2:
        hasil = angka1 - angka2
        print(f"\nHasilnya adalah {hasil}")
    elif operasi == 3:
        hasil = angka1 * angka2
        print(f"\nHasilnya adalah {hasil}")
    elif operasi == 4 and angka2 == 0:
        print("Tidak bisa melakukan pembagian dengan angka 0")
    elif operasi == 4:
        hasil = angka1 / angka2
        print(f"\nHasilnya adalah {hasil:.2f}")
    else:
        print("Program dihentikan, ada kesalahan teknis saat penginputan operasi")
    
    pilihan = input("Apakah ingin menghitung lagi? [y/n]: ")
    if pilihan == "n":
        break
    
    while pilihan != "y":
        pilihan = input("Apakah ingin menghitung lagi? [y/n]: ")
        if pilihan == "n":
            print("Prorgam hitungan dihentikan")
            exit()
        
        
print("Prorgam hitungan dihentikan")

# Latihan soal dari chatgpt

# Jawaban soal 1 menentukan bilangan positif atau negatif

print("\n====Cek angka positif atau negatif====")
angka = int(input("Masukkan angka: "))

if angka > 0:
    print("Angka positif")
elif angka < 0:
    print("Angka negatif")
else:
    print("Angka nol")
    
# Jawaban soal 2 penilaian ujian

print("\n====Cek predikat dari nilai ujian====")
angka = int(input("Masukkan nilai ujian anda: "))


if angka < 40:
    print("Predikat anda adalah E")
elif angka >= 40 and angka <= 54:
    print("Predikat anda adalah D")
elif angka >= 55 and angka <= 69:
    print("Predikat anda adalah C")
elif angka >= 70 and angka <= 84:
    print("Predikat anda adalah B")
elif angka >= 85 and angka <= 100:
     print("Predikat anda adalah A")
else:
    print("Silahkan masukkan angka yang tepat")
    
# Jawaban soal 3 menentukan tahun kabisat

print("\n====Menentukan tahun kabisat====")
tahun = int(input("Masukkan tahun yang ingin di cek: "))

if tahun % 4 == 0 and tahun % 100 != 0 or tahun % 400 == 0:
    print(f"Tahun {tahun} adalah tahun kabisat")
else:
    print(f"Tahun {tahun} bukanlah tahun kabisat")
    
# Jawaban soal 4 cek usia dan izin menonton
print("\n====Cek usia dan izin menonton====")

angka = int(input("Masukkan umur anda: "))

if angka < 13:
    print("Tidak boleh menonton")
elif angka >= 13 and angka <= 16:
    print("Boleh menonton dengan pendamping")
else:
    print("Boleh menonton")
    