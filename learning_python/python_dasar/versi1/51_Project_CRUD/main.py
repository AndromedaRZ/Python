# membuat program perpustakaan digital

import os
import CRUD as CRUD

if __name__ == '__main__': # konvensional
    sistem_operasi = os.name # os.name digunakan untuk mengecek sistem operasi, apakah hasilnya 'posix': linux/apple atau 'nt': windows
    
    match sistem_operasi:
        case 'posix': os.system("clear")
        case 'nt': os.system("cls")
        
    print("Selamat datang di program")
    print("Database Perpustakaan")
    print("==========================")
    
    # mengecek apakah Databasenya ada atau tidak ada
    CRUD.init_console()
    
    while True:
        match sistem_operasi: # 'match' bisa dikatakan sebagai pencocokkan
            case "posix": os.system("clear") # dan 'case' digunakan untuk mencocokkan kondisi,
            # jika os name-nya adalah 'posix' atau 'linux/apple' maka perintah 'clear' akan dijalankan
            case "nt": os.system("cls") # dan jika os name-nya adalah 'nt' atau 'windows' maka perintah yang akan berjalan adalah 'cls'
            
            # 'clear' dan 'cls' digunakan untuk membersihkan terminal dan mengulang dari baris paling awal (baris atas)
        
        print("Selamat datang di program")
        print("Database Perpustakaan")
        print("==========================")
        
        print("1. Read Data")
        print("2. Create Data")
        print("3. Update Data")
        print("4. Delete Data")
        
        option = input('Masukkan opsi [1-4]: ')
        
        match option:
            case '1': CRUD.read_console()
            case '2': CRUD.create_console()
            case '3': CRUD.update_console()
            case '4': CRUD.delete_console()
            
        isDone = input("Apakah selesai? (y/n) ").lower()
        if isDone == 'y':
            break
        
    print("Program selesai, terima kasih KAKAK!!")
        