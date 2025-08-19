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
        print('Tugas anda sudah ditambahkan')
        
    elif choice == 2: # Jika user memilih untuk melihat semua tugas yang sudah dibuat
        if tugas == []: # Jika user ingin melihat list tugas tetapi masih kosong, maka program akan masuk ke dalam kondisi ini
            print("\nTugas anda masih kosong")
        
        else:
            print("\nList tugas yang anda buat")
            for index, item in enumerate(tugas,start=1):
                print(index,".", item)
        
    elif choice == 3: # Jika user memilih untuk menghapus salah satu list tugas
        if tugas == []: # Jika list tugas masih kosong saat user ingin menghapus salah satu tugasnya, maka program akan masuk ke dalam kondisi ini
            print("\nTugas anda masih kosong")
        else:
            nomor = int(input('Nomor tugas yang ingin: '))
            tugas.pop(nomor - 1)
            print('Tugas anda sudah dihapus')
        
    elif choice == 4: # Jika user memilih untuk langsung keluar program
        break
    
print('Selamat tinggal')