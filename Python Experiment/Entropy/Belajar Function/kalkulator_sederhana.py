def kalkulator(**kwargs):
    angka1 = kwargs['angka1']
    option = kwargs['option']
    angka2 = kwargs['angka2']
    
    if option == '1':
        return angka1 * angka2
    elif option == '2':
        if angka2 == 0:
            return "\nTidak bisa membagi angka dengan 0!"
        else:
            return angka1 / angka2
    elif option == '3':
        return angka1 + angka2
    elif option == '4':
        return  angka1 - angka2
    else:
        return "\nMasukkan operasi yang benar!"
    
while True:
    angka1 = float(input("\nMasukkan angka pertama: "))
    print("""Operasi
1) Kali (*)
2) Bagi (/)
3) Tambah (+)
4) Kurang (-)""")
    option = input("Masukkan operasi yang diinginkan [1-4]: ")
    angka2 = float(input("Masukkan angka kedua: "))
    option = int(option)
    if option > 4:
        print("\nMasukkan operasi yang benar!")
    elif angka2 == 0 and option == '2':
        print("\nTidak bisa membagi angka dengan 0!")
    else:
        option = str(option)
        print(f"\nHasilnya adalah = {kalkulator(angka1 = angka1, option = option, angka2 = angka2)}")

    konfirmasi = input("Apakah masih ingin berhitung? (y/n): ").lower()
    if konfirmasi == 'y':
        continue
    else:
        print("Program selesai")
        break
    