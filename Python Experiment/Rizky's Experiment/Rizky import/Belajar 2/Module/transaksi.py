from .Database import read, save_data, check
from .operasi import create, delete
from datetime import datetime

# fungsi untuk membaca data transaksi file jsonnya
def read_console():
    '''fungsi untuk melihat data transaksi'''
    data = read()
    
    # cek apakah sudah ada transaksi atau belum
    if not data:
        title = "│ Belum ada transaksi yang tercatat │"
        print(f"\n┌{'─'*(len(title) - 2)}┐")
        print(title)
        print(f"└{'─'*(len(title) - 2)}┘")
        return
    
    # header
    print("\n  DATA TRANSAKSI")
    title = f'│ {'No':^3} │ {'Tanggal':<10} │ {'Jenis Transaksi':<15} │ {'Jumlah (Rp)':<20} │ {'Keterangan':<30} │'
    print(f"┌{'─'*5}┬{'─'*12}┬{'─'*17}┬{'─'*22}┬{'─'*32}┐")
    print(title)
    print(f"├{'─'*5}┼{'─'*12}┼{'─'*17}┼{'─'*22}┼{'─'*32}┤")
    # data
    for i, n in enumerate(data, start=1):
        print(f'│ {i:^3} │ {n['tanggal']:<10} │ {n['jenis']:<15} │ {n['jumlah']:<20,} │ {n['keterangan']:<30} │'.replace(',','.'))
    # footer
    print(f"└{'─'*5}┴{'─'*12}┴{'─'*17}┴{'─'*22}┴{'─'*32}┘")
    
# fungsi untuk menambahkan data transaksi ke file json
def create_console():
    '''fungsi untuk menambahkan data transaksi ke file json'''
    
    tanggal = datetime.now().strftime("%d/%M/%Y")
    
    print("Silahkan masukan data transaksi")
    print("======================================")
    print("1. Pemasukan")
    print("2. Pengeluaran")
    
    while True:
        pilihan = input("\nPilih jenis transaksi [1/2]: ")
        match pilihan:
            case '1':
                jenis = 'pemasukan'
                break
            case '2':
                jenis = 'pengeluaran'
                break
            case _: print("\ninput tidak valid!")
        
    while True:
        try:
            jumlah = int(input("\nMasukan nominal uangnya (Rp): "))
            break
        except:
            print("\nNominal harus berupa angka!")
     
    keterangan = input("Masukan keterangan transaksi: ").capitalize()
    
    create(tanggal, jenis, jumlah, keterangan)
       
# fungsi untuk menghapus data transaksi
def delete_console():
    '''fungsi untuk menghapus data transaksi'''
    data = read()
    if not data:
        title = "│ Belum ada transaksi yang tercatat │"
        print(f"\n┌{'─'*(len(title) - 2)}┐")
        print(title)
        print(f"└{'─'*(len(title) - 2)}┘")
        return
    
    read_console()
    while True:
        nomor = int(input("Pilih nomor urut dari transaksi yang ingin dihapus: "))
        cek_nomor = check(nomor)
        if cek_nomor:
           break
        else:
            print("Nomor urut tidak ditemukan!")
    
    # mengambil index yang sesungguhnya dari list
    transaksi_terpilih = data[nomor - 1]
    
    # header
    print("\n  DATA TRANSAKSI")
    title = f'│ {'Tanggal':<10} │ {'Jenis Transaksi':<15} │ {'Jumlah (Rp)':<20} │ {'Keterangan':<30} │'
    print(f"┌{'─'*12}┬{'─'*17}┬{'─'*22}┬{'─'*32}┐")
    print(title)
    print(f"├{'─'*12}┼{'─'*17}┼{'─'*22}┼{'─'*32}┤")
    # data
    print(f'│ {transaksi_terpilih['tanggal']:<10} │ {transaksi_terpilih['jenis']:<15} │ {transaksi_terpilih['jumlah']:<20,} │ {transaksi_terpilih['keterangan']:<30} │'.replace(',','.'))
    # footer
    print(f"└{'─'*12}┴{'─'*17}┴{'─'*22}┴{'─'*32}┘")
    
    konfirmasi = input('Ingin menghapus transaksi tersebut? [y/n]: ')
    match konfirmasi:
        case 'y':
            delete(nomor)
            title = "│ Data transaksi berhasil dihapus │"
            print(f"\n┌{'─'*(len(title) - 2)}┐")
            print(title)
            print(f"└{'─'*(len(title) - 2)}┘")
            
        case 'n':
            title = "│ Kembali ke menu │"
            print(f"\n┌{'─'*(len(title) - 2)}┐")
            print(title)
            print(f"└{'─'*(len(title) - 2)}┘")
            
        case _:
            title = "│ Input invalid, kembali ke menu │"
            print(f"\n┌{'─'*(len(title) - 2)}┐")
            print(title)
            print(f"└{'─'*(len(title) - 2)}┘")
            
            
    
        
    
    
    
    