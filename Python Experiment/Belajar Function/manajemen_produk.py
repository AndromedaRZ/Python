# program manajemen produk

daftar_produk = [
    {"nama": "Roti", "harga": 3000, "stok": 50},
    {"nama": "Susu", "harga": 3000, "stok": 60},
]

print(daftar_produk, type(daftar_produk))


print("┌────────────────────────────────────────┐")
print("│           SELAMAT DATANG DI            │")
print("│        SISTEM MANAJEMEN PRODUK         │")
print("└────────────────────────────────────────┘")

def lihat_produk():
    if not daftar_produk:
        print("Beluma ada produk yang ditambahkan!")
    else:
        title = f"│ {'NO':<3} {'NAMA BARANG':<15} {'HARGA':<10} {'STOK':<5} │"
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
            
            print(f"│ {i:<3} {NAMA:<15} {HARGA:<10,} {STOK:<5} │".replace(",","."))

        print(f"└{'─'*(len(title)-2)}┘")
    
def tambah_produk(**data):
    daftar_produk.append(data)

def cari_produk():
    if not daftar_produk:
        print("Beluma ada produk yang ditambahkan!")
    else:
        cari_nama = input("Masukkan nama barang yang dicari: ").capitalize()
        barang_ada = False
        for item in daftar_produk:
            if cari_nama in item['nama']:
                barang_ada = True
                   
        if barang_ada:
            print(item)
        else:
            print("Barang tidak ditemukan!") 

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
# 2. Lihat produk
    if choice == '2':
        barang = input("Masukkan nama barang yang ingin ditambahkan: ").capitalize()
        harga = int(input("Masukkan harga dari barang tersebut: "))
        stok = int(input("Masukkan jumlah stok dari barang yang ditambahkan: "))
        
        tambah_produk(nama = barang, harga = harga, stok = stok)
        
# ========================================================================================================
# 3. Cari dan ubah produk
    if choice == '3':
        cari_produk()

        
        
        
        
