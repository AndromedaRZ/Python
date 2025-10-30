'''struktur data'''
# struktur data (data structure) adalah cara untuk menyimpan dan mengorganisir data dalam program
# salah satu contohnya adalah menyimpan data atau nilai pada sebuah variabel
# selanjutnya kita akan mempelajari cara menyimpan banyak data atau nilai sekaligus
# dengan menggunakan struktur data

'''list (daftar)'''
# list adalah kumpulan data yang bisa menyimpan banyak nilai atau data dalam satu variabel
# list ditulis dengan menggunakan kurung siku '[]'

# list kosong
daftar_kosong = [] # kita bisa membuat data kosong seperti ini dengan menggunakan list
print(daftar_kosong)

# list dengan angka
angka = [1,2,3,4,5] # list yang berisi angka, setiap nilai atau angka harus dipisahkan dengan menggunakan koma
print(angka)

# list dengan string
nama = ['Luna', 'Voyager', 'Alex'] # list yang berisi teks atau string, setiap data harus dipisahkan dengan menggunakan koma
print(nama)

# list campuran
campuran = ['Annabel', 24, 'George', 28] # kita juga bisa membuat list yang berisi berbagai macam tipe data (data campuran)
print(campuran)

'''manipulasi list'''
# data yang ada di dalam list juga bisa kita modifkasi atau manipulasikan

# 1. mengakses data yang ada di dalam list dengan menggunakan index
# index pada list hampir mirip pada string, setiap index atau urutan yang ada di dalam list berisi data atau suatu nilai
# index pada list diawali dengan index 0
buah = ['Apel', 'Jeruk', 'Melon']
print(buah[0])      # Apel -> index ke-0
print(buah[1])      # Jeruk -> index ke-1
print(buah[2])      # Melon -> index ke-2
print(buah[-1])     # Melon -> memasukkan index negatif akan memulai perhitungan dari index terakhir

# 2. mengubah elemen pada list
# kita bisa menggunakan index untuk menandai data spesifik dan memasukkan nilai yang baru seperti mengubah nilai pada variabel
warna = ['Merah', 'Hijau', 'Biru']
print(warna)
warna[1] = 'Kuning' # mengubah data atau nilai yang ada pada index ke-1
print(warna)        # maka isi dari list tersebut akan berubah


# 3. menambah elemen atau data ke dalam list
# kita bisa menggunakan method 'append(<data>)' untuk menambahkannya ke index atau urutan yang terakhir
# atau menggunakan method 'insert(<index>, <data>)' untuk menambahkan data ke dalam index atau urutan yang kita inginkan
# ketika kita menambahkan data di tengah-tengah list, maka posisi atau index data yang lama akan bergeser
buah = ['Apel', 'Pisang']
print(buah)
buah.append('Durian') # append akan menambahkan data ke urutan terakhir
print(buah)

buah.insert(0, 'Melon') # sedangkan insert akan menambahkan data sesuai urutan index yang kita masukkan
print(buah)

# 4. menghapus elemen atau data di dalam list
# gunakan method 'remove(<data>)', data yang kita masukkan berarti menghapus data yang di dalam list tersebut
# atau gunakan 'pop()' untuk menghapus data pada index atau urutan terakhir yang ada di dalam list
# tapi, ketika kita menggunakan 'pop()' di dalam sebuah variabel
# maka data terakhir tersebut akan masuk ke dalam variabel terebut, jadi lebih tepatnya ini disebut mengambil data daripada menghapus
# data yang dihapus atau diambil akan membuat posisi atau index dari data lain yang ada di dalam list akan bergeser
buah.remove('Apel')     # menghapus data spesifik -> 'Apel'
print(buah)

data_diambil = buah.pop()      # mengambil data terakhir
print(buah)
print(data_diambil)

del buah[0] # menghapus data berdasarkan index
print(buah)

# 5. menghitung panjang list
# kita juga bisa menggunakan 'len(<list>)' untuk menghitung panjang data yang ada di dalam list
# hasinya adalah angka atau integer yang menunjukkan berapa banyak data atau nilai yang ada di dalam list tersebut
buah = ['Mangga', 'Semangka', 'Anggur', 'Nanas']
print(f"Panjang data list buah adalah: {len(buah)}")

# 6. menggabungkan list
# kita juga bisa menggabungkan list dengan list lain menggunakan simbol tambah (+)
satu = [1,2,3]
print(satu)

dua = [4,5,6]
print(dua)

gabungan = satu + dua      # menggabungkan list
print(gabungan)

# 7. for loop
# sama seperti string, kita juga bisa melakukan iterasi menggunakan for loop pada list untuk menampilan setiap data atau nilai
# yang tersimpan di dalam list tersebut
keranjang = ['Mangga', 'Semangka', 'Anggur', 'Nanas', 'Apel']
for buah in keranjang:
    print(buah)
    
# cara lain menggunakan for loop pada list
for i in range(0, len(keranjang)):
    print(keranjang[i]) # hasinya akan tetap sama
    
'''mengecek data apakah ada di dalam list atau tidak'''
# kita bisa menggunakan if-else
if 'Apel' in keranjang:
    print("Ada Apel")
else:
    print("Tidak ada Apel")
    
if 'Durian' in keranjang:
    print("Ada Durian")
else:
    print("Tidak ada Durian")
    