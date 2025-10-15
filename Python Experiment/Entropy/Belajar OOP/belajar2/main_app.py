# Sistem perpustakaan digital

import os

if __name__ == '__main__':
    sistem_operasi = os.name
    
    match sistem_operasi:
        case 'posix': os.system("clear")
        case 'nt': os.system("cls")
        
    while True:
        
        
         
        print("=== Sistem Perpustakaan Digital ===")
        print("1. Tambah Buku")
        print("2. Tambah Anggota")
        print("3. Pinjam Buku")
        print("4. Kembalikan Buku")
        print("5. Tampilkan Semua Buku")
        print("6. Keluar")
        option = input("Masukkan opsi [1-6]: ")
        
        match option:
            case '1':
                print("1. Tambah Buku")
            case '2':
                print("2. Tambah Anggota")
            case '3':
                print("3. Pinjam Buku")
            case '4':
                print("4. Kembalikan Buku")
            case '5':
                print("5. Tampilkan Semua Buku")
            case '6':
                print("6. Keluar")