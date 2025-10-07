# import statement

'''
import pada python digunakan untuk memanggil (menggunakan) kode dari luar file python kita, bisa berupa:
- Modul bawaan python (library standar seperti math, random, oss, dll)
- Modul buatan sendiri atau file python eksternal yang kita buat
- Modul dari pihak ketiga (library yang diinstal dengan pip seperti numpy, pandas, dll)

Dengan menggunakan import, kita tidak perlu lagi menulis ulang sebuah kode, tinggal ambil saja kode yang sudah pernah kita buat'''

# 1. untuk menjalankan program dari file eksternal
import program_print

# 2. import data dari file eksternal
import variabel

# data ada di namescape variabel
print(variabel.data) # cara mengambil data dari file lain menggunakan import adalah dengan mengetikan nama filenya (variabel) lalu ketikan data yang ada di dalam file tersebut di sebelah kanan nama filenya dan pisahkan dengan simbol titik

# variabel = namescapenya

# 3. import fungsi dari file eksternal
import matematika

hasil = matematika.tambah(1, 3) # cara mengambil fungsi dari file lain menggunakan import adalah dengan mengetikan nama filenya (matematika) lalu ketikan nama fungsi yang ada di dalam file tersebut di sebelah kanan filenya dan pisahkan dengan titik
print(f"hasil tambah = {hasil}")