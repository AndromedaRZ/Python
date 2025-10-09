# PROJEK CRUD

import os
import CRUD as CRUD

if __name__ == '__main__':
    sistem_operasi = os.name # untuk mendeteksi sistem operasi yang dipakai user

    match sistem_operasi:
        case 'posix': os.system('clear')
        case 'nt': os.system('cls')
    
    print("SELAMAT DATANG DI PROGRAM")
    print("DATABASE PERPUSTAKAAN")
    print("============================")
    
    # check apakah databasenya ada atau tidak
    CRUD.init_console()
    
    while(True): 
        match sistem_operasi: # match ini hampir sama dengan fungasi if-else
            case 'posix': os.system('clear') # jika os nya mac atau cocok dengan 'posix', maka prorgam ini akan dieksekusi
            case 'nt': os.system('cls') # jika os nya windows atau cocok dengan 'nt', maka program ini akan dieksekusi
        
        print("SELAMAT DATANG DI PROGRAM")
        print("DATABASE PERPUSTAKAAN")
        print("============================")
            
        print("1. Read Data")
        print("2. Create Data")
        print("3. Update Data")
        print("4. Delete Data\n")
        
        user_option = input("Masukan opsi [1-4]: ")
        
        
        match user_option:
            case '1': CRUD.read_console()
            case '2': CRUD.create_console()
            case '3': print('Update Data')
            case '4': print('Delete Data')
            
        isDone = input("Apakah selesai? [y/n]: ").lower()
        if isDone == 'y':
            break
        
        
    print('Program Berakhir, Terima Kasih')