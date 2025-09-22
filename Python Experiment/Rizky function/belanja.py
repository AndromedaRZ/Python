# Program mini kasir toko elektronik menggunakan function

import time, sys, os
os.system("clear")

data_barang = {
    "B001":{'nama':'Blender', 'harga':400000},
    "B002":{'nama':'Kipas angin', 'harga':250000},
    "B003":{'nama':'Setrika', 'harga':150000},
    "B004":{'nama':'Kulkas mini', 'harga':500000},
    "B005":{'nama':'Mesin cuci', 'harga':800000},
    "B006":{'nama':'Penanak nasi', 'harga':300000},
    "B007":{'nama':'Televisi led', 'harga':1500000},
    "B008":{'nama':'Mixer', 'harga':500000},
    "B009":{'nama':'Kamera digital', 'harga':2000000},
    "B010":{'nama':'Microwave', 'harga':750000},
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
        print(f' {KEY:<6} {NAMA:<14} Rp{HARGA:<11,}')
    print("╌"*37)


# memasukan barang ke dalam keranjang ( 2 )
def in_keranjang():
    '''fungsi untuk memasukan barang yang ingin dibeli ke dalam keranjang'''
    check_kode = input("Masukan kode barangnya: ")
    if check_kode not in data_barang:
        title = "│ Barang dengan kode tersebut tidak ada! │"
        print(f"\n┌{"─"*(len(title) - 2)}┐")
        print(title)
        print(f"└{"─"*(len(title) - 2)}┘")
    else:
        print("\nBarang ditemukan!")
        print("╌"*30)
        print(f"Nama Barang  : {data_barang[check_kode]['nama']}")
        print(f"Harga Barang : {data_barang[check_kode]['harga']}")
        print("╌"*30)
        
        jumlah = int(input("\nIngin beli berapa unit?: "))

        item = {
            'kode' : check_kode,
            'nama' : data_barang[check_kode]['nama'],
            'harga' : data_barang[check_kode]['harga'],
            'jumlah' : jumlah,
            'total' : data_barang[check_kode]['harga'] * jumlah,
        }

        keranjang.append(item)
        
        print(f'{jumlah} unit {data_barang[check_kode]['nama']} berhasil ditambahkan ke keranjang')
        
# melihat isi keranjang ( 3 )
def isi_keranjang():
    if not keranjang:
        title = "│ Keranjang belanja anda masih kosong │"
        print(f"\n┌{"─"*(len(title) - 2)}┐")
        print(title)
        print(f"└{"─"*(len(title) - 2)}┘")
    else:
        title = f"│ {'NO':<3} {'Nama Barang':<15} {'Harga':<15} {'Jumlah':<10} {'Total':<15} │"
        print(f"\n┌{"─"*(len(title) - 2)}┐")
        print(title)
        print(f"├{"─"*(len(title) - 2)}┤")
        for i, item in enumerate(keranjang):
            print(f"│ {i+1:<3} {item['nama']:<15} Rp{item['harga']:<15,} {item['jumlah']:<8} Rp{item['total']:<13,} │")
        print(f"└{"─"*(len(title) - 2)}┘")
        
        
        
     
     
# melihat ketentuan diskon ( 4 )
def display_diskon():
    '''menampilkan aturan diskon kepada user'''
    print()
    print("╌"*45)
    print(f'{'KETENTUAN DISKON':^45}')
    print("╌"*45)
    print("* Belanja <= Rp 500,000   = Tidak ada diskon")
    print("* Belanja >= Rp 1,500,000 = Diskon 3%")
    print("* Belanja >= Rp 3,000,000 = Diskon 5%")
    print("* Belanja >= Rp 7,000,000 = Diskon 8%")
    print("╌"*45)


# fungsi diskon
def hitung_diskon(total):
    '''fungsi diskon saat checkout'''
    if total >= 7000000:
        diskon = 0.08
    elif total >= 3000000:
        diskon = 0.05
    elif total >= 1500000:
        diskon = 0.03
    else:
        diskon = 0.0
    
    potongan = total * diskon
    total_setelah_diskon = total - potongan
    return diskon, total_setelah_diskon
        
# fungsi checkout ( 5 )
def checkout():
    if not keranjang:
        title = "│ Keranjang belanja anda masih kosong │"
        print(f"\n┌{"─"*(len(title) - 2)}┐")
        print(title)
        print(f"└{"─"*(len(title) - 2)}┘")
    else:
        confirm = input("Konfirmasi Checkout? [y/n]: ")
        if confirm == "y":
            loading = "|/-\\"
            for i in range(20):  # jumlah putaran animasi
                time.sleep(0.3)  # kecepatan animasi
                sys.stdout.write("\r" + "Menghitung belanjaan anda " + loading[i % len(loading)])
                sys.stdout.flush()
                
            print('\n')
            # tabel struk belanjaan
            title = f'│ {"STRUK BELANJA":^52} │'
            title2 = f'│ {"Nama barang":<15} {"Harga":<12} {"Jumlah":<8} {"Total":<15}│'
            print(f'┌{'─'*(len(title2) - 2)}┐')
            print(title)
            print(f'├{'─'*(len(title2) - 2)}┤')
            print(title2)
            total_belanja = 0
            
            
            for item in keranjang:
                print(f'│ {item["nama"]:<15} Rp{item["harga"]:<9,} {item["jumlah"]:^8}  Rp{item["total"]:<13,}│')
                total_belanja += item["total"]
            
            diskon, total_akhir = hitung_diskon(total_belanja)
            diskon = diskon*100
            
            print(f'├{'─'*(len(title2) - 2)}┤')
            print(f'│ {"Total belanja":<35} : Rp{total_belanja:<13,}│')
            print(f'│ {"Diskon":<35} : {int(diskon)}%{"":<12} │')
            print(f'│ {"Total setelah diskon":<35} : Rp{int(total_akhir):<13,}│')
            print(f'└{'─'*(len(title2) - 2)}┘')
            
            print('\nKeranjang anda telah dikosongkan kembali')
            keranjang.clear()
            time.sleep(1)
            print("Terima kasih telah berbelanja :)")
            
            return total_belanja
                
        elif confirm == "n":
            pass
        else:
            pass
        
        
title = "│ SELAMAT DATANG DI TOKO ELEKTRONIK │"
print(f"┌{'─'*(len(title) - 2)}┐")
print(title)
print(f"└{'─'*(len(title) - 2)}┘")
    
while True:
    title = " MENU BELANJA "
    print()
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
        in_keranjang()
    
# ========================================================================================================================================
# jika user ingin melihat barang yang telah dimasukan ke dalam keranjang
    if choice == "3":
        isi_keranjang()
    
# ========================================================================================================================================
# jika user ingin melihat ketentuan diskon yang berlaku
    if choice == "4":
        display_diskon()
    
# ========================================================================================================================================
# jika user ingin checkout semua barang yang ada di dalam keranjang
    if choice == "5":
        checkout()
    
# ========================================================================================================================================
# jika user ingin keluar dari program
    if choice == "6":
        break