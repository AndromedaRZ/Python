import datetime

# pertama-tama kita akan membuat beberapa dictionary yang isinya data diri mahasiswa

mahasiswa1 = {
    'nama':'Ucup Surucup',
    'nim':'19022001',
    'sks_lulus':130,
    'beasiswa':False,
    'lahir':datetime.datetime(2001,4,10)
}

mahasiswa2 = {
    'nama':'Otong Surotong',
    'nim':'19022002',
    'sks_lulus':140,
    'beasiswa':True,
    'lahir':datetime.datetime(2002,10,10)
}

mahasiswa3 = {
    'nama':'Asep si kasyep',
    'nim':'19022003',
    'sks_lulus':100,
    'beasiswa':False,
    'lahir':datetime.datetime(2000,2,29) 
}

# lalu kita akan menggabungkan ketiga dictionary itu ke dalam satu dictionary (disebut nesting dictionary)

data_mahasiswa = {
    'MAH001':mahasiswa1,
    'MAH002':mahasiswa2,
    'MAH003':mahasiswa3,
}

title = f"{'KEY':<6} {'Nama':<17} {'nim':10}{'SKS':<3} {'Beasiswa':<9} {'Lahir':<10}"

print(title)
print("-"*len(title))

for i in data_mahasiswa: #untuk setiap i di dalam dictionary data_mahasiswa
    KEY = i # setiap urutan yang terlooping akan kita catat ke dalam constant KEY
    
    # singkatnya, fungsi constant KEY adalah untuk menandakan bahwa looping akan berulang ke looping yang berikutnya tergantung berapa banyak nested dict yang ada di dalam satu dictionary
    
    NAMA = data_mahasiswa[KEY]['nama'] # buat constant baru dan masukkan constant KEY lalu dengan menambahkan key dari dictionary yang kita inginkan
    NIM = data_mahasiswa[KEY]['nim'] # lakukan hal yang serupa untuk key dictionary berikutnya
    SKS = data_mahasiswa[KEY]['sks_lulus'] # nantinya setiap dictionary akan mengecek seluruh key dimulai dari atas sampai bawah
    BEASISWA = data_mahasiswa[KEY]['beasiswa']
    LAHIR = data_mahasiswa[KEY]['lahir'].strftime("%d/%m/%Y") # pada bagian ini, kita menambahkan fungsi tambahan menggunakan .strftime() agar outputnya hanya menampilkan tanggal, bulan, dan tahunnya saja
    print(f"{KEY:<6} {NAMA:<17} {NIM:<10}{SKS:<3} {BEASISWA:^9} {LAHIR:<10}")
    
