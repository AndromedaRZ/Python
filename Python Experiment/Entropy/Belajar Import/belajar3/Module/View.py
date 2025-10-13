from . import Operasi

def total_console():
    check = Operasi.check()
    if check:
        data_file = Operasi.read()
        print("\n=== Total semua pengeluaran yang tercatat ===")
        total = 0
        for data in data_file:
            total += data['jumlah']
            
        print(f"Rp{total:,}".replace(',','.'))
        
def delete_console():
    check = Operasi.check()
    if check:
        data_file = Operasi.read()
        print("\n=== Pengeluaran yang tercatat ===")
        Operasi.title(data_file)
        nomor = input("Masukkan nomor pengeluaran yang ingin dihapus: ")
        Operasi.delete(nomor, data_file)
        print("\nData pengeluaran berhasil dihapus!")
    
def search_console():
    print("\n=== Cari Pengeluaran ===")
    keyword = input("Masukkan keyword pencarian: ").lower()
    Operasi.search(keyword)
    
def read_console():
    check = Operasi.check()
    if check:
        data_file = Operasi.read()
        print("\n=== Lihat Semua Pengeluaran ===")
        Operasi.title(data_file)

def create_console():
    print("\n=== Tambah pengeluaran ===")
    tanggal = input("Tanggal (DD/MM/YYYY): ")
    print("Pilih kategori:")
    print("1. Makan & Minum")
    print("2. Transportasi")
    print("3. Belanja")
    print("4. Tagihan")
    print("5. Lainnya")
    kategori = Operasi.input_kategori(input("Masukkan nomor kategori: "))
    keterangan = input("Keterangan: ").capitalize()
    jumlah = int(input("Jumlah (Rp): "))
    
    Operasi.create(tanggal, kategori, keterangan, jumlah)
    
    