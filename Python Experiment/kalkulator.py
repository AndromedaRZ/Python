# program kalkulator sederhana menggunakan if, elif, dan else statement

while True:
    print("\n====Kalkulator Sederhana====")
    angka1 = int(input("Masukkan angka pertama: "))
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
    elif operasi == 4:
        hasil = angka1 / angka2
        print(f"\nHasilnya adalah {hasil}")
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