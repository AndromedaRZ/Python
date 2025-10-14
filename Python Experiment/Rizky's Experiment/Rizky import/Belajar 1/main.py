import os
import Modul as Modul

if __name__ == '__main__':
    sistem_operasi = os.name # untuk mendeteksi sistem operasi yang dipakai user
    
    match sistem_operasi:
            case 'posix': os.system('clear')
            case 'nt': os.system('cls')
    
    
    # untuk mengecek apakah data inventarisnya sudah dibuat atau belum saat program dijalankan
    Modul.init_json()
        
    while(True):
        print("\nSELAMAT DATANG DI PROGRAM")
        print('INVENTARIS MINIMARKET')
        print("==============================")
        
        print("1. Lihat Data Barang")
        print("2. Tambah Barang")
        print("3. Update Barang")
        print("4. Hapus Barang")
        print("5. Keluar\n")
        
        pilihan_user = input("Masukan opsi [1-5]: ")
        
        match pilihan_user:
            case '1': Modul.read_data()
            case '2': Modul.create_data()
            case '3': Modul.update_data()
            case '4': Modul.delete_data()
            case '5': break
            
print("Program Berhenti, selamat tinggal")