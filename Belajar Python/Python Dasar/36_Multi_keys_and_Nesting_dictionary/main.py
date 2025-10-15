# Multi keys and Nesting dictionary

import datetime

# data mahasiswa 1
mahasiswa1 = {
    'nama':'rizky si programmer',
    'nim':'22092006',
    'sks_lulus':140,
    'beasiswa':True,
    'lahir':datetime.datetime(2006,9,22)
}

# data mahasiswa 2
mahasiswa2 = {
    'nama':'Doni si hacker',
    'nim':'2220019',
    'sks_lulus':100,
    'beasiswa':False,
    'lahir':datetime.datetime(2002,10,21)
}

# data mahasiswa 3
mahasiswa3 = {
    'nama':'Jibar si pelawak',
    'nim':'12082001',
    'sks_lulus':130,
    'beasiswa':True,
    'lahir':datetime.datetime(2005,5,3)
}

# menggabungkan semua data mahasiswa ke dalam satu dictionary indux, seperti membuat dictionary di dalam dictionary, dengan keynya adalah kode unik mahasiswanya yaitu 001, 002, 003 dan value atau nilainya adalah data mahasiswa itu sendiri yang sebelumnya sudah dibuat di dalam dictionary di atas
data_mahasiswa = {
    '001': mahasiswa1,
    '002': mahasiswa2,
    '003': mahasiswa3
}

print(data_mahasiswa)

# selanjutnya kita akan membuat sebuah tabel untuk menampung semua data mahasiswa di atas, fungsi :<(angka) dalam setiap kolom adalah sebagai align text, dengan keterangan :< sebagai rata kiri, :^ sebagai rata tengah, dan :> sebagai rata kanan
print(f'{'KEY':<3} {'Nama':<20} {'SKS':<3} {'Beasiswa':<9} {'Lahir':<10}')

print("-"*50)

for KEY in data_mahasiswa:
    
    # ambil data detail dari dictionary berdasarkan key
    NAMA = data_mahasiswa[KEY]['nama']
    SKS = data_mahasiswa[KEY]['sks_lulus']
    BEASISWA = data_mahasiswa[KEY]['beasiswa']
    LAHIR = data_mahasiswa[KEY]['lahir'].strftime("%d/%m/%Y")
    
    if BEASISWA == 1:
        BEASISWA = "iya"
        
    else:
        BEASISWA = "tidak"
    
    print(f'{KEY:<3} {NAMA:<20} {SKS:<3} {BEASISWA:<9} {LAHIR:<10}')