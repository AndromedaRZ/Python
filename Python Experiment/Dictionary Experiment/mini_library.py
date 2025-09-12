# Perpustakaan mini

import string, random, json
from datetime import date

print('''┌─────────────────────────────┐
│  Program Perpustakaan Mini  │
└─────────────────────────────┘''')

peminjaman = {}

koleksi_buku = {}

# Saat program dijalankan, baca file JSON
with open("mini_library.json", "r") as f:
    data = json.load(f)
    koleksi_buku.update(data)   # pindahkan data JSON ke dictionary kosong

with open("data_peminjaman.json", "r") as f:
    data = json.load(f)
    peminjaman.update(data)

while True:
    rak_sementara = {}
    peminjaman_sementara = {}
    
    for peminjam in peminjaman:  
        KEY = peminjam
    
        if peminjaman[KEY]['tanggal kembali'] == None:
            peminjaman[KEY]['tanggal kembali'] = '-'
    
    print('''\n1) Lihat koleksi buku
2) Cari buku
3) Tambah buku baru
4) Ubah data buku
5) Hapus buku
6) Lihat data dan riwayat peminjaman buku
7) Pinjam buku
8) Kembalikan buku
9) Keluar''')
    choice = input("Apa yang ingin anda lakukan?: ")
    
# 1 ========================================================================================================================
# Baris kode untuk opsi meilhat koleksi buku    
    if choice == '1':
        if len(koleksi_buku) == 0:
            print("\n┌──────────────────────────────────┐")
            print("│ Belum ada buku yang ditambahkan! │")
            print("└──────────────────────────────────┘")
        else:
            title = f"│ {'Kode':<5} {'Judul':<20} {'Penulis':<20} {'Stok total':<11} {'Stok tersedia':<14} │"
            print(f'\n┌{"─" * (len(title) - 2)}┐')
            print(title)
            print(f'├{"─" * (len(title) - 2)}┤')
            for buku in koleksi_buku:
                KEY = buku
                JUDUL = koleksi_buku[KEY]['judul']
                PENULIS = koleksi_buku[KEY]['penulis']
                TOTAL = koleksi_buku[KEY]['stok total']
                TERSEDIA = koleksi_buku[KEY]['stok tersedia']
                print(f"│ {KEY:<5} {JUDUL:<20} {PENULIS:<20} {TOTAL:^11} {TERSEDIA:^14} │")
                
            print(f'└{"─" * (len(title) - 2)}┘')

# 2 ========================================================================================================================
# Baris kode untuk opsi mencari buku            
    elif choice == '2':
        if len(koleksi_buku) == 0:
            print("\n┌──────────────────────────────────┐")
            print("│ Belum ada buku yang ditambahkan! │")
            print("└──────────────────────────────────┘")
        else:
            cari_buku = input("Masukkan kata kunci seperti judul ataupun nama penulis dari buku yang dicari: ").title() # .title() digunakan untuk membuat huruf pertama dari setiap kata menjadi kapital, sehingga tidak perlu mengkhawatirkan case sensitive-nya
            hasil = [] # list kosong untuk menyimpan data ketika buku yang kita cari ketemu
            for kode, buku in koleksi_buku.items(): # mengambil setiap pasangan key (bukan KEY unik) dan value dari dictionary
                if cari_buku in buku['judul'].title() or cari_buku in buku['penulis'].title(): # mengecek apakah judul ataupun penulis ada di dalam koleksi buku, jika salah satu benar
                    hasil.append((kode, buku)) # maka data yang sama tadi dimasukkan ke dalam list 'hasil'
                    
            if hasil: # jika list hasil ini tidak kosong, maka sistem akan menampilkan semua data yang cocok (judul dan penulisnya serupa ataupun hampir serupa)
                title = f"│ {'Kode':<5} {'Judul':<20} {'Penulis':<20} {'Stok total':<11} {'Stok tersedia':<14} │"
                
                print("\nHasil pencarian:")
                print(f'┌{"─" * (len(title) - 2)}┐')
                print(title)
                print(f'├{"─" * (len(title) - 2)}┤')
                for kode, buku in hasil:
                    print(f"│ {kode:<5} {buku['judul']:<20} {buku['penulis']:<20} {buku['stok tersedia']:^11} {buku['stok total']:^14} │")
                
                print(f'└{"─" * (len(title) - 2)}┘')
            else:
                print("\n┌───────────────────────┐")
                print("│ Buku tidak ditemukan! │")
                print("└───────────────────────┘")

