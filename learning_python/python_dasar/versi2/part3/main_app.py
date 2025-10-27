# Operator
# operator adalah simbol yang digunakan untuk melakukan operasi pada variabel dan nilai

'''operator aritmatika'''
# digunakan untuk melakukan operasi matematika
# operator dasar:
# + -> tambah
# - -> kurang
# * -> kali
# / -> bagi

# operator pembagian bulat dan modulo:
# // -> pembagian bulat
# % -> modulo sisa pembagian

# operator pangkat:
# ** -> membuat perpangkatan

a = 10
b = 3

print(a + b)    # penjumlahan
print(a - b)    # pengurangan
print(a * b)    # pembagian
print(a / b)    # perkalian

print(a // b)   # pembagian bulat
print(a % b)    # mengambil sisa pembagian

print(a ** b)   # perpangkatan

# compund assignment
# adalah menggabungkan operator aritmatika dengan assignment

x = 10
print("Nilai awal x =", x)

x += 5  # fungsinya sama dengan: x = x + 5
print("Setelah += 5 =", x)

x = 10
x -= 5  # fungsinya sama dengan: x = x - 5
print("Setelah -= 5 =", x)

x = 10
x /= 5  # fungsinya sama dengan: x = x / 5
print("Setelah /= 5 =", x)

x = 10
x *= 5  # fungsinya sama dengan: x = x * 5
print("Setelah *= 5 =", x)

# operator perbandingan

print(a > b)    # Lebih besar: True atau False
print(a < b)    # Lebih kecil: True atau False
print(a >= b)   # Lebih besar atau sama dengan: True atau False
print(a >= b)   # Lebih kecil atau sama dengan: True atau False
print(a == b)   # Sama dengan: True atau False
print(a != b)   # Tidak sama dengan (bukan): True atau False

nama1 = 'Luna'
nama2 = 'Zeno'
nama3 = 'Luna'

# kita juga bisa menggunakan perbandingan ini pada string
print(nama1 == nama3)   # hasilnya True atau False
print(nama1 == nama2)   # hasilnya True atau False
print(nama1 != nama2)   # hasilnya True atau False

# operator logika
# digunakan untuk menggabungkan atau memodifikasi nilai boolean
# and (dan) -> menghasilkan True jika kedua kondisi True (terpenuhi)
# or (atau) -> menghasilkan True jika salah satu kondisi True (terpenuhi)
# not (tidak) -> membalik nilai boolean

# jika kondisi yang ada di and, or, maupun not tidak terpenuhi maka hasilnya akan menjadi False

umur = 20
print(umur > 18 and umur < 25) # True (20 > 18 dan 20 < 25 artinya kedua kondisi terpenuhi)

hari = 'Sabtu'
print(hari == 'Sabtu' or hari == 'Minggu') # True (karena salah satu kondisi terpenuhi)

aktif = True
print(not aktif) # akan menghasilkan 'False' karena itu adalah kebalikannya

# operator pada string
# kita juga bisa menggunakan operator pada string
# 1. Concatenation (+) -> menambah string
# 2. Repetition (*) -> mengulang string sejumlah angka
# 3. Membership (in), mengecek apakah teks ada di dalam string atau tidak (hasilnya adalah boolean: True atau False)

nama_depan = 'Mike'
nama_belakang = 'Tyson'

nama_lengkap = nama_depan + " " + nama_belakang # ini adalah concatenation
print(nama_lengkap)

kata = 'Hai'
print(kata * 5) # menggunakan repetition pada string

garis = '-'
print(garis * 30)

kalimat = "Python adalah bahasa pemrogramman"
print('Python' in kalimat)  # True -> karena kata 'Python' ada di dalam teks kalimat
print('Java' in kalimat)    # False -> karena kata 'Java' tidak ada di dalam teks kalimat
print('adalah' in kalimat)  # True -> karena kata 'adalah' ada di dalam teks kalimat

# prioritas operator
# operator atau operasi memiliki urutan prioritas (precedence). Operator dengan prioritas lebih tinggi akan dieksekusi lebih dulu
# urutan prioritas dari tinggi ke rendah:
# - ** (pangkat)
# - *, /, //, % (perkalian, pembagian, pembagian bulat, modulus)
# - +, - (penjumlahan, pengurangan)
# - ==, !=, <, >, <=, >= (perbandingan)
# - not (logika not)
# - and (logika and)
# - or (logika or)
