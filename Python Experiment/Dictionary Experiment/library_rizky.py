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
2) Cari Buku
3) Tambah Buku baru
4) Ubah Data Buku
5) Hapus Buku
6) Pinjam Buku
7) Kembalikan Buku
8) Keluar''')
    choice = input("Pilih Menu [1-8]: ")

# =======================================================================
# Jika user memilih untuk melihat daftar buku yang tersedia di rak perpustakaan
    if choice == "1":
        if rak_buku == {}: # jika rak buku masih kosong, maka user akan diperingatkan dengan kalimat di bawah ini
            print("\n┌─────────────────────────────┐")
            print("│ Rak buku anda masih kosong! │")
            print("└─────────────────────────────┘")
        else: # jika rak buku ada isinya, maka program di bawah ini akan berjalan dan menampilkan semua buku yang tersedia di rak perpustakaan
            print("\n┌──────────────────────────────────────────────────────────┐")
            print(f"│ {'NO':<3} {'KODE':<6} {'JUDUL BUKU':<15} {'NAMA PENULIS':<15} {'STOK TERSEDIA':<12} │")
            print("├──────────────────────────────────────────────────────────┤")
            for i, KEY in enumerate(rak_buku):
                JUDUL = rak_buku[KEY]['judul']
                NAMA = rak_buku[KEY]['penulis']
                STOK = rak_buku[KEY]['stok']
                print(f"│ {i+1:<3} {KEY:<6} {JUDUL:<15} {NAMA:<19} {STOK:<9} │")
            print("└──────────────────────────────────────────────────────────┘")
            
# =======================================================================
# Jika user memilih untuk mencari buku yang tersedia di rak perpustakaan
    elif choice == "2":
        if rak_buku == {}: # jika rak buku masih kosong, maka user akan diperingatkan dengan kalimat di bawah ini
            print("\n┌─────────────────────────────┐")
            print("│ Rak buku anda masih kosong! │")
            print("└─────────────────────────────┘")
            
        else: # jika rak buku ada isinya, maka program di bawah ini akan berjalan
            keyword = input("Masukan kata kunci buku yang ingin dicari: ").title() # meminta user untuk memasukan keyword atau kata kunci dari buku yang ingin dicari, bisa mencari lewat nama buku atau nama penulis bukunya
            hasil_cari = [] # list untuk menyimpan KEY (kode buku) yang cocok dengan pencarian
            for KEY in rak_buku:
                if keyword in rak_buku[KEY]['judul'] or keyword in rak_buku[KEY]['penulis']: # memeriksa setiap keyword atau kata kunci yang cocok di dalam rak buku
                    hasil_cari.append(KEY) # menyimpan semua kode buku (semua data bukunya seperti nama, penulis, dan stoknya) ke dalam list sementara bernama 'hasil_cari'
            if hasil_cari: # jika sudah ada buku yang cocok dengan keyword atau kata kunci user, maka kode di bawah ini akan menampilkan seluruh buku yang sesuai
                print("\n┌──────────────────────────────────────────────────────────┐")
                print(f"│ {'NO':<3} {'KODE':<6} {'JUDUL BUKU':<15} {'NAMA PENULIS':<15} {'STOK TERSEDIA':<12} │")
                print("├──────────────────────────────────────────────────────────┤")
                for i, KEY in enumerate(hasil_cari):
                    JUDUL = rak_buku[KEY]['judul']
                    NAMA = rak_buku[KEY]['penulis']
                    STOK = rak_buku[KEY]['stok']
                    print(f"│ {i+1:<3} {KEY:<6} {JUDUL:<15} {NAMA:<19} {STOK:<9} │")
                print("└──────────────────────────────────────────────────────────┘")
            else: # jika tidak ada buku yang cocok dengan keyword atau kata kunci yang dimasukan user
                print("\n┌───────────────────────┐")
                print("│ Buku tidak ditemukan! │")
                print("└───────────────────────┘")
                
        
# =======================================================================
# Jika user memilih untuk menambah buku baru ke rak perpustakaan
    elif choice == "3":
        rak_sementara = {} # dictionary untuk menyimpan data sementara sebelum dimasukan ke dictionary utama
        
        rak_sementara['judul'] = input("Masukan nama buku: ").title() # membuat key baru dengan nama 'nama' dan meminta user untuk memasukan value atau nilainya
        rak_sementara['penulis'] = input("Masukan nama penulis: ").title() # membuat key baru dengan nama 'penulis' dan meminta user untuk memasukan value atau nilainya
        rak_sementara['stok'] = int(input("Masukan stok buku: ")) # membuat key baru dengan nama 'stok' dan meminta user untuk memasukan value atau nilainya
    
        KEY = 'B' + ''.join(random.choices(string.digits, k = 3)) # mengenerate kode random yang dimulai dari huruf "B" dengan total kode sebanyak 4 digit dan menjadikannya key unik
        
        rak_buku[KEY] = rak_sementara.copy() # menyimpan salinan data dictionary 'rak_sementara' ke dictionary utama bernama 'rak_buku'
        
        JUDUL = rak_buku[KEY]['judul']
        NAMA = rak_buku[KEY]['penulis']
        STOK = rak_buku[KEY]['stok']
        
        rak_buku.update({KEY:rak_sementara})
        
        print(f"Buku '{JUDUL}' berhasil ditambahkan dengan kode: {KEY}")

# =======================================================================
# Jika user memilih untuk mengubah data buku dari rak perpustakaan
    elif choice == "4":
        continue

# =======================================================================
# Jika user memilih untuk menghapus buku dari rak perpustakaan
    elif choice == "5":
        continue
    
# =======================================================================
# Jika user memilih untuk meminjam buku dari perpustakaan
    elif choice == "6":
        continue
    
# =======================================================================
# Jika user memilih untuk mengembalikan buku yang dipinjam dari perpustakaan
    elif choice == "7":
        continue
    
# =======================================================================
# Jika user memilih untuk keluar dari sistem perpustakaan
    elif choice == "8":
        break
    

    else:
        continue