# 3 ========================================================================================================================
# Baris kode untuk opsi menambahkan buku baru          
    elif choice == '3':
        rak_sementara['judul'] = input("Masukkan judul buku: ").title()
        rak_sementara['penulis'] = input("Masukkan nama penulisnya: ").title()
        rak_sementara['stok total'] = int(input("Masukkan stok yang tersedia: "))
        rak_sementara['stok tersedia'] = rak_sementara['stok total']

        # Generate KEY unik untuk dijadikan kode buku
        KEY = "B" + "".join(random.choices(string.digits, k = 3))
        
        buku_sudah_ada = False # dummy variabel false
        for buku in koleksi_buku.values(): # untuk setiap value yang ada di dalam koleksi buku
            if rak_sementara['judul'] in buku['judul'] and rak_sementara['penulis'] in buku['penulis']: # jika judul buku yang baru di-input ada yang sama dengan buku di koleksi buku
                buku_sudah_ada = True # maka dummy variabel akan berubah menjadi True
            break

        if buku_sudah_ada == True: # lalu mengeksekusi baris ini
            print("\n┌────────────────────────────────────────────────┐")
            print("│ Buku tersebut sudah ada di dalam koleksi buku! │")
            print("└────────────────────────────────────────────────┘")
            continue
            
        koleksi_buku[KEY] = rak_sementara.copy() # untuk menyalin isi yang ada di rak_sementara ke dalam dictionary koleksi_buku dengan menambahkan KEY uniknya juga sesuai yang digenerate oleh sistem pada pembuatan KEY unik

