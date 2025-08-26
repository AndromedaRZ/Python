# Program mini kasir menggunakan dictionary

import os
import sys
import time

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

keranjang = []

title = 'MENU KASIR'

while True:
    print("")
    print('╌' * (len(title) + 6))
    print(f"{title:^16}")
    print('╌' * (len(title) + 6))
    print('''1) Lihat Daftar Produk
2) Tambah ke Keranjang
3) Lihat Keranjang
4) Checkout
5) Keluar ''')
    choice = input("Pilih menu [1-5]: ")

    if choice == "":
        print("Masukan pilihan yang benar!")

# =============================================================
# Jika user ingin melihat daftar produk yang ingin dibeli    
    elif choice == '1':
        # print('\n┌──────┬──────────────────┬────────────────┐')
        print("╌"*37)
        print(f'{"KODE":^6} {"NAMA BARANG":<15} {"HARGA BARANG":<13}') 
        print("╌"*37)
        # print('├──────┼──────────────────┼────────────────┤')

        for kode, produk in data_produk.items():
            KEY = kode
            NAMA = data_produk[KEY]['nama']
            HARGA = data_produk[KEY]['harga']
            print(f'{kode:^6} {NAMA:<15} Rp {HARGA:,}')
        print("╌"*37)
        # print('└──────┴──────────────────┴────────────────┘') 

# =============================================================
# Jika user ingin menambah barang ke keranjang belanjaannya
    elif choice == '2':
        check_kode = input("Masukan kode barang yang ingin dibeli: ")
        if check_kode in data_produk:
            print("\nBarang ditemukan!")
            print('╌'*20)
            NAMA = data_produk[check_kode]['nama']
            HARGA = data_produk[check_kode]['harga']
            print(f'Nama  : {NAMA}')
            print(f'Harga : {HARGA}')
            print('╌'*20)
            
            jumlah = int(input("Masukan jumlah barang yang ingin dibeli: "))
            
            # membuat dictionary sementara bernama 'item' untuk mengumpulkan data belanjaan seperti kode, nama barang, harga barang, jumlah barang yang dibeli, dan harga total barang yang ingin dibeli user
            item = {
                'kode': check_kode,
                'nama': data_produk[check_kode]['nama'],
                'harga': data_produk[check_kode]['harga'],
                'jumlah': jumlah,
                'total': data_produk[check_kode]['harga'] * jumlah
            }
            
            keranjang.append(item) # memasukan data barang belanjaan dari dictionary 'item' ke list kosong bernama 'keranjang
            
            print(f'{jumlah} {data_produk[check_kode]['nama']} berhasil ditambahkan ke keranjang.')
            
        else:
            print("Barang dengan kode tersebut tidak ada")
# =============================================================
# Jika user ingin melihat keranjang belanjaannya    
    elif choice == '3':
        if keranjang == []:
            print("Keranjang belanja anda masih kosong!")
            
        else:    
            print('╌'*42)
            print(f'{'NAMA':<14} {'HARGA':<8} {'JUMLAH':<3} {'TOTAL':<10}')
            print('╌'*42)
            for item in keranjang:
                print(f"{item['nama']:<14} Rp {item['harga']:<6,} {item['jumlah']:<5} Rp {item['total']:<11,}") 
            print('╌'*42)
        
        
    
# =============================================================
# Jika user ingin memutuskan membeli barang yang sudah terkumpul di dalam keranjang belanjaannya  
    elif choice == '4':
        if keranjang == []:
            print("Keranjang belanja anda masih kosong!")
        
        else:
            checkout_confirm = input("Apakah anda yakin ingin checkout? [y/n]: ")
            
            if checkout_confirm == 'n':
                print('>>> Kembali ke Menu Utama')
                
            elif checkout_confirm == 'y':
                loading = "|/-\\"
                for i in range(20):  # jumlah putaran animasi
                    time.sleep(0.3)  # kecepatan animasi
                    sys.stdout.write("\r" + "Menghitung belanjaan anda " + loading[i % len(loading)])
                    sys.stdout.flush()

                print('\n')
                # tabel struk belanjaan
                print('┌────────────────────────────────────────────────┐')
                print(f'│ {"STRUK BELANJA":^46} │')
                print('├────────────────────────────────────────────────┤')
                print(f'│ {"NAMA BARANG":<15} {"HARGA":<10} {"JUMLAH":<8} {"TOTAL":<11}│')
                total_belanja = 0
                for item in keranjang:
                    print(f'│ {item["nama"]:<15} Rp {item["harga"]:<6,} {item["jumlah"]:^8}  Rp {item["total"]:<8,}│')
                    total_belanja += item["total"]
                print('├────────────────────────────────────────────────┤')
                print(f'│ {"TOTAL BELANJA:":<34}  Rp {total_belanja:<8,}│')
                print('└────────────────────────────────────────────────┘')
                
                print('\nKeranjang anda telah dikosongkan kembali')
                keranjang.clear()
                time.sleep(1)
                print("Terima kasih telah berbelanja :)")
                
            else:
                print("Masukan pilihan yang benar!")
    
# Jika user memilih untuk keluar dari menu kasir
    elif choice == '5':
        break

    else:
        print("Masukan pilihan yang benar!")
        
print('Selamat tinggal!')
