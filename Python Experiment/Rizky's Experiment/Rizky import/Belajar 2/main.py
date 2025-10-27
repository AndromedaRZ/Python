import os
import Module as modul

if __name__ == '__main__':
    sistem_operasi = os.name # untuk mendeteksi sistem operasi yang dipakai user
    
    match sistem_operasi:
        case 'posix': os.system('clear')
        case 'nt': os.system('cls')
        
    # mengecek apakah file jsonnya sudah ada atau belum saat programnya pertama kali berjalan
    modul.init_console()
    
    while True:
        print("\nSELAMAT DATANG DI PROGRAM")
        print("MANAJEMEN KEUANGAN PRIBADI")
        print("==============================")
        
        print("1. Tambah Transaksi")
        print("2. Lihat Semua Transaksi")
        print("3. Hapus Transaksi")
        print("4. Keluar")
        
        pilihan = input("Masukan opsi [1-4]: ")
        
        match pilihan:
            case '1': modul.create_console()
            case '2': modul.read_console()
            case '3': modul.delete_console()
            case '4': break
            
print("Program Selesai, selamat tinggal")
        