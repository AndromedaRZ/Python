# operasi dan manipulasi string

# 1. menyambung string (concatenate)

nama_depan = "ucup"
nama_tengah = "D"
nama_belakang = "Fame"

nama_lengkap = nama_depan + " " + nama_tengah + "'" + nama_belakang
print("Nama lengkap:", nama_lengkap)

# 2. menghitung panjang karakter string
panjang_nama = len(nama_lengkap)
print("Panjang dari " + nama_lengkap + " = " + str(panjang_nama))

# 3. operator untuk string
# mengecek apakah ada komponen char atau string lain di dalam string

# mengecek apakah ada karakter string "d" di dalam string nama_lengkap
d = "d"
status = d in nama_lengkap
print("string " + d + " ada di " + nama_lengkap + " = " + str(status))

# mengecek apakah ada karakter string "D" di dalam string nama_lengkap
D = "D"
status = D in nama_lengkap
print("string " + D + " ada di " + nama_lengkap + " = " + str(status))

# mengecek apakah ada karakter string "d" di dalam string nama_lengkap, jika tidak ada maka hasilnya True
d = "d"
status = d not in nama_lengkap
print("string " + d + " tidak ada di " + nama_lengkap + " = " + str(status))

# mengulang string
print("wkwk" * 10)

# indexing
# mengambil karakter dari setiap index pada string nama_lengkap
print("index ke-0 : " + nama_lengkap[0])
print("index ke-1 : " + nama_lengkap[1])
print("index ke-2 : " + nama_lengkap[2])

# mengambil dari index 0 sampai 3 (tidak termasuk index ke-3)
print("index ke-[0-3] : " + nama_lengkap[0:3])

# jika kita ingin mengambil index ke-3 sampai 7, maka kita bisa mengambilnya dari index ke-3 sampai 8 (index ke-8 tidak termasuk)
print("index ke-[3-8] : " + nama_lengkap[3:8]) 

# mengambil index ke-0,2,4,6,8,10 dengan cara memasukkan angka index awal (0), lalu angka index akhir (10), dan step atau jarak setiap index (2)
print("index ke-[0,2,4,6,8,10] : " + nama_lengkap[0:10:2])

# mengambil item paling kecil
print("paling kecil : " + min(nama_lengkap))

# mengambil item paling besar
print("paling besar : " + max(nama_lengkap))

# ascii code

# memeriksa ascii code dari suatu karakter
ascii_code = ord(" ") # mengambil kode ascii dari karakter spasi
print("ASCII code untuk spasi adalah " + str(ascii_code))

# memeriksa karakter dari ascii code
data = 117
print(f"karakter untuk ascii code {data} adalah {chr(data)}")

# 4. operator dalam bentuk method

data = "otong surotong pararotong"
jumlah = data.count("o") # menghitung jumlah karakter "o" dalam string 'data'
print(f"jumlah karakter 'o' dalam string '{data}' adalah {jumlah}") 