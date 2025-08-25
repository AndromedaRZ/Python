# program buku kontak

print('''┌───────────────────────────────────────┐
│ Selamat datang di Program Buku Kontak │
└───────────────────────────────────────┘''')

kontak_template = {
    'nama':'nama',
    'nomor':0
}

kontak_dict = {}

# di sini title

while True:
    kontak = dict.fromkeys(kontak_template.keys())
    
    print('''
1) Tambah kontak
2) Lihat semua kontak
3) Cari & ubah kontak
4) Hapus kontak
5) Keluar''')
    choice = int(input("Apa yang ingin anda lakukan? "))

    if choice == 1:
        kontak['nama'] = input("Masukkan nama kontak: ").capitalize()
        kontak['nomor'] = input("Masukkan nomor telepon: ")

        KEY = kontak['nama']  # gunakan nama sebagai key unik (lowercase)

        kontak_dict[KEY] = kontak.copy()  # simpan salinan kontak agar tidak tertimpa

    elif choice == 2:
        if len(kontak_dict) == 0:
            print("\n─────────────────────────────────")
            print("Belum ada kontak yang ditambahkan")
            print("─────────────────────────────────")
        else:
            title = "┌────┬──────────────┬───────────────┐"
            title2 = f"│ {'No':<2} │ {'Nama':<12} │ {'Nomor telepon':<13} │"
            print('')
            print('Daftar Kontak'.center(len(title2)))
            print(title)
            print(title2)
            print('├────┼──────────────┼───────────────┤')
            for i,KEY in enumerate(kontak_dict):
                NAMA = kontak_dict[KEY]['nama']
                NOMOR = kontak_dict[KEY]['nomor']
                print(f"│ {i+1}. │ {NAMA:<12} │ {NOMOR:<13} │")
            print('└────┴──────────────┴───────────────┘')
    
    elif choice == 3:
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
            print("\n──────────────────────")
            print("Kontak tidak ditemukan")
            print("──────────────────────")
            
    elif choice == 4:
        if len(kontak_dict) == 0:
            print("\n─────────────────────────────────")
            print("Belum ada kontak yang ditambahkan")
            print("─────────────────────────────────")
        else:
            title = "┌────┬──────────────┬───────────────┐"
            title2 = f"│ {'No':<2} │ {'Nama':<12} │ {'Nomor telepon':<13} │"
            print('')
            print('Daftar Kontak'.center(len(title2)))
            print(title)
            print(title2)
            print('├────┼──────────────┼───────────────┤')
            for i,KEY in enumerate(kontak_dict):
                NAMA = kontak_dict[KEY]['nama']
                NOMOR = kontak_dict[KEY]['nomor']
                print(f"│ {i+1}. │ {NAMA:<12} │ {NOMOR:<13} │")
            print('└────┴──────────────┴───────────────┘')
            hapus_kontak = input("Masukkan nama kontak yang ingin dihapus: ").capitalize()
            del kontak_dict[hapus_kontak]
            print(f"Kontak '{hapus_kontak}' berhasil dihapus!")
            
    elif choice == 5:
        break

print("Program selesai!")            