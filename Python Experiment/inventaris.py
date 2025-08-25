import random
import string

inventaris = {}
print("Selamat datang di program manajemen inventaris toko")

while True:
    inventaris_sementara = {}
    
    print("""
1) Tambah barang
2) Lihat daftar barang
3) Cari barang
4) Update stok
5) Hapus barng
6) Keluar""")
    choice = input("Apa yang ingin anda lakukan? ")
    
    if choice == '1':
        inventaris_sementara['nama'] = input("Masukkan nama barang: ").capitalize()
        inventaris_sementara['stok'] = int(input("Masukkan stok yang tersedia: "))
        inventaris_sementara['harga'] = int(input("Masukkan harga barang: "))
        
        # Generate KEY
        KEY = "A" + "".join(random.choices(string.digits, k = 3))
        
        # Cek apakah barang dengan nama yang sama sudah ada di dalam inventaris
        barang_sudah_ada = False # dummy variabel False
        for item in inventaris.values(): # untuk setiap item yang ada di dalam dict inventaris, tapi kita menambahkan .values() yang berarti untuk setiap values di dalam dict inventaris
            if inventaris_sementara['nama'] == item['nama']: # jika 'value' dari 'nama' yang kita input ada yang sama dengan value dari key 'nama' di dalam inventaris utamanya
                barang_sudah_ada = True # maka dummy variabel akan berubah menjadi True
            break
        if barang_sudah_ada == True: # lalu men-trigger baris disini
            print("\nBarang tersebut sudah ada di inventaris")
            continue # dan meminta program untuk langsung lanjut ke perulangan berikutnya tanpa menjalankan baris perintah di bawahnya terlebih dahulu untuk satu kali perulangan ini
                    
        inventaris[KEY] = inventaris_sementara.copy()
        print(inventaris_sementara)
        print(inventaris)
        
    elif choice == '2':
        if len(inventaris) == 0:
            print("\nBelum ada barang yang ditambahkan ke inventaris")
        else:
            title = f"{'Kode':<4} {'Nama barang':<15} {'Jumlah stok':<9} {'Harga':<8}"
            
            print("-"*len(title))
            print(title)
            print("-"*len(title))
            for i in inventaris:
                KEY = i
                NAMA = inventaris[KEY]['nama']
                STOK = inventaris[KEY]['stok']
                HARGA = inventaris[KEY]['harga']
                
                print(f"{KEY:<4} {NAMA:<15} {STOK:^11} {HARGA:,}")
                
    elif choice == '3':
        if len(inventaris) == 0:
            print("\nBelum ada barang yang ditambahkan ke inventaris")
        else:
            cari_barang = input("Masukkan nama barang yang ingin dicari: ").capitalize()
            barang_ketemu = False # dummy variabel False
            for items in inventaris.values(): # untuk setiap item yang ada di dict inventaris, tetapi kita menambahkan fungsi .values() yang berarti untuk setiap key (tidak termasuk KEY unik), dan value yang ada di dalam dict inventaris
                print(items)
                if cari_barang == items['nama']: # jika nama barang yang kita input sama dengan value dari key 'nama' yang ada di dalam dict inventaris
                    barang_ketemu = True # dummy variabel akan berubah menjadi True
                    break
                
            if barang_ketemu == True: # dan dummy variabel akan mengeksekusi baris ini karena sudah menjadi True
                print("\nBarang ditemukan!")
                title = f"{'Kode':<4} {'Nama barang':<15} {'Jumlah stok':<9} {'Harga':<8}"
                print("-"*len(title))
                print(title)
                print("-"*len(title))
                # Cari key dari barang yang ditemukan
                for key, value in inventaris.items(): # karena kita menggunakan .items(), berarti penjelasannya untuk setiap KEY unik, key, dan value yang ada di dalam dict inventaris
                # sistem akan menunjukkan semua items (KEY unik, key, value) yang ada di dalam dict inventaris dengan cara perulangan (loop)
                    if value['nama'] == cari_barang: # jika nama barang yang kita input ada yang sama dengan value dari key 'nama' di dalam dict inventaris pada saat perulangan, maka otomatis kita akan mengakses KEY unik, key, dan value dari barang yang kita temukan tersebut dengan menggunakan if
                        # print(value) # bisa dilihat di baris ini untuk melihat valuenya
                        # print(key) # untuk melihat KEY uniknya
                        KEY = key
                        NAMA = value['nama'] # baris ini dan 2 setelahnya akan menampilkan value dari key 'nama',
                        STOK = value['stok'] # key 'stok',
                        HARGA = value['harga'] # dan key 'harga' yang dimiliki oleh KEY unik yang sudah kita akses tadi
                        print(f"{KEY:<4} {NAMA:<15} {STOK:^11} {HARGA:,}")
                        
            else:
                print("\nBarang tidak ditemukan!") # ini akan tereksekusi ketika barang yang kita input tidak ditemukan di dalam dict inventaris, tapi kenapa informasi 'barang tidak ditemukan' ini ada di bawah sini? karena saya tidak bisa memasukkan program untuk menunjukkan bahwa 'barang tidak ditemukan' di dalam for loop yang di baris sebelumnya
                    
                    