
# program fungsi tambah kontak pada manajemen kontak 

import re

dict_contact= {}

def tambah_kontak(dict_kontak,**sementara):
    while True:
        nama = input("Masukan nama kontak: ")
        sementara['nama'] = nama
        
        while True:
            nomor = input("Masukan nomor kontak: ")
            if len(nomor) == 12 and nomor.isdigit(): # fungsi ini akan memastikan nilai yang user input panjang angkanya harus 12 angka (len(nomor) == 2) dan karakter yang diinput harus berupa angka, tetapi bukan integer (method nomor.isdigit())
                sementara['nomor'] = nomor
                break
            else:
                print("Nomor telepon tidak sesuai!") 
        
        while True:
            email = input("Masukan email kontak: ")
            if re.fullmatch(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}", email): # fungsi ini akan memastikan nilai yang user input berupa format email dan bukan yang lain, contoh sekian@gmail.com
                sementara['email'] = email
                break
            else:
                print("Email tidak valid!")
        
        for kontak in dict_kontak.values():
            if (kontak['nama'] == nama and kontak['nomor'] == nomor and kontak['email'] == email):
                print("Kontak tersebut sudah ada!")
                return None
        
        KEY = sementara['nama']
        dict_kontak[KEY] = sementara.copy()
        return sementara


