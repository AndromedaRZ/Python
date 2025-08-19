# prorgam sistem to-do-list pada python

import time

tugas = []

while True:
    time.sleep(0.5)
    print('\n=== Program to-do-list ===')
    print('''1) Tambah tugas
2) Lihat semua tugas
3) Hapus tugas
4) Keluar''')
    choice = int(input('Apa yang ingin anda lakukan? [1-4]: '))

    while choice > 4:
        choice = int(input('Apa yang ingin anda lakukan? [1-4]: '))


    if choice == 1: # jika user memilih untuk menambahkan tugas baru 
        tugas_tambah = input("\nMasukkan tugas yang ingin anda tambahkan: ")
        tugas.append(tugas_tambah)
        print(f'\n=== Tugas {tugas_tambah} sudah ditambahkan ===')

    elif choice == 2: # Jika user memilih untuk melihat semua tugas yang sudah dibuat
        if tugas == []: # Jika user ingin melihat list tugas tetapi masih kosong, maka program akan masuk ke dalam kondisi ini
            print("\n=== Tugas anda masih kosong ===")
        
        else:
            print("\n=== List tugas yang anda buat ===")
            for index, item in enumerate(tugas):
                print(f"{index + 1}. {item}")
            print("=================================")

    elif choice == 3: # Jika user memilih untuk menghapus salah satu list tugas
        if not tugas: # Jika tidak ada tugas yang tersisa, maka program ini akan dijalankan
            print("\n=== Tugas anda masih kosong ===")
        elif len(tugas) > 0: # Jika ada tugas yang tersisa, maka program ini akan dijalankan
            nomor = int(input('Nomor tugas yang ingin dihapus: '))
            if 1 <= nomor <= len(tugas): # Memastikan nomor tugas yang dimasukkan user sama dengan nomor yang tersedia di dalam list tugas
                dihapus = tugas.pop(nomor - 1)
                print(f"\n=== Tugas '{dihapus}' sudah dihapus ===")
            else: # Jika user memasukkan nomor yang tidak tersedia di dalam list tugas
                print('\n=== Nomor tugas tidak valid! ===')


    elif choice == 4: # Jika user memilih untuk langsung keluar program
        break

print('=== Selamat tinggal ===')