# 4 ========================================================================================================================
# Baris kode untuk opsi mengubah data buku       
    elif choice == '4':
        if len(koleksi_buku) == 0:
            print("\n┌──────────────────────────────────┐")
            print("│ Belum ada buku yang ditambahkan! │")
            print("└──────────────────────────────────┘")
        else:
            title = f"│ {'Kode':<5} {'Judul':<20} {'Penulis':<20} {'Stok total':<11} {'Stok tersedia':<14} │"
            
            print(f'\n┌{"─" * (len(title) - 2)}┐')
            print(title)
            print(f'├{"─" * (len(title) - 2)}┤')
            for buku in koleksi_buku:
                KEY = buku
                JUDUL = koleksi_buku[KEY]['judul']
                PENULIS = koleksi_buku[KEY]['penulis']
                TOTAL = koleksi_buku[KEY]['stok total']
                TERSEDIA = koleksi_buku[KEY]['stok tersedia']
                print(f"│ {KEY:<5} {JUDUL:<20} {PENULIS:<20} {TOTAL:^11} {TERSEDIA:^14} │")
                
            print(f'└{"─" * (len(title) - 2)}┘')
            
            ubah_data = input("Masukkan kode buku yang ingin diubah: ")
            if ubah_data in koleksi_buku: # jika kode buku ada di dalam dictionary koleksi_buku, baris ini akan tereksekusi
                title = f"│ {'Kode':<5} {'Judul':<20} {'Penulis':<20} {'Stok total':<11} {'Stok tersedia':<14} │"
                
                print(f'\n┌{"─" * (len(title) - 2)}┐')
                print(title)
                print(f'├{"─" * (len(title) - 2)}┤')
                
                KEY = ubah_data
                JUDUL = koleksi_buku[KEY]['judul']
                PENULIS = koleksi_buku[KEY]['penulis']
                TOTAL = koleksi_buku[KEY]['stok total']
                TERSEDIA = koleksi_buku[KEY]['stok tersedia']
                print(f"│ {KEY:<5} {JUDUL:<20} {PENULIS:<20} {TOTAL:^11} {TERSEDIA:^14} │")
                
                print(f'└{"─" * (len(title) - 2)}┘')
                
                print("Pilih data yang ingin diubah: ")
                print("1) Judul") 
                print("2) Penulis")
                print("3) Stok total")
                print("4) Batal")
                pilihan_ubah = input("Jawabanmu [1/2/3/4]: ")
                if pilihan_ubah == '1':
                    judul_baru = input("Masukkan judul baru: ").title() # .title() digunakan untuk mengabaikan case sensitive agar input yang dilakukan oleh user akan disesuaikan oleh sistem dan dibandingkan dengan data yang ada di koleksi buku
                    if judul_baru == '':
                        print("\n┌────────────────────────────────┐")
                        print("│ Judul buku tidak boleh kosong! │")
                        print("└────────────────────────────────┘")
                    koleksi_buku[KEY]['judul'] = judul_baru
                    print(f"Berhasil mengubah judul buku menjadi '{judul_baru}'")
                elif pilihan_ubah == '2':
                    penulis_baru = input("Masukkan nama penulis baru: ").title()
                    if penulis_baru == '':
                        print("\n┌──────────────────────────────────┐")
                        print("│ Nama penulis tidak boleh kosong! │")
                        print("└──────────────────────────────────┘")
                    koleksi_buku[KEY]['penulis'] = penulis_baru
                    print(f"Berhasil mengubah nama penulis buku '{koleksi_buku[KEY]['judul']}' menjadi '{penulis_baru}'")
                elif pilihan_ubah == '3':
                    stok_total_baru = int(input("Masukkan total stok yang baru: "))
                    if stok_total_baru <= koleksi_buku[KEY]['stok tersedia']:
                        print("\n┌────────────────────────────────────────────────────────────────────────────────┐")
                        print("│ Perhitungan tidak valid! Stok total tidak bisa lebih kecil dari stok tersedia. │")
                        print("└────────────────────────────────────────────────────────────────────────────────┘")
                    else:
                        selisih_stok = stok_total_baru - koleksi_buku[KEY]['stok total']
                        v_stok = koleksi_buku[KEY]['stok total']
                        koleksi_buku[KEY]['stok total'] = stok_total_baru
                        koleksi_buku[KEY]['stok tersedia'] += selisih_stok
                        title = f"│ Stok total buku '{JUDUL}' berhasil diupdate dari {v_stok} menjadi {koleksi_buku[KEY]['stok total']} │"
                        
                        print(f'\n┌{"─" * (len(title) - 2)}┐')
                        print(title)
                        print(f'└{"─" * (len(title) - 2)}┘')
                elif pilihan_ubah == '4':
                    print("\n┌───────────────────────┐")
                    print("│ Perubahan dibatalkan! │")
                    print("└───────────────────────┘")
                    continue
                        
                        
            else:
                print("\n┌───────────────────────┐")
                print("│ Buku tidak ditemukan! │")
                print("└───────────────────────┘")

