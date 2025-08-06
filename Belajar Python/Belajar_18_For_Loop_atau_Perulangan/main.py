# Latihan perulangan (for loop)

# for kondisi:
#     aksi

# ini dengan list
angka = [0, 1, 2, 3] # ini adalah list

for i in angka: # i akan mengikuti nilai yang ada didalam variabel angka
    print(f"i sekarang adalah {i}")
    
print("Akhir dari program 1\n")

# in dengan range
angka_range = range(5) # saat diprint, angka yang keluar bukan dari 1, melainkan dari angka 0 dan seterusnya sampai angka 4 karena hitungannya 5 (walaupun angka 5 tidak termasuk)

for i in angka_range:
    print(f"i sekarang adalah {i}")
    
print("Akhir dari program 2\n")

angka_range = range(1, 10) # dalam parameter range, ada 3 input yang bisa dimasukkan, contoh: (1,10,2), keterangan: (start, stop, step) angka 1 berarti berapa nilai awalnya, lalu angka 10 berarti dimana nilainya akan berhenti, dan angka 2 berarti step atau berapa selang atau jarak antar nilai ketika diprint nanti

for i in angka_range:
    print(f"i sekarang adalah {i}")
    
print("Akhir dari program 3\n")

# menggunakan string

data_str = "saya ganteng abiez"

for huruf in data_str:
    print(huruf) # perintah ini akan melakukan print dari nilai atau string yang ada didalam variabel data_str, tetapi print nya berbentuk perulangan atau loop mulai dari huruf pertama sampai huruf terakhir menurun kebawah
    
print("Akhir dari program 4")


