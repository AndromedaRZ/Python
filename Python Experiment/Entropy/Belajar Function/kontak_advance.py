# program buku kontak

print('''┌───────────────────────────────────────┐
│ Selamat datang di Program Buku Kontak │
└───────────────────────────────────────┘''')

def title_kosong():
    '''title kontak kosong'''
    print("\n┌───────────────────────────────────┐")
    print("│ Belum ada kontak yang ditambahkan │")
    print("└───────────────────────────────────┘")
    
kontak_dict = {}

def title_atas():
    '''title bagian atas'''
    title = f"│ {'No':<3}│ {'Nama':<12} │ {'Nomor telepon':<13} │"
    print(f"\n{'DAFTAR KONTAK':^{len(title)}}")
    print("┌────┬──────────────┬───────────────┐")
    print(title)
    print('├────┼──────────────┼───────────────┤')
    
def title_bawah():
    for i, KEY in enumerate(kontak_dict):
        NAMA = kontak_dict[KEY]['nama']
        NOMOR = kontak_dict[KEY]['nomor']
        i = int(i)
        i += 1
        i = str(i)
        i = i + '.'
        print(f"│ {i:<3}│ {NAMA:<12} │ {NOMOR:<13} │")
    print("└────┴──────────────┴───────────────┘")
        
while True:
    print('''
1) Tambah kontak
2) Lihat semua kontak
3) Cari & ubah kontak
4) Hapus kontak
5) Keluar''')
    choice = input("Apa yang ingin anda lakukan? ")

    if choice == '1':
        def tambah_kontak(**kontak_sementara): # fungsi yang berguna untuk menambahkan kontak, karena hasil dari input berupa dict
            '''fungsi menambah kontak'''
            KEY = nama # nama yang diinput akan menjadi KEY dari pemilik nomor yang ditambahkan            
            kontak_dict[KEY] = kontak_sementara.copy()
        
        nama = input("Masukkan nama kontak: ").capitalize()
        nomor = input("Masukkan nomor telepon: ")
        
        tambah_kontak(nama = nama, nomor = nomor)
            
    elif choice == '2':
        if len(kontak_dict) == 0:
            title_kosong()
        else:
            title_atas()
            title_bawah()
    
    elif choice == '3':
        cari_nama = input("Masukkan nama kontak yang ingin dicari: ").capitalize()
        
        if cari_nama in kontak_dict:
            print("\nKontak ditemukan!")
            print(f"{'Nama':<5}: {cari_nama}")
            print(f"{'Nomor':<5}: {kontak_dict[cari_nama]['nomor']}")
            ubah_kontak = input("Apakah ingin mengubah kontak ini? (y/n): ")
            if ubah_kontak.lower() == 'y':
                nomor_baru = input("Masukkan nomor baru: ")
                
                kontak_dict[cari_nama]['nomor'] = nomor_baru
                print(f"Kontak '{cari_nama}' berhasil diperbarui menjadi {nomor_baru}!")
            else:
                print("Kontak tidak diubah")
        else:
            print("\n┌────────────────────────┐")
            print("│ Kontak tidak ditemukan │")
            print("└────────────────────────┘")
            
    elif choice == '4':
        if len(kontak_dict) == 0:
            title_kosong()
        else:
            title_atas()
            title_bawah()
            
            hapus_kontak = input("Masukkan nama kontak yang ingin dihapus: ").capitalize()
            if hapus_kontak in kontak_dict:
                del kontak_dict[hapus_kontak]
                print(f"Kontak '{hapus_kontak}' berhasil dihapus!")
            else:
                print("\n┌────────────────────────┐")
                print("│ Kontak tidak ditemukan │")
                print("└────────────────────────┘")
            
    elif choice == '5':
        break

print("Program selesai!")