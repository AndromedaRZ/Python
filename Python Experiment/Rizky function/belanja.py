# Program mini kasir toko elektronik menggunakan function

import time, sys, os
os.system("clear")

data_barang = {
    "B001":{'nama':'blender', 'harga':400000},
    "B002":{'nama':'kipas angin', 'harga':250000},
    "B003":{'nama':'setrika', 'harga':150000},
    "B004":{'nama':'kulkas mini', 'harga':500000},
    "B005":{'nama':'mesin cuci', 'harga':800000},
    "B006":{'nama':'penanak nasi', 'harga':300000},
    "B007":{'nama':'televisi led', 'harga':1500000},
    "B008":{'nama':'mixer', 'harga':500000},
    "B009":{'nama':'kamera digital', 'harga':2000000},
    "B010":{'nama':'microwave', 'harga':750000},
}

keranjang = []

'''
penjelasan dictionary data barang
'B001' adalah key unik dari dictionarynya
'nama' dan 'harga' adalah key dari nested dictionary yang juga memiliki valuenya
ketika user ingin memilih sebuah barang, maka hanya perlu memanggil kode produknya atau key uniknya
'''

# kumpulan fungsi setiap aksinya

# menampilkan daftar barang yang dijual ( 1 )
def display():
    '''fungsi untuk menampilkan seluruh barang yang dijual'''
    print("╌"*37)
    print(f'{"KODE":^6} {"NAMA BARANG":<15} {"HARGA BARANG":<13}') 
    print("╌"*37)
    for kode, produk in data_barang.items():
        KEY = kode
        NAMA = data_barang[KEY]['nama']
        HARGA = data_barang[KEY]['harga']
        print(f' {KEY:<6} {NAMA:<15} {HARGA:<13,}')
    print("╌"*37)


# memasukan barang ke dalam keranjang ( 2 )

def in_keranjang():
    '''fungsi untuk memasukan barang yang ingin dibeli ke dalam keranjang'''
    check_kode = input("Masukan kode barangnya: ")
    if check_kode not in data_barang:
        title = "Barang dengan kode tersebut tidak ada!"
        print("╌"*(len(title) + 2))
        print(title) 
        print("╌"*(len(title) + 2))
    else:
        print("Barang ditemukan!")
        print("╌"*20)
        print(f"Nama Barang  : {data_barang[check_kode]['nama']}")
        print(f"Harga Barang : {data_barang[check_kode]['harga']}")
        print("╌"*20)
        
        jumlah = int(input("Ingin beli berapa unit?: "))
        
        # membuat dictionary sementara untuk memasukan data barang yang ingin dimasukan ke dalam keranjan
        print(f'{jumlah} unit {data_barang[check_kode]['nama']} berhasil ditambahkan ke keranjang')
        
        return {
            'kode': check_kode,
            'nama': data_barang[check_kode]['nama'],
            'harga': data_barang[check_kode]['harga'],
            'jumlah': jumlah,
            'total': data_barang[check_kode]['harga'] * jumlah
        }
    
        
        
# melihat isi keranjang
def keranjang():
     print(keranjang)

title = "│ SELAMAT DATANG DI TOKO ELEKTRONIK │"
print(f"┌{'─'*(len(title) - 2)}┐")
print(title)
print(f"└{'─'*(len(title) - 2)}┘")
    
while True:
    title = " MENU BELANJA "
    print("-" * (len(title) + 4))
    print(f"{title:^18}")
    print("-" * (len(title) + 4))
    print('''1) Lihat Daftar Barang
2) Tambah ke Keranjang
3) Lihat Keranjang
4) Lihat Ketentuan Diskon
5) Checkout
6) Keluar''')
    choice = input("Pilih Menu [1-6]: ")
    
# ========================================================================================================================================
# jika user memilih untuk melihat daftar barang yang dijual
    if choice == "1":
        display()

# ========================================================================================================================================
# jika user ingin menambah barang yang dipilih ke dalam keranjang
    if choice == "2":
        item = in_keranjang()
        keranjang.append()
    
# ========================================================================================================================================
# jika user ingin melihat barang yang telah dimasukan ke dalam keranjang
    if choice == "3":
        continue
    
# ========================================================================================================================================
# jika user ingin melihat ketentuan diskon yang berlaku
    if choice == "4":
        continue
    
# ========================================================================================================================================
# jika user ingin checkout semua barang yang ada di dalam keranjang
    if choice == "5":
        continue
    
# ========================================================================================================================================
# jika user ingin keluar dari program
    if choice == "6":
        continue