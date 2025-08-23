# Latihan dictionary
import datetime
import os
import string
import random

# template dictionary mahasiswa untuk key-key yang akan digunakan nanti
mahasiswa_template = {
    'nama':'nama',
    'nim':'nim',
    'jurusan':'jurusan',
    'lahir':datetime.datetime(1111,11,1)
}

# dictionary untuk menyimpan semua data mahasiswa
data_mahasiswa = {}

while True:
    # os.system("cls") # digunakan untuk terminal powershell pada windows
    os.system("clear") # digunakan untuk os linux, mac, dan terminal git
    print(f"{'SELAMAT DATANG DI':^25}")
    print(f"{'DATA MAHASISWA':^25}")
    print("-"*25)

    # membuat dictioanary baru dengan nama 'mahasiswa' menggunakan key dari dictionary 'mahasiswa_template'
    mahasiswa = dict.fromkeys(mahasiswa_template.keys())
    
    # mengambil input dari user untuk mengisi value dari key 'nama','nim' dan 'jurusan' ke dalam dictionary 'mahasiswa'
    mahasiswa['nama'] = input("Nama Mahasiswa: ")
    mahasiswa['nim'] = input("Nim Mahasiswa: ")
    mahasiswa['jurusan'] = input("Jurusan Mahasiswa: ")
    TAHUN_LAHIR = int(input("Tahun lahir: "))
    BULAN_LAHIR = int(input("Bulan lahir: "))
    TANGGAL_LAHIR = int(input("Tanggal lahir: "))
    mahasiswa['lahir'] = datetime.datetime(TAHUN_LAHIR, BULAN_LAHIR, TANGGAL_LAHIR)

    # fungsi kode di bawah ini adalah akan membuat KEY unik dengan menggunakan random lalu memilih string dengan kode ascii_uppercase, lalu for untuk menentukan dibuat berapa kali
    KEY = ''.join((random.choice(string.ascii_uppercase) for i in range(6)))
    
    # menambahkan data 'mahasiswa' ke dictionary 'data_mahasiswa' dengan KEY sebagai kunci
    data_mahasiswa.update({KEY:mahasiswa})
    
    print(f'\n{'KEY':<7} {'Nama':<10} {'nim':<10} {'jurusan':<13} {'Lahir':<10}')
    print("-"*55)
    
    for mahasiswa in data_mahasiswa:
        KEY = mahasiswa
        # ambil data detail dari dictionary berdasarkan key
        NAMA = data_mahasiswa[KEY]['nama']
        NIM = data_mahasiswa[KEY]['nim']
        JURUSAN = data_mahasiswa[KEY]['jurusan']
        LAHIR = data_mahasiswa[KEY]['lahir'].strftime("%d/%m/%Y")
        
        print(f'{KEY:<7} {NAMA:<10} {NIM:<10} {JURUSAN:<13} {LAHIR:<10}')
        
    print("\n")
    isDone = input("Mau tambah data mahasiswa lagi? [y/n]: ")
    if isDone == "n":
        break

print("Akhir dari program, terima kasih!")


