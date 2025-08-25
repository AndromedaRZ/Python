# Latihan dictionary 1

import datetime
import os
import string
import random

# template dictionary mahasiswa

mahasiswa_template = {
    'nama':'nama',
    'nim':'0000000',
    'sks_lulus':0,
    'lahir':datetime.datetime(1111,1,11)
}

data_mahasiswa = {} # dictionary kosong

while True:
    os.system('clear') # program akan langsung menjalankan perintah 'clear' di terminal
    print(f"{'SELAMAT DATANG':^20}")
    print(f"{'DATA MAHASISWA':^20}")
    print("-"*20)

    mahasiswa = dict.fromkeys(mahasiswa_template.keys()) # mengambil template keys dari dict mahasiswa_template dan membuat dictionary baru
    # dengan menggunakan fungsi dict.fromkeys() dan memasukkannya ke dalam dictionary yang baru bernama mahasiswa
    print(mahasiswa) # jika masih belum ada isinya, maka outputnya akan menjadi 'none'

    mahasiswa['nama'] = input("Nama Mahasiswa: ") # kita tinggal membuat perintah input untuk mengambil data yang diinginkan dari user
    # dan memasukkannya ke dalam dictionary yang sudah mengambil template tadi yaitu dict mahasiswa
    mahasiswa['nim'] = input("NIM Mahasiswa: ")

    mahasiswa['sks_lulus'] = int(input("SKS Lulus: "))

    TAHUN_LAHIR = int(input("Tahun lahir (YYYY): "))
    BULAN_LAHIR = int(input("Bulan lahir (1-12)): "))
    TANGGAL_LAHIR = int(input("Tanggal lahir (1-31): "))

    mahasiswa['lahir'] = datetime.datetime(TAHUN_LAHIR,BULAN_LAHIR,TANGGAL_LAHIR)

    KEY = ''.join((random.choice(string.ascii_uppercase) for i in range(6))) # berfungsi untuk membuat KEY dengan menggunakan random dan memilih string kode ascii uppercase sebanyak 6 kali agar KEY-nya tidak meinmpa satu sama lain
    data_mahasiswa.update({KEY:mahasiswa})
    
    title = f"\n{'KEY':<6} {'Nama':<17} {'nim':10}{'SKS':<3} {'Lahir':<10}"

    print(title)
    print("-"*len(title))
    
    for i in data_mahasiswa: #untuk setiap i di dalam dictionary data_mahasiswa
        KEY = i # setiap urutan yang terlooping akan kita catat ke dalam constant KEY
    
        # singkatnya, fungsi constant KEY adalah untuk menandakan bahwa looping akan berulang ke looping yang berikutnya tergantung berapa banyak nested dict yang ada di dalam satu dictionary
    
        NAMA = data_mahasiswa[KEY]['nama'] # buat constant baru dan masukkan constant KEY lalu dengan menambahkan key dari dictionary yang kita inginkan
        NIM = data_mahasiswa[KEY]['nim'] # lakukan hal yang serupa untuk key dictionary berikutnya
        SKS = data_mahasiswa[KEY]['sks_lulus'] # nantinya setiap dictionary akan mengecek seluruh key dimulai dari atas sampai bawah
        LAHIR = data_mahasiswa[KEY]['lahir'].strftime("%d/%m/%Y") # pada bagian ini, kita menambahkan fungsi tambahan menggunakan .strftime() agar outputnya hanya menampilkan tanggal, bulan, dan tahunnya saja
        print(f"{KEY:<6} {NAMA:<17} {NIM:<10}{SKS:<3} {LAHIR:<10}")
        
    print('\n')
    isDone = input("Mau tambah lagi bro [y/n]? ") # untuk mengonfirmasi user apakah masih ingin menginput data atau tidak
    if isDone == 'n':
        break
    
print("\nAkhir dari program, terima kasih")