# 5 ========================================================================================================================
# Baris kode untuk opsi menghapus buku               
    elif choice == '5':
        if len(koleksi_buku) == 0:
            print("\n┌──────────────────────────────────┐")
            print("│ Belum ada buku yang ditambahkan! │")
            print("└──────────────────────────────────┘")
        else:
            title = f"│ {'Kode':<5} {'Judul':<20} {'Penulis':<20} {'Stok total':<11} {'Stok tersedia':<14} │"
            
            print(f'\n┌{"─" * (len(title) - 2)}┐')
            print(title)
            print(f'├{"─" * (len(title) - 2)}┤')
            for buku in koleksi_buku:
                KEY = buku
                JUDUL = koleksi_buku[KEY]['judul']
                PENULIS = koleksi_buku[KEY]['penulis']
                TOTAL = koleksi_buku[KEY]['stok total']
                TERSEDIA = koleksi_buku[KEY]['stok tersedia']
                print(f"│ {KEY:<5} {JUDUL:<20} {PENULIS:<20} {TOTAL:^11} {TERSEDIA:^14} │")
                
            print(f'└{"─" * (len(title) - 2)}┘')
            
            hapus_buku = input("Masukkan kode buku yang ingin dihapus: ")
            
            buku_sedang_dipinjam = False
            if hapus_buku in koleksi_buku:
                for buku in koleksi_buku:
                    if koleksi_buku[hapus_buku]['stok tersedia'] < koleksi_buku[hapus_buku]['stok total']:
                        buku_sedang_dipinjam = True

                if buku_sedang_dipinjam:
                    print("\n┌──────────────────────────────────────────────────────────────────────────┐")
                    print("│ Tidak bisa menghapus buku! Karena masih ada yang meminjam buku tersebut. │")
                    print("└──────────────────────────────────────────────────────────────────────────┘")
                    continue
                        
                konfirmasi = input("Apakah anda yakin ingin menghapus buku ini? (y/n): ").lower()
                if konfirmasi == 'y':
                    title = f"│ Buku '{koleksi_buku[hapus_buku]['judul']}' berhasil dihapus! │"
                
                    print(f'\n┌{"─" * (len(title) - 2)}┐')
                    print(title)
                    print(f'└{"─" * (len(title) - 2)}┘')
                
                    del koleksi_buku[hapus_buku]
                else:
                    print("\n┌─────────────────────┐")
                    print("│ Buku tidak dihapus! │")
                    print("└─────────────────────┘")
            
                    
            else:
                print("\n┌───────────────────────┐")
                print("│ Buku tidak ditemukan! │")
                print("└───────────────────────┘")

# 6 ========================================================================================================================
# Baris kode untuk opsi melihat data peminjaman buku

    elif choice == '6':
        if len(peminjaman) == 0:
            print("\n┌───────────────────────────────┐")
            print("│ Belum ada buku yang dipinjam! │")
            print("└───────────────────────────────┘")
        else:
            title = f"│ {'No':<3} {'Nama Peminjam':<15} {'Kode':<5} {'Judul dan Penulis':<35} {'Pinjam':<11} {'Kembali':<14} {'Status':<12} │"
            
            print(f'\n┌{"─" * (len(title) - 2)}┐')
            print(title)
            print(f'├{"─" * (len(title) - 2)}┤')
            
            for i, peminjam in enumerate(peminjaman):
                KEY = peminjam
                
                KODE = peminjaman[KEY]['kode']
                NAMA = peminjaman[KEY]['peminjam']
                JUDUL = peminjaman[KEY]['judul']
                PENULIS = peminjaman [KEY]['penulis']
                
                JUDUL_PENULIS = [JUDUL, PENULIS]
                
                JUDUL_PENULIS = f"{JUDUL_PENULIS[0]} oleh {JUDUL_PENULIS[1]}"
                PINJAM = peminjaman[KEY]['tanggal pinjam']
                KEMBALI = peminjaman[KEY]['tanggal kembali']
                STATUS = peminjaman[KEY]['status']

                i = int(i)
                i = i + 1
                i = str(i)
                i = i + '.'
                title_bawah = f"│ {i:<3} {NAMA:<15} {KODE:<5} {JUDUL_PENULIS:<35} {PINJAM:<11} {KEMBALI:<14} {STATUS:<12} │"
                print(title_bawah)
                # print(f"│ {f(i+1)} {NAMA:<15} {KEY:<5} {JUDUL_PENULIS:<35} {PINJAM:<11} {KEMBALI:<14} {STATUS:<12} │")

            print(f'└{"─" * (len(title) - 2)}┘')

