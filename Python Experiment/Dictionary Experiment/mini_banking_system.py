# program sistem mini banking

import os, json, datetime, random, string

os.system("clear")

akun_bank = {}

with open("data_akun_bank.json", "r") as file:
    data = json.load(file) # memanggil data dari file json eksternal
    akun_bank.update(data) # mengupdate atau menyalin data yang ada di file json eksternal yang dipanggil ini ke dictionary akun_bank


title = "│ SELAMAT DATANG DI BANK RIZKY │"

print(f"┌{'─'*(len(title) - 2)}┐")
print(title)
print(f"└{'─'*(len(title) - 2)}┘")

while True:
    print()
    print("⎼"*20)
    print(f'{"Menu Bank":^20}')
    print("⎼"*20)
    print('''1) Login
2) Buat Akun
3) Lihat Akun Bank
4) Keluar''')
    choice = input("Pilih menu [1/2/3/4]: ")
    
# =========================================================================================================================================
# Jika user ingin login ke sistem bank    
    if choice == '1':  
        if akun_bank == {}: # Jika belum ada akun yang terdaftar, maka user akan diperingatkan kalimat di bawah ini
            title = "│ Belum ada akun yang terdaftar! │"
            print(f"\n┌{'─'*(len(title) - 2)}┐")
            print(title)
            print(f"└{'─'*(len(title) - 2)}┘")
        else:
            nama_verifikasi = input("Masukan nama akun anda: ")
            pin_verifikasi = input("Masukan pin akun anda: ") 
            if pin_verifikasi.isdigit() and len(pin_verifikasi) == 6: # memastikan bahwa pin yang dimasukan hanyalah angka dan panjangnya 6 digit tidak kurang dan lebih
                
                akun_login = []
                
                pin_matched = False
                for key, value in akun_bank.items(): # akan memeriksa dictionary akun_bank menggunakan for loop untuk mengecek apakah ada nama dan pin yang cocok dengan yang dimasukan user untuk login
                    if nama_verifikasi in value['nama'] and pin_verifikasi in value['pin']: # memeriksa apakah nama dan pin yang dimasukan user cocok atau tidak dengan dengan yang ada di dictionary utama (akun_bank)
                        akun_login.append(key) # memasukan no rekening dari akun yang sedang login ke dictionary verifikasi
                        pin_matched = True
                        
                if akun_login:
                    for key in akun_login:
                        title = "│ Login Berhasil │"
                        print(f"\n┌{'─'*(len(title) - 2)}┐")
                        print(title)
                        print(f"└{'─'*(len(title) - 2)}┘")
                        while True:
                            print()
                            print("⎼"*20)
                            print(f'{"Menu Akun":^20}')
                            print("⎼"*20)
                            print('''1) Informasi Akun
2) Setor Tunai
3) Tarik Tunai
4) Transfer
5) Logout''')
                            choice = input("Pilih Menu [1-5]: ")
# ========================================================================================================================================
# Jika user memilih untuk melihat informasi akun banknya                    
                            if choice == '1':
                                NAMA = akun_bank[key]['nama']
                                SALDO = akun_bank[key]['saldo']
                                title = f"│ {'Nama Akun':<14} │ {'No Rekening':<11} │"
                                value = f"│ {NAMA:<14} │ {key:<11} │"
                                value2 = f"│ {'Sisa Saldo: ':<10}Rp {SALDO:<13} │"
                                for key in akun_login:
                                    print(f"\n┌────────────────┬─────────────┐")
                                    print(title)
                                print(f"├────────────────┼─────────────┤")
                                print(value)
                                print(f"├────────────────┴─────────────┤")
                                print(value2)
                                print(f"└──────────────────────────────┘")
                                
# ========================================================================================================================================
# Jika user memilih untuk setor tunai ke rekeningnya                  
                            elif choice == '2':
                                deposit = int(input("Masukan jumlah uang (Rp): "))
                                confirm = input("Konfirmasi setor yes/batal [y/n]: ").lower()
                                if confirm == 'y':
                                    for key in akun_login:
                                        akun_bank[key]['saldo'] += deposit
                                        title = "│ Setor tunai berhasil │"
                                        print(f"\n┌{'─'*(len(title) - 2)}┐")
                                        print(title)
                                        print(f"└{'─'*(len(title) - 2)}┘")
                                
                                elif confirm == 'n':
                                    title = "│ Setor tunai dibatalkan │"
                                    print(f"\n┌{'─'*(len(title) - 2)}┐")
                                    print(title)
                                    print(f"└{'─'*(len(title) - 2)}┘")
                                    
                                else:
                                    title = "│ Setor tunai gagal │"
                                    print(f"\n┌{'─'*(len(title) - 2)}┐")
                                    print(title)
                                    print(f"└{'─'*(len(title) - 2)}┘")

# ========================================================================================================================================
# Jika user memilih untuk tarik tunai dari rekeningnya                     
                            elif choice == '3':
                                while True:
                                    print('''1) + Rp 50,000
2) - Rp 50,000
3) Tarik tunai
4) Kembali''')
                                    choice_ = 
                                
                    
