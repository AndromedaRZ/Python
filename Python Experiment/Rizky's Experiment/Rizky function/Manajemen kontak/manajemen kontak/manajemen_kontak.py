# Projek manajemen kontak menggunakan function

import tambah_kontak, display_kontak, cari_ubah

data_kontak = {}

title = "│ DATA KONTAK PRIBADI │"
print(f"┌{'─'*(len(title) - 2)}┐")
print(title)
print(f"└{'─'*(len(title) - 2)}┘")

while True:
    print()
    title = "   MENU KONTAK   "
    print("-" * (len(title)))
    print(f"{title}")
    print("-" * (len(title)))
    print('''1. Tambah Kontak
2. Lihat Kontak
3. Cari & Ubah Kontak
4. Hapus Kontak
5. Keluar''')
    choice = input("Pilih Menu [1-5]: ")

# =======================================================================================================================================
# Jika user memilih untuk menambahkan kontak
    if choice == '1':
        tambah_kontak.tambah_kontak(data_kontak)
    
# =======================================================================================================================================
# Jika user memilih untuk melihat seluruh kontak yang ada
    if choice == '2':
        display_kontak.display_kontak(data_kontak)
    
# =======================================================================================================================================
# Jika user memilih untuk mengubah (mengedit) kontak yang ada
    if choice == '3':
        cari_ubah.cari_ubah(data_kontak)
    
# =======================================================================================================================================
# Jika user memilih untuk menghapus kontak yang ada
    if choice == '4':
        if not data_kontak:
            title = f"│ Daftar kontak anda masih kosong! │"
            print(f"\n┌{'─'* (len(title) - 2)}┐")
            print(title)
            print(f"└{'─'* (len(title) - 2)}┘")
        
        else:
            dihapus = input("Masukan nama kontak yang ingin anda hapus: ")    
            if dihapus not in data_kontak:
                title = f"│ Kontak tersebut tidak ada! │"
                print(f"\n┌{'─'* (len(title) - 2)}┐")
                print(title)
                print(f"└{'─'* (len(title) - 2)}┘")
            
            else:
                del data_kontak[dihapus]
                title = f"│ Kontak berhasil dihapus! │"
                print(f"\n┌{'─'* (len(title) - 2)}┐")
                print(title)
                print(f"└{'─'* (len(title) - 2)}┘") 
        
# =======================================================================================================================================
# Jika user memilih untuk menambahkan kontak
    if choice == '5': 
        break
    
title = f"│ Program kontak dihentikan │"
print(f"\n┌{'─'* (len(title) - 2)}┐")
print(title)
print(f"└{'─'* (len(title) - 2)}┘")
