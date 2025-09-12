# program manajemen produk

daftar_produk = [
    {"nama": "Roti", "harga": 3000, "stok": 50},
    {"nama": "Susu", "harga": 3000, "stok": 60},
    {"nama": "Roti Buaya", "harga": 130000, "stok": 20},
    {"nama": "Teh", "harga": 1500, "stok": 100},
]

print("┌────────────────────────────────┐")
print("│       SELAMAT DATANG DI        │")
print("│    SISTEM MANAJEMEN PRODUK     │")
print("└────────────────────────────────┘")

def lihat_produk():
    if not daftar_produk:
        print("Beluma ada produk yang ditambahkan!")
    else:
        title = f"│ {'NO':<3} {'NAMA BARANG':<15} {'HARGA':<12} {'STOK':<5} │"
        print(f"\n┌{'─'*(len(title)-2)}┐")
        print(title)
        print(f"├{'─'*(len(title)-2)}┤")
        for i, produk in enumerate(daftar_produk):
            NAMA = produk['nama']
            HARGA = produk['harga']
            STOK = produk['stok']

            i += 1
            i = str(i)
            i = i + '.'
            
            print(f"│ {i:<3} {NAMA:<15} Rp{HARGA:<10,} {STOK:^5} │".replace(",","."))

        print(f"└{'─'*(len(title)-2)}┘")
    
def tambah_produk(**data):
    daftar_produk.append(data)

def cari_ubah_produk():
    if not daftar_produk:
        print("Beluma ada produk yang ditambahkan!")
    else:
        cari_nama = input("Masukkan nama barang yang dicari: ").title()
        barang_ditemukan = []
        for item in daftar_produk:
            if cari_nama in item['nama']:
                barang_ditemukan.append((item))
                   
        if barang_ditemukan:
            print(f"\nHasil pencarian ditemukan {len(barang_ditemukan)} barang terkait")
            title = f"│ {'NO':<3} {'NAMA BARANG':<15} {'HARGA':<12} {'STOK':<5} │"
            print(f"┌{'─'*(len(title)-2)}┐")
            print(title)
            print(f"├{'─'*(len(title)-2)}┤")
            for i, produk in enumerate(barang_ditemukan):
                NAMA = produk['nama']
                HARGA = produk['harga']
                STOK = produk['stok']

                i += 1
                i = str(i)
                i = i + '.'
            
                print(f"│ {i:<3} {NAMA:<15} Rp{HARGA:<10,} {STOK:^5} │".replace(",","."))

            print(f"└{'─'*(len(title)-2)}┘")
            
            if len(barang_ditemukan) > 1:
                cari_nama = input("Masukkan nama barang yang ingin diubah: ").title()
                # barang_ditemukan = []
                barang_ada = True
                for item in barang_ditemukan:
                    if cari_nama == item['nama']:
                         barang_ada = False
                         barang_ditemukan = []
                         barang_ditemukan.append((item))
                
                if barang_ada:
                    print("\nBarang tidak ditemukan!")
                    return                   

            konfirm = input(f"Apakah ingin mengubah data produk ini? (y/n): ").lower()
            
            if konfirm == 'y':
                print("\nApa yang ingin diubah?")
                print("1. Nama produk")
                print("2. Harga")
                print("3. Stok")
                pilihan = input("Pilihan anda [1/2/3]: ")
                if pilihan == '1':
                    nama_baru = input("Masukkan nama yang baru: ").title()
                    barang_sudah_ada = False
                    for barang in daftar_produk:
                        if nama_baru in barang['nama']:
                            barang_sudah_ada = True
                        continue
                    
                    if barang_sudah_ada:
                        print("\nBarang dengan nama tersebut sudah tersedia!")
                    else:
                        for barang in barang_ditemukan:
                            if cari_nama in barang['nama']:
                                barang['nama'] = nama_baru
                                print("\nProduk berhasil diperbarui!")
                    
                if pilihan == '2':
                    harga_baru = int(input("Masukkan harga baru: "))
                    while harga_baru < 0:
                        print("Harga baru tidak boleh kurang dari 0!")
                        harga_baru = int(input("Masukkan harga baru dengan benar: "))
                    for barang in barang_ditemukan:
                        barang['harga'] = harga_baru
                        print("\nProduk berhasil diperbarui!")
                    
                if pilihan == '3':
                    stok_baru = int(input("Masukkan stok yang baru: "))
                    while stok_baru < 0:
                        print("Stok baru tidak boleh kurang dari 0!")
                        stok_baru = int(input("Masukkan stok yang baru dengan benar: "))
                    for barang in barang_ditemukan:
                        barang['stok'] = stok_baru
                        print("\nProduk berhasil diperbarui!")
                
            else:
                print("\nProduk batal diubah!")
                
        else:
            print("\nBarang tidak ditemukan!") 

def hapus_produk():
    hapus = input("Masukkan nama barang yang ingin dihapus: ").title()
    
    for i, item in enumerate(daftar_produk):
        if item['nama'] == hapus:
            konfirmasi = input("Apakah yakin ingin menghapus barang ini (y/n): ").lower()
            if konfirmasi == 'y':
                daftar_produk.pop(i)
                print(f"\nProduk '{hapus}' berhasil dihapus")
            else:
                print("\nPenghapusan dibatalkan!")
            return
    else:
        print("\nProduk tidak ditemukan!")
        

while True:
    print('''
=== SISTEM MANAJEMEN PRODUK ===
1. Lihat produk
2. Tambah produk
3. Cari & ubah produk
4. Hapus Produk
5. Keluar
-------------------------------''')
    choice = input("Apa yang ingin Anda lakukan [1-5]: ")
    
# ========================================================================================================
# 1. Lihat produk
    if choice == '1':
        lihat_produk()
                
# ========================================================================================================
# 2. Tambah produk
    if choice == '2':
        barang = input("Masukkan nama barang yang ingin ditambahkan: ").title()
        barang_sudah_ada = False
        for produk in daftar_produk:
            if barang in produk['nama']:
                barang_sudah_ada = True
        
        if barang_sudah_ada:
            print("Barang tersebut sudah tersedia!")
            continue
        
        harga = int(input("Masukkan harga dari barang tersebut: "))
        if harga < 0:
            print("Harga tidak bisa lebih kecil dari 0!")
            continue
        
        stok = int(input("Masukkan jumlah stok dari barang yang ditambahkan: "))
        if stok < 0:
            print("Jumlah stok tidak bisa lebih kecil dari 0!")
            continue
        
        tambah_produk(nama = barang, harga = harga, stok = stok)
        
# ========================================================================================================
# 3. Cari dan ubah produk
    if choice == '3':
        cari_ubah_produk()

# ========================================================================================================
# 4. Hapus produk
    if choice == '4':
        lihat_produk()
        hapus_produk()
        
# ========================================================================================================
# 5. Keluar program
    if choice == '5':
        print('Program selesai.')
        break
        
        
        
        
