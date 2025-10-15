from . import Database
from .Utils import random_string

# komponen fungsi untuk melihat data inventaris
def read():
    '''komponen fungsi untuk melihat data inventaris'''
    data = Database.read_json()
    return data

# komponen fungsi untuk menambah data saat pertama kali membuka data invenataris
def create_first_data():
    data = read()
    '''fungsi untuk menambah data awal pada inventaris'''
    nama = input("Masukan nama barang: ")
    while True:
        try:
            harga = int(input("masukan harga satuan barang (Rp): "))
            break
        except:
            print("Harga barang harus berupa angka!")
    
    while True:
        try:
            stok = int(input("masukan stok barang: "))
            break
        except:
            print("Stok barang harus berupa angka!")
    
    KEY = random_string(3)
    
    data_sementara = {
            'nama': nama,
            'harga': harga,
            'stok': stok
    }

    # menggabungkan data sementara dengan data lama untuk menambahkan data
    data[KEY] = data_sementara.copy()
    
    # menyimpan data yang dibuat ke file json
    Database.save_json(data)
    print("Data berhasil ditambahkan")
    return data
    
# komponen fungsi untuk menambah data inventaris
def create(nama, harga, stok):
    '''komponen fungsi untuk menambah data inventaris'''
    data = read()
        
    data_sementara = {
        'nama':nama,
        'harga':harga,
        'stok':stok,
    }
    
    KEY = random_string(3)
    
    # menggabungkan data sementara dengan data lama untuk menambahkan data
    data[KEY] = data_sementara.copy()
    
    # menyimpan data yang dibuat ke file json
    Database.save_json(data)
    print("Data berhasil ditambahkan")
    return data

# komponen fungsi untuk mengupdate data inventaris
def update(kode, harga, stok):
    '''komponen fungsi untuk mengupdate data inventaris'''
    data = read()
    # Update hanya bagian yang dikirim (tidak semua harus diubah)
    if harga is not None:
        data[kode]['harga'] = harga
    if stok is not None:
        data[kode]['stok'] = stok
    
    Database.save_json(data)
    print("Data berhasil diupdate")
    return data
    
# cek kode unik yang ada di data inventaris
def check(kode):
    '''cek kode unik yang ada di data inventaris'''
    data = read()
    if kode in data:
        return kode
    else:
        return False  
    
# komponen fungsi untuk menghapus salah satu data inventaris
def delete(kode):
    '''komponen fungsi untuk menghapus salah satu data inventaris'''
    data = read()
    del data[kode]
    Database.save_json(data)
    print("Data berhasil dihapus")
    return data
    
    

        