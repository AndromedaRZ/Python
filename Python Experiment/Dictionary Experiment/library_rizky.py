# Program sistem perpustakaan mini

from datetime import date
import os, random, string, time, json, datetime

os.system("clear")

rak_buku = {}
data_peminjaman = {}

with open("data_perpustakaan_rizky.json", "r") as file:
    data = json.load(file)
    rak_buku.update(data)

with open("data_peminjaman_rizky.json", "r") as file:
    data = json.load(file)
    data_peminjaman.update(data)

title = "│ SELAMAT DATANG DI PERPUSTAKAAN RIZKY │"

print(f"┌{'─'*(len(title) - 2)}┐")
print(title)
print(f"└{'─'*(len(title) - 2)}┘")
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
6) Lihat Data Peminjaman
7) Pinjam Buku
8) Kembalikan Buku
9) Keluar''')
    choice = input("Pilih Menu [1-9]: ")

# =======================================================================
# Jika user memilih untuk melihat daftar buku yang tersedia di rak perpustakaan
    if choice == "1":
        if rak_buku == {}: # jika rak buku masih kosong, maka user akan diperingatkan dengan kalimat di bawah ini
            print("\n┌─────────────────────────────┐")
            print("│ Rak buku anda masih kosong! │")
            print("└─────────────────────────────┘")
        else: # jika rak buku ada isinya, maka program di bawah ini akan berjalan dan menampilkan semua buku yang tersedia di rak perpustakaan
            title = f"│ {'NO':<3} {'KODE':<6} {'JUDUL BUKU':<25} {'NAMA PENULIS':<20} {'STOK TOTAL':<12} {'STOK TERSEDIA':<12} │"
            print(f"\n┌{'─'*(len(title) - 2)}┐")
            print(title)
            print(f"├{'─'*(len(title) - 2)}┤")
            for i, KEY in enumerate(rak_buku):
                JUDUL = rak_buku[KEY]['judul']
                NAMA = rak_buku[KEY]['penulis']
                TOTAL = rak_buku[KEY]['total']
                STOK = rak_buku[KEY]['stok']
                print(f"│ {i+1:<3} {KEY:<6} {JUDUL:<25} {NAMA:<24} {TOTAL:<12} {STOK:<9} │")
            print(f"└{'─'*(len(title) - 2)}┘")
            
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
            for key, value in rak_buku.items():
                if keyword in value['judul'] or keyword in value['penulis']: # memeriksa setiap keyword atau kata kunci yang cocok di dalam rak buku
                    hasil_cari.append(key) # menyimpan semua kode buku (semua data bukunya seperti nama, penulis, dan stoknya) ke dalam list sementara bernama 'hasil_cari'
            if hasil_cari: # jika sudah ada buku yang cocok dengan keyword atau kata kunci user, maka kode di bawah ini akan menampilkan seluruh buku yang sesuai
                title = f"│ {'NO':<3} {'KODE':<6} {'JUDUL BUKU':<25} {'NAMA PENULIS':<20} {'STOK TOTAL':<12} {'STOK TERSEDIA':<12} │"
                print(f"\n┌{'─' * (len(title) - 2)}┐")
                print(title)
                print(f"├{'─' * (len(title) - 2)}┤")
                for i, KEY in enumerate(hasil_cari):
                    JUDUL = rak_buku[KEY]['judul']
                    NAMA = rak_buku[KEY]['penulis']
                    TOTAL = rak_buku[KEY]['total']
                    STOK = rak_buku[KEY]['stok']
                    print(f"│ {i+1:<3} {KEY:<6} {JUDUL:<25} {NAMA:<24} {TOTAL:<12} {STOK:<9} │")
                print(f"└{'─' * (len(title) - 2)}┘")
            else: # jika tidak ada buku yang cocok dengan keyword atau kata kunci yang dimasukan user
                print("\n┌───────────────────────┐")
                print("│ Buku tidak ditemukan! │")
                print("└───────────────────────┘")
                
        
# =======================================================================
# Jika user memilih untuk menambah buku baru ke rak perpustakaan
    elif choice == "3":
        rak_sementara = {} # dictionary untuk menyimpan data sementara sebelum dimasukan ke dictionary utama
        
        rak_sementara['judul'] = input("Masukan nama buku: ").title() # membuat key baru dengan nama 'judul' dan meminta user untuk memasukan value atau nilainya
        rak_sementara['penulis'] = input("Masukan nama penulis: ").title() # membuat key baru dengan nama 'penulis' dan meminta user untuk memasukan value atau nilainya
        
        # cek apakah buku yang dimasukan user sudah ada atau belum
        buku_berbeda = False # dummy variable, akan menjadi True jika buku yang ingin user ditambahkan sudah ada di rak buku dan user tidak bisa menambahkan buku yang sebelumnya sudah ada tersebut
        for key, value in rak_buku.items():
            if rak_sementara['judul'] in value['judul'] and rak_sementara['penulis'] in value['penulis']:
                buku_berbeda = True
                break
        
        if buku_berbeda:
            print("\n┌─────────────────────────────────┐")
            print("│ Buku tersebut sudah ada di rak! │")
            print("└─────────────────────────────────┘")
        
        else:
            rak_sementara['total'] = int(input("Masukan stok yang tersedia: ")) # membuat key baru dengan nama 'total' dan meminta user untuk memasukan value atau nilainya
            rak_sementara['stok'] = rak_sementara['total'] # membuat key baru dengan nama 'stok' dan menyalin nilai atau value dari key 'total'
            
            KEY = 'B' + ''.join(random.choices(string.digits, k = 3)) # mengenerate kode random yang dimulai dari huruf "B" dengan total kode sebanyak 4 digit dan menjadikannya key unik
                            
            rak_buku[KEY] = rak_sementara.copy() # menyimpan salinan data dictionary 'rak_sementara' ke dictionary utama bernama 'rak_buku'
                            
            JUDUL = rak_buku[KEY]['judul']

            # menampilkan pesan buku yang sudah ditambahkan 
            title = f"│ Buku '{JUDUL}' berhasil ditambahkan dengan kode: {KEY} │"
            print(f"\n┌{'─' * (len(title) - 2)}┐")
            print(title)
            print(f"└{'─' * (len(title) - 2)}┘")

# =======================================================================
# Jika user memilih untuk mengubah data buku dari rak perpustakaan
    elif choice == "4":
        if rak_buku == {}: # jika rak buku masih kosong, maka user akan diperingatkan dengan kalimat di bawah ini
            print("\n┌─────────────────────────────┐")
            print("│ Rak buku anda masih kosong! │")
            print("└─────────────────────────────┘")
        else: # jika rak buku ada isinya, maka program di bawah ini akan berjalan
            ubah_buku = input("Masukan kode buku yang ingin anda ubah: ").capitalize()
            if ubah_buku not in rak_buku: # jika kode yang dimasukan user tidak ada di rak buku
                print("\n┌───────────────────────┐")
                print("│ Buku tidak ditemukan! │")
                print("└───────────────────────┘")
            else: # jika kode yang dimasukan user sama dengan yang ada di rak buku
                while True:
                    title = f"│ {'KODE':<6} {'JUDUL BUKU':<25} {'NAMA PENULIS':<20} {'STOK TOTAL':<12} {'STOK TERSEDIA':<12} │"
                    print(f"\n┌{'─' * (len(title) - 2)}┐")
                    print(title)
                    print(f"├{'─' * (len(title) - 2)}┤")
                    
                    JUDUL = rak_buku[ubah_buku]['judul']
                    NAMA = rak_buku[ubah_buku]['penulis']
                    TOTAL = rak_buku[ubah_buku]['total']
                    STOK = rak_buku[ubah_buku]['stok']
                    print(f"│ {ubah_buku:<6} {JUDUL:<25} {NAMA:<24} {TOTAL:<12} {STOK:<9} │")
                    print(f"└{'─' * (len(title) - 2)}┘")
                
                    print('''\n1) Judul Buku
