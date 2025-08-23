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
    kontak = dict.fromkeys(kontak_template.keys())

    print('''
1) Lihat Semua Kontak
2) Tambah Kontak
3) Cari Kontak
4) Hapus Kontak
5) Keluar''')

    choice = int(input("Apa yang ingin anda lakukan?[1-5]: "))
    while choice > 5:
        print("Masukan pilihan yang benar!\n")
        choice = int(input("Apa yang ingin anda lakukan?[1-5]: "))

    if choice == 1:
        if len(kontak_dict) == 0:
            print('Daftar kontak anda masih kosong')
            continue
        
        else:
            print(f'┌────┬──────────────┬───────────────┐')
            print(f'│ {"NO":<2} │ {"NAMA":<13}│ {"NOMOR KONTAK":<14}│')
            print(f'├────┼──────────────┼───────────────┤')
            for i, KEY in enumerate(kontak_dict):
                NAMA = kontak_dict[KEY]['nama']
                NOMOR = kontak_dict[KEY ]['nomor']
                print(f'│ {i+1}. │ {NAMA:<13}│ {NOMOR:<14}│')
            print(f'└────┴──────────────┴───────────────┘')
        
    if choice == 2:
        
        kontak['nama'] = input("Masukan nama kontak: ")
        kontak['nomor'] = input("Masukan nomor telepon: ")
        
        KEY = kontak['nama'] # menggunakan 'nama' kontak sebagai key unik
        kontak_dict[KEY] = kontak.copy()
            
 
        
    if choice == 5:
        break


    