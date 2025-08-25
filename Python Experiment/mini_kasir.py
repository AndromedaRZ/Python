# Program mini kasir
import time

data_barang = {
    'A001':{'nama':'indomie','harga':3500},
    'A002':{'nama':'air mineral','harga':2000},
    'A003':{'nama':'roti','harga':5000},
    'A004':{'nama':'teh kotak','harga':4000},
    'A005':{'nama':'biskuit','harga':3000},
    'A006':{'nama':'susu kotak','harga':4000},
    'A007':{'nama':'teh','harga':500},
    'A008':{'nama':'kopi','harga':2000},
    'A009':{'nama':'sabun','harga':2500},
    'A010':{'nama':'es krim','harga':3000}
}

keranjang = [] # list kosong ini berfungsi untuk menyimpan semua belanjaan yang kita pilih dan nantinya akan dijumlahkan kemudian

# penjelasan dictionary data barang
# 'A001' adalah key dictionary-nya
# 'nama' dan 'harga' adalah key dari nested dictionary yang juga memiliki value
# jadi ketika kita ingin mengambil data di dalam dictionary, kita juga harus mengambil KEY dictionary-nya terlebih dahulu (yang A001)

while True:
    title = f"{'Kode':<6} {'Nama barang':<14} {'harga':<7}"

    print('-'*len(title))
    print(title)
    print('-'*len(title))

    for i in data_barang:
        KEY = i # setiap urutan data yang ada di dalam dict data_barang kita definisikan dengan i, dan i-nya dimasukkan ke dalam constant KEY
        # nah, KEY ini sebagai kode dari setiap nested dict di dalamnya 'A001', 'A002' dan seterusnya
        NAMA = data_barang[KEY]['nama'] # jadi, KEY berfungsi untuk memunculkan value dari 'key' bernama 'nama'
        HARGA = data_barang[KEY]['harga'] #  dan KEY berfungsi untuk memunculkan value dari 'key' bernama 'harga'
        # 'nama' dan 'harga' juga merupakan key dari nested dictionary di dalamnya
        
        print(f"{KEY:<6} {NAMA:<14} {HARGA:,}") # kita memunculkan outputnya menggunakan constantnya
        # KEY untuk memunculkan key dari dictionarynya
        # NAMA untuk memunculkan key dari nested dictionary di dalam KEY
        # HARGA untuk memunculkan key dari nested dictionary di dalam KEY
        
    print('-'*len(title))
    beli_barang = input("Masukkan kode barang yang ingin dibeli: ")
    # baris di atas kita meminta user memasukkan kode barang yang mana kode barang adalah KEY dari dictionarnya seperti 'A001'

    if beli_barang in data_barang: # maka kita mengecek apakah key tersebut ada atau tidak di dalam dictionary data_barang
        print("")
        print("Barang ditemukan!")
        print("-----------------") # jika ada, maka KEY terebut akan memunculkan key dan value dari nested dictionary yang dicari
        print(f"Nama : {data_barang[beli_barang]['nama']}") # data barang[][] adalah nama dictionary-nya
        print(f"Harga: {data_barang[beli_barang]['harga']}") # [beli barang][] adalah KEY dari dictionary-nya
        # dan ['nama'] dan ['harga'] adalah key dari nested dictionary-nya dan nantinya akan memunculkan value dari kedua key tersebut
        
        jumlah = int(input("Ingin beli berapa banyak? "))
        
        keranjang.append({ # .append() berguna untuk memasukkan perubahan yang terjadi pada input masuk ke dalam list keranjang
            'kode': beli_barang,
            'nama': data_barang[beli_barang]['nama'],
            'harga': data_barang[beli_barang]['harga'],
            'jumlah': jumlah,
            'subtotal': data_barang[beli_barang]['harga'] * jumlah
        })
        print(f"{jumlah} {data_barang[beli_barang]['nama']} telah dimasukkan ke keranjang.")
        
        konfirmasi = input("Apakah masih ingin berbelanja? (y/n): ").lower()
        if konfirmasi == 'n':
            break
        
    else:
        print('Kode barang tidak ditemukan')
    

for anim in ["-", "\\", "|", "/", "-", "\\", "--", "--"]:
    print(f"\rMenghitung belanjaan {anim}  ", end='', flush=True)
    time.sleep(0.2)
print()

total = 0
for item in keranjang:
    total += item['subtotal']
    
print("┌────────────────────────────────────────┐")
print("│            Daftar belanjaan            │")
print("├────────────────────────────────────────┤")
print(f"│ {'Nama':<12} {'Harga':<7} {'Jumlah':<6} {'Subtotal':<10} │")
for item in keranjang:
    print(f"│ {item['nama']:<12} {item['harga']:<7} {item['jumlah']:^6} {item['subtotal']:<10} │")
    
print("├────────────────────────────────────────┤")
print(f"│ {'Total belanja':<26}: {total:<10} │")
print("└────────────────────────────────────────┘")