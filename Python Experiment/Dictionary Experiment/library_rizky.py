# Program sistem perpustakaan mini

import os, random, string, time

os.system("clear")

rak_buku = {}

#   KEY = 'B' + ''.join(random.choices(string.digits, k = 3))
title = "SELAMAT DATANG DI PERPUSTAKAAN RIZKY"

print(f'''┌────────────────────────────────────────┐
│ {title:^38} │
└────────────────────────────────────────┘''')
time.sleep(1)

while True:
    print()
    print("⎼"*25)
    print(f'{"Menu Perpustakaan":^25}')
    print("⎼"*25)
    print('''1) Lihat Daftar Buku
2) Cari dan Ubah Buku
3) Tambah Buku baru
4) Hapus Buku
5) Pinjam Buku
6) Kembalikan Buku
7) Keluar''')
    choice = input("Pilih Menu [1-7]: ")
        
# =======================================================================
# Jika user memilih untuk melihat daftar buku yang tersedia di rak perpustakaan

    if choice == "1":
        if rak_buku == {}:
            print("┌─────────────────────────────┐")
            print(f"│ Rak buku anda masih kosong! │")
            print("└─────────────────────────────┘")
        else:
            print(f" {'NO':<3} {'KODE':<6} {'JUDUL BUKU':<15} {'NAMA PENULIS':<15} {'STOK TERSEDIA':<12}")
            for i, KEY in enumerate(rak_buku):
                JUDUL = rak_buku[KEY]['nama']
                NAMA = rak_buku[KEY]['penulis']
                STOK = rak_buku[KEY]['stok']
                print(f" {i+1:<3} {KEY:<6} {JUDUL:<15} {NAMA:<19} {STOK:<5}")

# =======================================================================
# Jika user memilih untuk mencari dan mengubah buku yang tersedia di rak perpustakaan

    elif choice == "2":
        continue
    
# =======================================================================
# Jika user memilih untuk menambah buku baru ke rak perpustakaan

    elif choice == "3":
        rak_sementara = {} # dictionary untuk menyimpan data sementara sebelum dimasukan ke dictionary utama
        
        rak_sementara['nama'] = input("Masukan nama buku: ") # membuat key baru dengan nama 'nama' dan meminta user untuk memasukan value atau nilainya
        rak_sementara['penulis'] = input("Masukan nama penulis: ") # membuat key baru dengan nama 'penulis' dan meminta user untuk memasukan value atau nilainya
        rak_sementara['stok'] = input("Masukan stok buku: ") # membuat key baru dengan nama 'stok' dan meminta user untuk memasukan value atau nilainya
    
        KEY = 'B' + ''.join(random.choices(string.digits, k = 3)) # mengenerate kode random yang dimulai dari huruf "B" dengan total kode sebanyak 4 digit dan menjadikannya key unik
        
        rak_buku[KEY] = rak_sementara.copy() # menyimpan salinan data dictionary 'rak_sementara' ke dictionary utama bernama 'rak_buku'
        
        JUDUL = rak_buku[KEY]['nama']
        NAMA = rak_buku[KEY]['penulis']
        STOK = rak_buku[KEY]['stok']
        
        rak_buku.update({KEY:rak_sementara})
        
        print(f"Buku '{JUDUL}' berhasil ditambahkan dengan kode: {KEY}")
    
# =======================================================================
# Jika user memilih untuk menghapus buku dari rak perpustakaan

    elif choice == "4":
        continue
    
# =======================================================================
# Jika user memilih untuk meminjam buku dari perpustakaan

    elif choice == "5":
        continue
    
# =======================================================================
# Jika user memilih untuk mengembalikan buku yang dipinjam dari perpustakaan

    elif choice == "6":
        continue
    
# =======================================================================
# Jika user memilih untuk keluar dari sistem perpustakaan

    elif choice == "7":
        break
    

    else:
        continue



