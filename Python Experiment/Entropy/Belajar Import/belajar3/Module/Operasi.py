from . import Database

def check():
    data_file = read()
    if len(data_file) == 0:
        print('\nData pengeluaran masih kosong! Silahkan tambahkan pengeluaran terlebih dahulu.')
        return False
    else:
        return True

def delete(nomor, data_file):
    data_file.pop(int(nomor)-1)
    Database.simpan_data(data_file)

def search(keyword):
    data_file = read()
    hasil_cari = []

    for data in data_file:
        gabungan = f"{data['tanggal']} {data['kategori']} {data['keterangan']} {data['jumlah']}".lower()

        if keyword in gabungan:
            hasil_cari.append(data)

    if hasil_cari:
        print(f"Hasil pencarian untuk '{keyword}':")
        title(hasil_cari)
    else:
        print(f"\nTidak ditemukan pengeluaran dengan keyword: '{keyword}'") 

def title(data):
    data_file = data
    
    print("┌────┬────────────┬──────────────────────┬────────────────────────────────┬──────────────┐")
    print(f"│ {'NO':2} │ {'TANGGAL':^10} │ {'KATEGORI':^20} │ {'KETERANGAN':^30} │ {'JUMLAH':^12} │")
    print("├────┼────────────┼──────────────────────┼────────────────────────────────┼──────────────┤")
    
    for i, data in enumerate(data_file):
        print(f"│ {i+1:<2} │ {data['tanggal']:<10} │ {data['kategori']:20} │ {data['keterangan']:30} │ Rp{data['jumlah']:<10,} │".replace(',','.'))
        
    print("└────┴────────────┴──────────────────────┴────────────────────────────────┴──────────────┘")

def read():
    data = Database.baca_database()
    return data

def input_kategori(input_data):
    match input_data:
        case '1': return 'Makan & Minum'
        case '2': return 'Transportasi'
        case '3': return 'Belanja'
        case '4': return 'Tagihan'
        case '5': return 'Lainnya'
    
def create(tanggal, kategori, keterangan, jumlah):
    
    data_baru = {
        'tanggal': tanggal,
        'kategori': kategori,
        'keterangan': keterangan,
        'jumlah': jumlah
    }
    
    databaes_sementara = read()
    databaes_sementara.append(data_baru)
    Database.simpan_data(databaes_sementara)
    
