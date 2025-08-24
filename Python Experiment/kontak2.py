# PROGRAM BUKU KONTAK TELEPON MENGGUNAKAN DICTIONARY

import os

os.system("clear")

print('''┌───────────────────────────────────────┐
│ SELAMAT DATANG DI BUKU KONTAK TELEPON │
└───────────────────────────────────────┘''')

kontak_template = {
    'nama': 'rizki',
    'nomor': '08821292893'
}

kontak_dict = {}

while True:
    kontak = dict.fromkeys(kontak_template.keys()) # membuat dictionary baru bernama 'kontak' setiap kali loop berjalan

    print('''
1) Lihat Semua Kontak
2) Tambah Kontak
3) Cari & Ubah Kontak
4) Hapus Kontak
5) Keluar''')

    choice = input("Apa yang ingin anda lakukan? [1-5]: ") # meminta user memilih diantara 5 pilihan di atas berdasarkan apa yang ingin dilakukan user
    
    if choice == "":
        print("Masukan pilihan yang benar!") 
    
    elif choice == '1': # jika user memilih ingin melihat semua daftar kontak
        if len(kontak_dict) == 0: # jika daftar kontak kosong, maka akan muncul tampilan yang diprint di bawah ini
            print("\n┌───────────────────────────────────────┐")
            print('│    Daftar kontak anda masih kosong    │')
            print("└───────────────────────────────────────┘")
            continue
        
        else: # jika ada minimal satu kontak di dalam daftar kontak, maka akan ditampilkan nama beserta nomornya
            print(f'\n┌────┬──────────────┬───────────────┐')
            print(f'│ {"NO":<2} │ {"NAMA":<13}│ {"NOMOR KONTAK":<14}│')
            print(f'├────┼──────────────┼───────────────┤')
            for i, KEY in enumerate(kontak_dict): # untuk menampilkan nama dan nomor dari dalam 'kontak_dict' menggunakan for dan index (i) untuk memunculkan numberingnya
                NAMA = kontak_dict[KEY]['nama'] 
                NOMOR = kontak_dict[KEY ]['nomor']
                print(f'│ {i+1}. │ {NAMA:<13}│ {NOMOR:<14}│')
            print(f'└────┴──────────────┴───────────────┘')
        
    elif choice == '2': # jika user memilih ingin menambahkan kontak baru
        
        kontak['nama'] = input("\nMasukan nama kontak: ")
        
        kontak['nomor'] = input("Masukan nomor telepon: ")
        KEY = kontak['nama'] # menggunakan 'nama' kontak sebagai key unik
        kontak_dict[KEY] = kontak.copy() # membuat dictionary baru bernama 'kontak' dan menyalin setiap key dan valuenya ke dalam dictionary 'kontak_dict' yang awalnya kosong
        
        print("\n┌───────────────────────────────────────┐")
        print(f"│ {"Berhasil Menambahkan ke Daftar Kontak"} │")
        print("└───────────────────────────────────────┘")
        
    
    elif choice == '3': # jika user memilih ingin mengubah salah satu kontak di dalam daftar kontak
        
        if len(kontak_dict) == 0: # jika daftar kontak kosong, maka akan muncul tampilan yang diprint di bawah ini
            print("\n┌───────────────────────────────────────┐")
            print('│    Daftar kontak anda masih kosong    │')
            print("└───────────────────────────────────────┘")
            continue
        
        KEY = input("Masukan nama kontak yang ingin anda cari: ")
        
        if KEY not in kontak_dict:
            print("\n┌───────────────────────────────────────┐")
            print("│    Kontak yang anda cari tidak ada    │")
            print("└───────────────────────────────────────┘")
            
        else:
            NAMA = kontak_dict[KEY]['nama']
            NOMOR = kontak_dict[KEY ]['nomor']
            
            print("\n┌───────────────────────────────────────┐")
            print("│           Kontak Ditemukan            │") 
            print("├──────────────────┬────────────────────┤")
            print(f"│ {NAMA:<17}│ {NOMOR:<19}│")
            print("└──────────────────┴────────────────────┘")
            
 
            isUbah = input("\nApakah ingin mengubah nomor kontak ini? [y/n]: ")
            
            if isUbah == "n":
                print(">>> Kembali ke Menu")
                
            elif isUbah == "y":
                nomor_baru = input("Masukan nomor baru: ")
                kontak_dict[KEY]['nomor'] = nomor_baru # memasukkan value baru bernama variabel 'nomor baru' untuk key 'nomor' yang memiliki KEY unik sesuai nama yang user input
                
                print("\n┌───────────────────────────────────────┐")
                print(f'│{'Nomor kontak berhasil diubah':^39}│')
                print("└───────────────────────────────────────┘")
    
    elif choice == '4': # jika user memilih ingin menghapus salah satu kontak dari dalam daftar kontak
        if len(kontak_dict) == 0:
            print("\n┌───────────────────────────────────────┐")
            print('│    Daftar kontak anda masih kosong    │')
            print("└───────────────────────────────────────┘")
            continue
        
        else:
            dihapus = input("Masukan nama kontak yang ingin anda hapus: ")
            
            if dihapus not in kontak_dict:
                print("\n┌───────────────────────────────────────┐")
                print("│    Kontak yang anda cari tidak ada    │")
                print("└───────────────────────────────────────┘")
            
            else:
                del kontak_dict[dihapus]
                print("\n┌───────────────────────────────────────┐")
                print(f"│{'Kontak berhasil dihapus':^39}│")
            print("└───────────────────────────────────────┘")
                
                
        
    elif choice == '5': # jika user memilih ingin keluar dari program buku kontak
        break
    
    else:
        print("Masukan pilihan yang benar!")
        
print("\n┌───────────────────────────────────────┐")
print(f'│{'SELAMAT TINGGAL':^39}│')
print("└───────────────────────────────────────┘")
        
        



    