# 7 ========================================================================================================================
# Baris kode untuk opsi meminjam buku               
    elif choice == '7':
        if len(koleksi_buku) == 0:
            print("\n┌──────────────────────────────────┐")
            print("│ Belum ada buku yang ditambahkan! │")
            print("└──────────────────────────────────┘")
        else:
            title = f"│ {'Kode':<5} {'Judul':<20} {'Penulis':<20} {'Stok total':<11} {'Stok tersedia':<14} │"
            
            print(f'\n┌{"─" * (len(title) - 2)}┐')
            print(title)
            print(f'├{"─" * (len(title) - 2)}┤')
            for buku in koleksi_buku:
                KEY = buku
                JUDUL = koleksi_buku[KEY]['judul']
                PENULIS = koleksi_buku[KEY]['penulis']
                TOTAL = koleksi_buku[KEY]['stok total']
                TERSEDIA = koleksi_buku[KEY]['stok tersedia']
                print(f"│ {KEY:<5} {JUDUL:<20} {PENULIS:<20} {TOTAL:^11} {TERSEDIA:^14} │")
                
            print(f'└{"─" * (len(title) - 2)}┘')
            pinjam_buku = input("Masukkan kode buku yang ingin dipinjam: ")
            KEY = pinjam_buku
            trigger = False
            if pinjam_buku in koleksi_buku:
                if koleksi_buku[pinjam_buku]['stok tersedia'] > 0:
                    nama_peminjam = input("Masukkan nama peminjam: ").title()
                    for i, buku in peminjaman.items():
                        if nama_peminjam in buku['peminjam'] and pinjam_buku == buku['kode'] and buku['status'] == 'Dipinjam':
                            title = f"│ {'Nama Peminjam':<15} {'Kode':<5} {'Judul dan Penulis':<35} {'Pinjam':<11} {'Kembali':<14} {'Status':<12} │"
            
                            print(f'\n┌{"─" * (len(title) - 2)}┐')
                            print(title)
                            print(f'├{"─" * (len(title) - 2)}┤')
                            
                            NAMA = buku['peminjam']
                            JUDUL = buku['judul']
                            PENULIS = buku['penulis']
                            JUDUL_PENULIS = [JUDUL, PENULIS]
                            JUDUL_PENULIS = f"{JUDUL_PENULIS[0]} oleh {JUDUL_PENULIS[1]}"
                            
                            PINJAM = buku['tanggal pinjam']
                            KEMBALI = buku['tanggal kembali']
                            STATUS = buku['status']
                            
                            print(f"│ {NAMA:<15} {KEY:<5} {JUDUL_PENULIS:<35} {PINJAM:<11} {KEMBALI:<14} {STATUS:<12} │")
                            
                            print(f'└{"─" * (len(title) - 2)}┘')
                            
                            print("Buku tersebut masih anda pinjam! Dimohon untuk mengembalikannya terlebih dahulu sebelum meminjam buku yang sama lagi.")
                            trigger = True
                        else:
                            continue
                    if trigger:
                        continue
                    
                    konfirmasi = input("Apakah anda yakin ingin meminjam buku ini? (y/n): ").lower()
                    
                    if konfirmasi == 'y':
                        koleksi_buku[pinjam_buku]['stok tersedia'] -= 1
                        
                        KEY = "A" + "".join(random.choices(string.digits, k = 3))
                        
                        peminjaman_sementara['kode'] = pinjam_buku
                        peminjaman_sementara['peminjam'] = nama_peminjam
                        peminjaman_sementara['judul'] = koleksi_buku[pinjam_buku]['judul']
                        peminjaman_sementara['penulis'] = koleksi_buku[pinjam_buku]['penulis']
                        peminjaman_sementara['tanggal pinjam'] = date.today().strftime("%d/%m/%Y")
                        peminjaman_sementara['tanggal kembali'] = None
                        peminjaman_sementara['status'] = 'Dipinjam'
                        
                        # mengonversi tipe data pada tanggal yaitu 'datetime' menjadi string
                        # karena file json tidak bisa menyimpan format file 'datetime' ketika kita menyimpan perubahan yang terjadi
                        peminjaman_sementara['tanggal pinjam'] = str(peminjaman_sementara['tanggal pinjam'])

                        peminjaman[KEY] = peminjaman_sementara.copy() # menyalin perubahan yang ada di dalam dict peminjaman_sementara ke dalam dict peminjaman
                        # dengan menggunakan KEY unik yang kita input tadi agar dict peminjaman_sementara tidak tertimpa bisa menyimpan data berikutnya
                        print("\n┌─────────────────────────┐")
                        print("│ Buku berhasil dipinjam! │")
                        print("└─────────────────────────┘")
                    else:
                        print("\n┌──────────────────────┐")
                        print("│ Buku batal dipinjam! │")
                        print("└──────────────────────┘")
                        continue
                else:
                    title = f"│ Stok untuk buku '{koleksi_buku[pinjam_buku]['judul']}' tidak tersedia! │"
                
                    print(f'\n┌{"─" * (len(title) - 2)}┐')
                    print(title)
                    print(f'└{"─" * (len(title) - 2)}┘')
                
            else:
                print("\n┌───────────────────────┐")
                print("│ Buku tidak ditemukan! │")
                print("└───────────────────────┘")
            
