# Program mini kasir menggunakan dictionary

import os

os.system("clear")

data_produk = {
        'A001':{'nama':'indomie', 'harga':3500},
        'A002':{'nama':'kopi sachet', 'harga':2000},
        'A003':{'nama':'susu sachet', 'harga':1500},
        'A004':{'nama':'teh sachet', 'harga':2500},
        'A005':{'nama':'roti', 'harga':2000},
        'A006':{'nama':'shampo sachet', 'harga':500},
        'A007':{'nama':'sabun mandi', 'harga':3000},
        'A008':{'nama':'tisu kotak', 'harga':6000},
        'A009':{'nama':'susu jahe', 'harga':3500},
        'A010':{'nama':'air mineral', 'harga':2000},
        }


while True:
    print('''=== MENU KASIR ===
1) Lihat Daftar Produk
2) Tambah ke Keranjang
3) Lihat Keranjang
4) Checkout
5) Keluar ''')
    choice = input("Pilih menu [1-5]: ")

    if choice == "":
        print("Masukan pilihan yang benar!")
    
    elif choice == '1':

        print('┌──────┬────────────────────────────────┐')
        print(f'│{"KODE":^6}│{"NAMA BARANG":<10}│{"HARGA BARANG":<20}') 
        print('├──────┼──────────┼──────────────────────┤')

        for kode, produk in data_produk.items():
            KEY = kode
            NAMA = data_produk[KEY]['nama']
            HARGA = data_produk[KEY]['harga']
            print(f'│{KEY:^6}. {NAMA:<10} - Rp{HARGA:<20}│')
        print('└───────────────────────────────────────┘') 

    elif choice == '5':
        break

    else:
        print("Masukan pilihan yang benar!")