2) Nama Penulis
3) Stok Total
4) Keluar''')
                    choice2 = input("Apa yang ingin anda ubah? [1/2/3/4]: ")

                    if choice2 == '1':
                        judul_baru = input("Masukan judul baru: ").title()
                        rak_buku[ubah_buku]['judul'] = judul_baru
                        
                        title = "│ Judul buku berhasil diubah │"
                        print(f"\n┌{'─'*(len(title) - 2)}┐")
                        print(title)
                        print(f"└{'─'*(len(title) - 2)}┘")
                             
                    elif choice2 == '2': 
                        nama_baru = input("Masukan nama penulis baru: ").title()
                        rak_buku[ubah_buku]['penulis'] = nama_baru
                        
                        title = "│ Nama penulis berhasil diubah │"
                        print(f"\n┌{'─'*(len(title) - 2)}┐")
                        print(title)
                        print(f"└{'─'*(len(title) - 2)}┘")
                
                    elif choice2 == '3':
                        if rak_buku[ubah_buku]['total'] > rak_buku[ubah_buku]['stok']:  # jika stok total lebih sedikit dari stok yang tersedia, maka stok total tidak bisa diubah
                            title = "│ Stok buku tidak dapat diperbarui! │"
                            print(f"\n┌{'─'*(len(title) - 2)}┐")
                            print(title)
                            print(f"└{'─'*(len(title) - 2)}┘")
                        
                        else:
                            stok_terbaru = int(input("Masukan stok terbaru: "))
                            stok = rak_buku[ubah_buku]['total']
                            rak_buku[ubah_buku]['total'] = stok_terbaru
                            rak_buku[ubah_buku]['stok'] = rak_buku[ubah_buku]['total'] # jika jumlah stok total berubah, maka stok tersedia juga akan mengikuti jumlah stok total
                            
                            title = "│ Stok buku berhasil diperbarui │"
                            print(f"\n┌{'─'*(len(title) - 2)}┐")
                            print(title)
                            print(f"└{'─'*(len(title) - 2)}┘")
                
                    elif choice2 == '4':
                        print("\n┌───────────────────────┐")
                        print("│ Kembali ke menu utama │")
                        print("└───────────────────────┘")
                        break

# =======================================================================
# Jika user memilih untuk menghapus buku dari rak perpustakaan
    elif choice == "5":
        if rak_buku == {}: # jika rak buku masih kosong, maka user akan diperingatkan dengan kalimat di bawah ini
            print("\n┌─────────────────────────────┐")
            print("│ Rak buku anda masih kosong! │")
            print("└─────────────────────────────┘")
        
        else:
            hapus_buku = input("Masukan kode buku yang ingin dihapus: ").capitalize()
            if hapus_buku not in rak_buku: # jika kode yang dimasukan user tidak ada di rak buku
                    print("\n┌───────────────────────┐")
                    print("│ Buku tidak ditemukan! │")
                    print("└───────────────────────┘")
            
            elif rak_buku[hapus_buku]['total'] > rak_buku[hapus_buku]['stok']:
                        title = f"│ Buku tersebut sedang dipinjam! │"
                        print(f"\n┌{'─'*(len(title) - 2)}┐")
                        print(title)
                        print(f"└{'─'*(len(title) - 2)}┘")
                        
            else:
                konfirmasi = input(f"Apakah anda yakin ingin menghapus buku '{rak_buku[hapus_buku]['judul']}'? [y/n]: ")
                if konfirmasi == 'n':
                    print("\n┌───────────────────────┐")
                    print("│ Kembali ke menu utama │")
                    print("└───────────────────────┘")
                elif konfirmasi == 'y':    
                    title = f"│ Data buku '{rak_buku[hapus_buku]['judul']}' berhasil dihapus │"
                    print(f"\n┌{'─'*(len(title) - 2)}┐")
                    print(title)
                    print(f"└{'─'*(len(title) - 2)}┘")
                    del rak_buku[hapus_buku]
                    
# =======================================================================
# Jika user memilih untuk melihat data buku yang dipinjam dari perpustakaan
    elif choice == "6":
        if data_peminjaman == {}:
            title = f"│ Belum ada buku yang dipinjam! │"
            print(f"\n┌{'─'*(len(title) - 2)}┐")
            print(title)
            print(f"└{'─'*(len(title) - 2)}┘")
        else:
            title = f"│ {'NO':<3} {'KODE':<5} {'NAMA PEMINJAM':<15} {'JUDUL DAN PENULIS':<45} {'DIPINJAM':^11} {'KEMBALI':^11} {'STATUS':^13} │"
            print(f"\n┌{'─'*(len(title) - 2)}┐")
            print(title)
            print(f"├{'─' * (len(title) - 2)}┤")
            
            for i, KEY in enumerate(data_peminjaman):
                nama = data_peminjaman[KEY]['nama']
                judul = data_peminjaman[KEY]['judul']
                penulis = data_peminjaman[KEY]['penulis']
                judul_penulis = [judul, penulis]
                judul_penulis = f"{judul_penulis[0]} oleh {judul_penulis[1]}"
                
                waktu = data_peminjaman[KEY]['waktu']
                kembali = data_peminjaman[KEY]['kembali']
                status = data_peminjaman[KEY]['status']
                
                print(f"│ {i+1:<3} {KEY:<5} {nama:<15} {judul_penulis:<45} {waktu:^11} {kembali:^11} {status:^13} │")
            print(f"└{'─' * (len(title) - 2)}┘")   
            
# =======================================================================
# Jika user memilih untuk meminjam buku dari perpustakaan
    elif choice == "7":
        if rak_buku == {}: # jika rak buku masih kosong, maka user akan diperingatkan dengan kalimat di bawah ini
            print("\n┌─────────────────────────────┐")
            print("│ Rak buku anda masih kosong! │")
            print("└─────────────────────────────┘")
        else:
            dipinjam = input("Masukan kode buku yang ingin dipinjam: ").capitalize()
            if dipinjam not in rak_buku: # jika kode yang dimasukan user tidak ada di rak buku
                    print("\n┌───────────────────────┐")
                    print("│ Buku tidak ditemukan! │")
                    print("└───────────────────────┘")
                    
            elif rak_buku[dipinjam]['stok'] < 1:
                title = f"│ Stok buku '{rak_buku[dipinjam]['judul']}' sedang tidak tersedia! │"
                print(f"\n┌{"─"*(len(title) - 2)}┐")
                print(title)
                print(f"└{"─"*(len(title) - 2)}┘")
            
            else:
                konfirmasi = input(f"Ingin meminjam buku '{rak_buku[dipinjam]['judul']}'? [y/n]: ")
                if konfirmasi == 'n':
                    print("\n┌───────────────────────┐")
                    print("│ Kembali ke menu utama │")
                    print("└───────────────────────┘")
                elif konfirmasi == 'y':
                    peminjaman_sementara = {} # dictionary untuk menyimpan data sementara sebelum dimasukan ke dictionary utama sebagai data peminjaman
                    
                    waktu_saat_ini = datetime.datetime.now() # mengambil waktu saat ini untuk digunakan sebagai tanggal peminjaman
                    
                    nama_peminjam = input("Masukan nama peminjam: ").title()
                    
                    if dipinjam in data_peminjaman and nama_peminjam in data_peminjaman[dipinjam]['nama'] and data_peminjaman[dipinjam]['status'] == 'dipinjam':
                        title = f"│ Buku tersebut masih anda pinjam! │"
                        print(f"\n┌{"─"*(len(title) - 2)}┐")
                        print(title)
                        print(f"└{"─"*(len(title) - 2)}┘")
                    else:
                        
                        KEY = 'B' + ''.join(random.choices(string.digits, k = 3)) # mengenerate kode random yang dimulai dari huruf "B" dengan total kode sebanyak 4 digit dan menjadikannya key unik
                        
                        peminjaman_sementara = {
                            "kode": dipinjam,
                            "nama": nama_peminjam, 
                            "judul": rak_buku[dipinjam]['judul'],
                            "penulis": rak_buku[dipinjam]['penulis'],
                            "waktu": waktu_saat_ini.strftime('%d/%m/%Y'),
                            "kembali": '-',
                            "status": 'dipinjam'
                        } # dicionary peminjaman sementara ini akan mengambil semua data seperti judul buku dan nama penulis buku yang dipinjam user dari rak buku
                        
                        
                        
                        rak_buku[dipinjam]['stok'] -= 1 # mengurangi stok buku yang tersedia dari rak buku karena bukunya sedang dipinjam
                        
                        data_peminjaman[KEY] = peminjaman_sementara.copy() # menyalin data peminjaman buku sementara ke data peminjaman buku utama yang sudah ada key uniknya
                        
                        title = f"│ Buku '{rak_buku[dipinjam]['judul']}' berhasil dipinjam │"
                        print(f"\n┌{"─"*(len(title) - 2)}┐")
                        print(title)
                        print(f"└{"─"*(len(title) - 2)}┘")

# =======================================================================
# Jika user memilih untuk mengembalikan buku yang dipinjam dari perpustakaan
    elif choice == "8":
        dikembalikan = input("Masukan kode buku yang ingin anda kembalikan: ").capitalize()

        if dikembalikan in data_peminjaman and data_peminjaman[dikembalikan]['status'] == 'dipinjam': # memeriksa apakah kode buku yang dimasukan oleh peminjam buku sama dengan yang ada di daftar peminjaman dan status buku tersebut juga sedang dipinjam
            nama_peminjam = input("Masukan nama peminjam: ").title()
            
            if nama_peminjam in data_peminjaman[dikembalikan]['nama'] and data_peminjaman[dikembalikan]['status'] == 'dipinjam': # memeriksa apakah nama peminjam yang dimasukan oleh pemnjam ada di dalam daftar peminjaman dan status buku tersebut juga sedang dipinjam 
                data_peminjaman[dikembalikan]['status'] = 'dikembalikan'
                
                KEY = data_peminjaman[dikembalikan]['kode']
                rak_buku[KEY]['stok'] += 1
                
                data_peminjaman[dikembalikan]['kembali'] = date.today().strftime('%d/%m/%Y')
                
                title = f"│ Buku '{data_peminjaman[dikembalikan]['judul']}' berhasil dikembalikan │"
                print(f"\n┌{"─"*(len(title) - 2)}┐")
                print(title)
                print(f"└{"─"*(len(title) - 2)}┘")
                
            else:
                title = f"│ Nama tersebut bukan peminjam bukunya! │"
                print(f"\n┌{"─"*(len(title) - 2)}┐")
                print(title)
                print(f"└{"─"*(len(title) - 2)}┘")
                
        else:
            title = f"│ Buku tersebut bukan yang dipinjam! │"
            print(f"\n┌{"─"*(len(title) - 2)}┐")
            print(title)
            print(f"└{"─"*(len(title) - 2)}┘")

# =======================================================================
# Jika user memilih untuk keluar dari sistem perpustakaan
    elif choice == "9":
        with open("data_perpustakaan_rizky.json", "w") as file:
            json.dump(rak_buku, file, indent=4)
            
        with open("data_peminjaman_rizky.json", "w") as file:
            json.dump(data_peminjaman, file, indent=4)
            
        exit()

            

