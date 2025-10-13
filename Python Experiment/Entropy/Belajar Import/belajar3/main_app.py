# Program manajemen pengeluaran harian

import os
import Module

if __name__ == '__main__':
    sistem_operasi = os.name
    
    match sistem_operasi:
        case 'posix': os.system("clear")
        case 'nt': os.system("cls")
    
    Module.init_console()
    
    while True:
        # match sistem_operasi:
        #     case 'posix': os.system("clear")
        #     case 'nt': os.system("cls")
        
        
        print("\nSelamat datang di Program")
        print("Manajemen Pengeluaran Harian")
        print("============================")
        
        print("1. Tambah Pengeluaran")
        print("2. Lihat Semua Pengeluaran")
        print("3. Cari Pengeluaran")
        print("4. Hapus Pengeluaran")
        print("5. Lihat Total Pengeluaran")
        print("6. Keluar")
        
        option = input("Masukkan opsi [1-6]: ")
        
        match option:
            case '1':
                Module.create_console()
            case '2':
                Module.read_console()
            case '3':
                Module.search_console()
            case '4':
                Module.delete_console()
            case '5':
                Module.total_console()
            case '6':
                print("\nProgram selesai.")
                break
