# latihan dictionary

import os

# Latihan ke-1
# mahasiswa = {
#     "001": {"nama":"Rizky", "jurusan":"Teknik Informatika"},
#     "002": {"nama":"Budi", "jurusan":"Sistem Informasi"},
# }

# print(mahasiswa["001"]["nama"])

# for nim, data in mahasiswa.items():
#     print(f'NIM: {nim} | Nama: {data["nama"]} | Jurusan: {data["jurusan"]}')

# break latihan

# data barang gudang elektronik

# template_gudang = {
#     'id':'123',
#     'nama barang':'laptop',
#     'jumlah': 3,
#     'keterangan':'barang masuk/keluar'
# }

# data_gudang = {}

# while True:
#     os.system("clear")
#     print(f'{"SELAMAT DATANG DI":^25}')
#     print(f'{"INPUT DATA GUDANG":^25}')
#     print('-'*25)

#     # membuat dictionary baru dengan nama 'gudang' dengan mengambil keysnya dari dictionary 'template_gudang' 
#     gudang = dict.fromkeys(template_gudang.keys())
    
#     gudang['id'] = input("Masukan id barang [3 digit]: ")
#     gudang['nama barang'] = input("Masukan nama barang: ")
#     gudang['jumlah'] = input("Masukan jumlah barangnya: ")
#     gudang['keterangan'] = input("Masukan keterangan barang tersebut [masuk/keluar]: ")

    # KEY = gudang['id'] # menggunakan id barang di gudang sebagai key unik

    # data_gudang[KEY] = gudang.copy()

#     print(f'\n{"ID":<3} {"NAMA BARANG":<12} {"JUMLAH":<7} {"KETERANGAN":<12}')
#     print("-"*40)

#     for gudang in data_gudang:
#         KEY = gudang
#         ID = data_gudang[KEY]['id']
#         NAMA_BARANG = data_gudang[KEY]['nama barang']
#         JUMLAH = data_gudang[KEY]['jumlah']
#         KETERANGAN = data_gudang[KEY]['keterangan']
#         print(f'{ID:<3} {NAMA_BARANG:<12} {JUMLAH:^7} {KETERANGAN:<12}')
        
    
#     print("\n")    
#     isLanjut = input("Lanjutkan memasukan data barang? [y/n]: ")
#     if isLanjut == "n":
#         break
        
# print("PRORGAM INPUT DATA GUDANG DIHENTIKAN")

# Program data buku 

template_buku = {
    "judul":"stop korupsi",
    "penulis":"soeharto.jr",
    "tahun terbit":1989
}


data_buku = {}

count = 1
while True:
    
    print()
    print(f"{"SELAMAT DATANG DI":^25}")
    print(f"{"DATA INVENTARIS BUKU":^25}")
    print("-"*25)
    
    list_buku = dict.fromkeys(template_buku.keys())

    list_buku['judul'] = input("Masukan judul buku: ")
    list_buku['penulis'] = input("Masukan nama penulis: ")
    list_buku['tahun terbit'] = int(input("Masukan tahun terbit buku: "))

    data_buku[count] = list_buku.copy()
    print(f"\n{'No':<3} {'Judul Buku':<13} {'Nama Penulis':<15} {'Tahun Terbit':<13}")
    print("-"*50)
    # print(data_buku)
    for KEY in data_buku:
        JUDUL = data_buku[KEY]['judul']
        PENULIS = data_buku[KEY]['penulis']
        TAHUN_TERBIT = data_buku[KEY]['tahun terbit']

        print(f'{KEY:<3} {JUDUL:<13} {PENULIS:<15} {TAHUN_TERBIT:<13}')
        
    count += 1
    
    isLanjut = input("\nMasih ingin memasukan data buku?[y/n]: ")
    if isLanjut == "n":
        break
    
    

print("PROGRAM INPUT DATA BUKU BERHENTI!")