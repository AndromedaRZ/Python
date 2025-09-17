# Program to-do-list

print("===Program To Do List===")

list_tugas = []

while True:
    print("""\nApa yang ingin anda lakukan hari ini?
1) Tambah tugas
2) Lihat daftar tugas
3) Hapus tugas
4) Keluar program""")
    choice = int(input("Pilihan anda [1/2/3/4]: "))

    if choice == 1:
        tambah_tugas = input("Silahkan tulis tugas yang ingin dimasukkan: ")
        list_tugas.append(tambah_tugas)
        
    elif choice == 2:
        if len(list_tugas) == 0:
            print("\nBelum ada tugas yang ditambahkan")
        else:
            title_tugas = "=====Daftar tugas====="
            print("")
            print(title_tugas)
            for i, tugas in enumerate(list_tugas):
                print(f"{i+1}. {tugas}")
            print("="*(len(title_tugas)))
    
    elif choice == 3:
        if len(list_tugas) == 0:
            print("\nBelum ada tugas yang ditambahkan")
        else:
            title_tugas = "=====Daftar tugas====="
            print("")
            print(title_tugas)
            for i, tugas in enumerate(list_tugas):
                print(f"{i+1}. {tugas}")
            print("="*(len(title_tugas)))

            try:
                delete = int(input("Masukkan nomor tugas yang ingin dihapus: "))
                if 1 <= delete <= len(list_tugas):
                    tugas_dihapus = list_tugas.pop(delete - 1)
                    print(f"Tugas '{tugas_dihapus}' berhasil dihapus.")
                else:
                    print("Nomor tugas tidak valid.")
            except ValueError:
                print("Input harus berupa angka.")
        
    else:
        print("Program selesai")
        break