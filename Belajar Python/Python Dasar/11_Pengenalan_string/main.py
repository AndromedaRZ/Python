# Pengenalan string dalam python

# 1. Cara membuat string

'''
1. Menggunakan tanda kutip tunggal/single quote (')
2. Menggunakan tanda kutip ganda/double quote (")
'''

data = "Menggunakan single quote"
print(data)

data = 'Menggunakan double quote'
print(data)

# Jika kita ingin memasukkan tanda kutip tunggal di dalam string, kita bisa menggunakan tanda kutip ganda di luar string seperti ini:
data = "\n'String ini menggunakan tanda kutip tunggal didalamnya'"
print(data)

# Begitupun sebaliknya
data = '"String ini menggunakan tanda kutip ganda didalamnya"'
print(data)

# 2. Menggunakan tanda backslash \

# Contoh kita ingin memasukkan tanda kutip tunggal (') di dalam string yang sudah menggunakan tanda kutip tunggal, maka bisa menggunakan backslash seperti berikut ini:
data = 'Hari ke-5 adalah hari Jum\'at'
print(data)

data = 'Good\'day isn\'t it?'
print(data)

# Contoh lainnya adalah jika kita ingin memasukkan tanda backslash (\) itu sendiri, maka bisa menggunakan backslash ganda seperti berikut ini:
data = 'C:\\Users\\NamaPengguna\\Documents'
print(data)

# Menggunakan tanda tab \t
print("ucup\totong, jadi berjauhan")

# Menggunakan backspace \b
print("ucup \botong, jadi berdekatan")

#  Menggunakan newline \n \r
print("baris pertama (\\n).\nbaris kedua.") # LN -> Line Feed > unix,macos,linux
print("baris pertama (\\r).\rbaris kedua.") # CR -> Carriage Return > commodore, acorn, lips
print("baris pertama (\\r\\n).\r\nbaris kedua.") # CRLF -> line feed carriage return > dipakai oleh windows

# 3. Menggunakan string literal atau raw

# Menggunakan raw string
# hati-hati jika menggunakan backslash seperti ini:
print("C:\new folder") # akan salah pathnya

# untuk menghindari hal tersebut, kita bisa menggunakan raw string dengan menambahkan huruf r di depan string
print(r"C:\new folder") # akan benar pathnya

# Multiline literal string
print("""
Nama : Doni
Kelas : 5 SD
""")

# Multiline literal string dan RAW
print(r"""
Nama   : Doni
Kelas  : 5 SD
Alamat : Jl. Raya No, 23 RT/RW 01/03
""")