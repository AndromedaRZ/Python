# Sistem login menggunakan dictionary

import os

os.system("clear")

users_template = {
    'nama':'rizky',
    'password':'12345'
}

users_dict = {}

while True:
    users = dict.fromkeys(users_template.keys()) # membuat dictionary baru bernama 'users' dengan mengambil key dari dictionary 'users_template'
    print("\n┏━━━━━━━━━━━━━━━━━━━━━┓")
    print(f"┃{"HALAMAN LOGIN":^21}┃")
    print("┗━━━━━━━━━━━━━━━━━━━━━┛")
    print('''1) Daftar Akun
2) Login
3) Keluar''')

    choice = input('Apa yang ingin anda lakukan? [1-3]: ')    
    if choice == "": # jika user menekan enter sebelum memilih angka untuk aksi selanjutnya
        print("Masukan pilihan yang benar!")

# =============================================================
# Daftar akun baru untuk login    
    elif choice == "1":    
        users['nama'] = input("Masukan username baru: ")
        KEY = users['nama'] # menggunakan 'nama' atau usernamenya sebagai key unik
        # users_dict[KEY] = users.copy()
        
        if KEY in users_dict:
            print("Username sudah terpakai!")
        else:
            users['password'] = input("Masukan passwordnya: ")
            users_dict[KEY] = users.copy()
            print("Akun berhasil dibuat!")
            
        
# =============================================================
# Login ke menu utama
    elif choice == "2":
        KEY = input("Masukan username: ")
        
        if KEY in users_dict:
            check_password = input("Masukan password: ")
            if check_password == users_dict[KEY]['password']:
                print("Anda berhasil login!")
                
                # Isi setelah berhasil login
                while True:
                    print("\n┏━━━━━━━━━━━━━━━━━━━━━┓")
                    print(f"┃{"MENU UTAMA":^21}┃")
                    print("┗━━━━━━━━━━━━━━━━━━━━━┛")
                    print('''1) Lihat Profil
2) Logout''')    
                    choice2 = input("Pilih menu [1-2]: ")
                    if choice2 == "":
                        print("Masukan pilihan yang benar!")
                    
                    elif choice2 == '1':
                        print("\nProfil anda")
                        for i, KEY in enumerate(users_dict):
                            USERNAME = users_dict[KEY]['nama']
                            PASS = users_dict[KEY]['password']
                            
                            print(f'{i+1}. username: {USERNAME}, password: {PASS}')
                            
                    
                    elif choice2 == '2':
                        print('Anda telah logout')
                        break
                    
                    else:
                        print("Masukan pilihan yang benar!")
                
            else:
                print("Password salah! Silakan coba lagi.\n")
        else:
            print('Username tidak ditemukan!')



# =============================================================
# Keluar dari halaman login
    elif choice == "3":
        break
    
    else: # jika user memasukkan pilihan yang tidak valid
       print("Masukan pilihan yang benar!")
       
print("Program selesai")