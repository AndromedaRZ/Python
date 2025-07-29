# Operasi manipulasi string

# 1. Menyambung string (Concatenate)
nama_pertama = "Ucup"
nama_tengah = "D"
nama_belakang = "Fame"

nama_lengkap = nama_pertama + " " + nama_tengah + "'" + nama_belakang
print(nama_lengkap)

# 2. Menghitung panjang string atau banyaknya jumlah karakter yang ada pada suatu string
panjang = len(nama_lengkap) # fungsi len() ini adalah menhitung berapa banyak karakter yang ada pada string, pada kasus ini kita menghitung berapa banyak seluruh karakter yang ada pada variabel nama lengkap
print("panjang dari " + nama_lengkap + " = " + str(panjang))
# pada baris di atas kita menggunakan konversi tipe data dari fungsi len() yang ada di variabel panjang menjadi string karena tipe data default dari fungsi len() adalah integer dan kita tidak bisa menggabungkannya ke dalam string sebelum diubah menjadi string

# 3. Operator untuk string
# Mengecek apakah komponen char atau string ada di dalam suatu string atau tidak

d = "d"
status = d in nama_lengkap # berfungsi untuk mengecek apalah data dari variabel d ada di dalam variabel nama_lengkap atau tidak
# jika ada maka hasilnya adalah True, jika tidak ada maka hasilnya adalah false
# fungsi in ini juga bersifat case sensitive
print("string " + d + " ada di " + nama_lengkap + " = " + str(status)) # hasilnya False karena huruf d kecil tidak ada di variaebl nama_lengkap

D = "D"
status = D in nama_lengkap
print("string " + D + " ada di " + nama_lengkap + " = " + str(status)) # hasilnya adalah True karena huruf D besar ada di dalam variaebl nama_lengkap

# berikutnya ada fungsi 'not in' dan berfungsi sebaliknya dari 'in'
d = "d"
status = d not in nama_lengkap
print("string " + d + " ada di " + nama_lengkap + " = " + str(status)) # hasilnya adalah True karena huruf d kecil tidak ada di dalam variabel nama_lengkap

# mengulang string
print(10*"wk")
print("wk"*5)

# indexing

print("index ke-0: " + nama_lengkap[0]) # memunculkan huruf ke atau index ke-0 dari variabel nama lengkap, outputnya adalah U karena itu huruf pertama dari nama Ucup D'Fame
# karena index dimulai dari angka 0
# berbeda dengan fungsi len() yang menghitung dari 1 sehingga jumlahnya menjadi 11
# pada kasus index ini karena 0 dimasukkan maka total panjangnya menjadi 10 dan bukan 11
print("index ke-10: " + nama_lengkap[10]) # outputnya adalah e karena itu adalah index ke-10 atau yang ke terakhir dari variabel nama_lengkap

'''
print("index ke 11: " + nama_lengkap[11]) # jika angkanya melebihi index, 11 misalnya, maka kodenya akan menjadi error
'''

print("index ke-(-1): " + nama_lengkap[-1]) # index ke (-1) artinya dimulai dari huruf paling terakhir maka outputnya akan menjadi e
# huruf pertamanya bisa juga dimasukkan sebagai index ke (-11) tetapi akan menjadi error ketika melebihi index juga yaitu index (-12)

print("index ke-[0:3]: " + nama_lengkap[0:4]) # outputnya huruf index ke 0 sampai 3, hanya saja pada kodenya perlu dibuat menjadi sampai index ke-4 karena nantinya index ke-3 tidak akan ikut ke-print

print("index ke-[3:7]: " + nama_lengkap[3:8]) # fungsinya hampir mirip dengan kode sebelumnya, hanya saja huruf pertama dimulai dari index ke-3 dan berakhir sampai index ke-7, pada kodenya juga kita harus membuatnya sampai index ke-8

print("index ke-[0,2,4,6,8,10]: " + nama_lengkap[0:11:2]) # bisa dilihat di kodenya, outputnya berasal dari index ke 0,2,4,6,8 dan 10
# tetapi ditambahkan angka 2 agar bisa melewatinya sebanyak 1 index

# item paling kecil
print("Paling kecil: " + min(nama_lengkap))
# item paling besar
print("Paling kecil: " + max(nama_lengkap))

# apa maksudnya dari item paling besar dan paling kecil? bisa dilihat pada ASCII code di bawah ini

ascii_code = ord(" ")
print("ASCII code untuk spasi adalah " + str(ascii_code))

data = 117
print("char untuk ASCII 117 adalah " + chr(data))

# 4. operator dalam bentuk method

data = "otong surotong pararotong"
jumlah = data.count("o") # fungsi .count digabung ke dalam variabel data sehingga disebut method dan bisa dikatakan variabel data menjadi objek
# .count juga berfungsi untuk menjumlahkan berapa banyak string huruf o yang ada di dalam variabel data
print("Jumlah o pada " + data + " = " + str(jumlah))