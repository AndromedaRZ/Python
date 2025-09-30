# Projek manajemen kontak menggunakan function

from tambah_kontak import tambah_kontak

data_kontak = {}

title = "│ DATA KONTAK PRIBADI │"
print(f"┌{'─'*(len(title) - 2)}┐")
print(title)
print(f"└{'─'*(len(title) - 2)}┘")

while True:
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
        tambah_kontak(data_kontak)
    
# =======================================================================================================================================
# Jika user memilih untuk melihat seluruh kontak yang ada
    if choice == '2':
        for kontak, value in data_kontak.items():
            print(value['nama'], value['nomor'], value['email'])
    
# =======================================================================================================================================
# Jika user memilih untuk mengubah (mengedit) kontak yang ada
    if choice == '3':
        continue
    
# =======================================================================================================================================
# Jika user memilih untuk menghapus kontak yang ada
    if choice == '4':
        continue
    
# =======================================================================================================================================
# Jika user memilih untuk menambahkan kontak
    if choice == '5':
        break
    
print("Program kontak berhenti")