# ========================================================================================================================================
# Jika user memilih untuk transfer saldo ke rekening lain                   
                            elif choice == '4':
                                    continue
                    
# ========================================================================================================================================
# Jika user memilih untuk keluar dari akun                 
                            elif choice == '5':
                                    title = "│ Logout berhasil │"
                                    print(f"\n┌{'─'*(len(title) - 2)}┐")
                                    print(title)
                                    print(f"└{'─'*(len(title) - 2)}┘")
                                    break      
                else:
                    title = "│ Login gagal │"
                    print(f"\n┌{'─'*(len(title) - 2)}┐")
                    print(title)
                    print(f"└{'─'*(len(title) - 2)}┘")
                             
                        
            else:
                title = "│ Login gagal │"
                print(f"\n┌{'─'*(len(title) - 2)}┐")
                print(title)
                print(f"└{'─'*(len(title) - 2)}┘")
                
# =========================================================================================================================================
# Jika user ingin membuat akun baru   
    elif choice == '2':
        data_sementara = {} # data sementara yang digunakan untuk menampung data untuk membuat akun
        
        data_sementara['nama'] = input("Masukan nama akun anda: ").lower() # membuat key baru bernama 'nama' dan meminta user untuk memasukan nilai atau valuenya
        
        pin_hanya_angka = False # dummy variabel untuk memastikan bahwa user memasukan angka untuk pinnya
        while pin_hanya_angka == False:
            pin = input("Masukan pin akun anda [6 digit]: ") # membuat key baru bernama 'pin' dan meminta user untuk memasukan nilai atau valuenya
            if pin.isdigit() and len(pin) == 6: # memastikan bahwa pin yang dimasukan hanyalah angka dan panjangnya 6 digit tidak kurang dan lebih
                pin_hanya_angka = True # keluar dari loop kalau benar
            else:
                title = "│ Pin harus berupa 6 digit angka, coba lagi! │"

                print(f"\n┌{'─'*(len(title) - 2)}┐")
                print(title)
                print(f"└{'─'*(len(title) - 2)}┘\n")
        
        data_sementara['pin'] = pin # membuat key baru bernama 'pin' dan mengambil pin yang tadi dimasukan user sebelumnya untuk dijadikan nilai atau valuenya
        
        KEY = ''.join(random.choices(string.digits, k = 6)) # generate nomor rekening random 6 digit dan menjadikannya key unik
        if KEY not in akun_bank: # untuk memastikan bahwa no rekening yang akan dijadikan key unik tidak sama dengan akun yang sudah terdaftar
            minimun_saldo = False
            while minimun_saldo == False:
                saldo_awal = int(input('Masukan saldo awal [min Rp 50,000]: '))
                if saldo_awal < 50000:
                    title = "│ Saldo kurang dari minimum! │"

                    print(f"\n┌{'─'*(len(title) - 2)}┐")
                    print(title)
                    print(f"└{'─'*(len(title) - 2)}┘\n")
                else:
                    minimun_saldo = True
                    
            data_sementara['saldo'] = saldo_awal
            
            akun_bank[KEY] = data_sementara.copy() # menyimpan salinan semua data yang ada di dictionary 'data_sementara' ke dictionary utama bernama 'akun_bank' untuk mengumpulkan semua akun yang telah dibuat
            
            title = "│ Akun berhasil dibuat     │"
            title2 = f"│ No Rekening Anda: {KEY} │"

            print(f"\n┌{'─'*(len(title2) - 2)}┐")
            print(title)
            print(title2)
            print(f"└{'─'*(len(title2) - 2)}┘")
            
        else:
            continue
# =========================================================================================================================================
# sistem khusus untuk admin bank, jika admin ingin melihat seluruh akun bank yang terdaftar
    elif choice == '3':
        if akun_bank == {}: # Jika belum ada akun yang terdaftar, maka user akan diperingatkan kalimat di bawah ini
            title = "│ Belum ada akun yang terdaftar! │"
            print(f"\n┌{'─'*(len(title) - 2)}┐")
            print(title)
            print(f"└{'─'*(len(title) - 2)}┘")
        else:
            title = f"│ {'No':<3} {'Nama Pengguna':<15} {'No Rekening':<12} {'Pin Akun':<9} {'Sisa Saldo':<15} │"
            print(f"\n┌{'─'*(len(title) - 2)}┐")
            print(title)
            print(f"├{'─'*(len(title) - 2)}┤")
            
            for i, KEY in enumerate(akun_bank):
                NAMA = akun_bank[KEY]['nama']
                PIN = akun_bank[KEY]['pin']
                SALDO = (akun_bank[KEY]['saldo'])
                print(f"│ {i+1:<3} {NAMA:<15} {KEY:<12} {PIN:<9} Rp {SALDO:<12,} │")
            print(f"└{'─'*(len(title) - 2)}┘")

# =========================================================================================================================================
# Jika user ingin keluar dari menu bank (otomatis akan mematikan program)
    elif choice == '4':
        with open("data_akun_bank.json", "w") as file:
            json.dump(akun_bank, file, indent=4)
            
        exit()