# 8 ========================================================================================================================
# Baris kode untuk opsi mengembalikan buku yang dipinjam
    elif choice == '8':
        nama_peminjam = input("Masukkan nama peminjam buku: ").capitalize()
        hasil = []
        for key, buku in peminjaman.items():
            if nama_peminjam in buku['peminjam'] and buku['status'] == 'Dipinjam':
                hasil.append((key, buku))
                
        if hasil:
            title = f"│ {'Nama Peminjam':<15} {'Kode':<5} {'Judul dan Penulis':<35} {'Pinjam':<11} {'Kembali':<14} {'Status':<12} │"
            
            print(f'\n┌{"─" * (len(title) - 2)}┐')
            print(title)
            print(f'├{"─" * (len(title) - 2)}┤')
            
            for kode, buku in hasil:
                judul_penulis = f"{buku['judul']} oleh {buku['penulis']}"
                
                print(f"│ {buku['peminjam']:<15} {buku['kode']:<5} {judul_penulis:<35} {buku['tanggal pinjam']:<11} {buku['tanggal kembali']:<14} {buku['status']:<12} │")
        
            print(f'└{"─" * (len(title) - 2)}┘')
        
            buku_dipinjam = input("Masukkan kode buku yang ingin dikembalikan: ")

            for KEY, buku in peminjaman.items():
                if buku_dipinjam in buku['kode'] and nama_peminjam in buku['peminjam'] and buku['status'] == 'Dipinjam':
                    konfirmasi = input("Apakah anda yakin ingin mengembalikan buku ini? (y/n): ")
                    if konfirmasi == 'y':
                        buku['status'] = 'Dikembalikan'
                        buku['tanggal kembali'] = date.today().strftime("%d/%m/%Y")
                        
                        KEY = buku_dipinjam
                        koleksi_buku[KEY]['stok tersedia'] += 1
                        
                        title = f"│ Buku '{buku['judul']}' berhasil dikembalikan! │"
                        print(f"┌{"─" * (len(title) - 2)}┐")
                        print(title)
                        print(f"└{"─" * (len(title) - 2)}┘")
                    else:
                        print("\n┌──────────────────────────┐")
                        print("│ Buku batal dikembalikan! │")
                        print("└──────────────────────────┘")
                    break
                
            else:
                print("\n┌────────────────────────────────────────────┐")
                print("│ Buku dengan kode tersebut tidak ditemukan! │")
                print("└────────────────────────────────────────────┘")
            
        else:
            print("\n┌────────────────────────────────┐")
            print("│ Nama peminjam tidak ditemukan! │")
            print("└────────────────────────────────┘")        
                   
# 9 ========================================================================================================================
# Baris kode untuk opsi keluar dari program
    elif choice == '9':
        with open('mini_library.json', 'w') as file: # untuk menyimpan perubahan yang terjadi di dalam dictionary inventaris ke dalam file eksternal bernama inventaris.json
            json.dump(koleksi_buku, file, indent= 4) # indent = 4 untuk format yang rapi
        
        with open('data_peminjaman.json', 'w') as file:
            json.dump(peminjaman, file, indent= 4)
        
        print("Program perpusatakaan mini selesai.")
        exit()