from .Database import read, save_data

# komponen fungsi untuk menambah data transaksi
def create(tanggal, jenis, jumlah, keterangan):
    '''komponen fungsi untuk menambah data inventaris'''
    data = read()
    
    data_sementara = {
        'tanggal':tanggal,
        'jenis':jenis,
        'jumlah':jumlah,
        'keterangan':keterangan,
    }
    
    data.append(data_sementara)
    save_data(data)
    print("Data transaksi berhasil ditambahkan")
    return

# komponen fungsi untuk menghapus data transaksi
def delete(transaksi_terpilih):
    '''komponen fungsi untuk menghapus data transaksi'''
    data = read()
    transaksi_terpilih -= 1
    data.pop(transaksi_terpilih)
    save_data(data)
    return data
