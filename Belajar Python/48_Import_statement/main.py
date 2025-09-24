# import statement

# salah satu fungsi import adalah untuk mengambil program dari file eksternal (.py)

# 1. untuk menjalankan program dari file eksternal
import program_print

# 2. import dengan data
import variabel

# data ada di namescape variabel
print(variabel.data) # cara mengambil data dari file lain menggunakan import adalah dengan mengetikan nama filenya (variabel) lalu ketikan data yang ada di dalam file tersebut di sebelah kanan nama filenya dan pisahkan dengan simbol titik

# variabel = namescapenya

# 3. import dengan fungsi
import matematika

hasil = matematika.tambah(1, 3) # cara mengambil fungsi dari file lain menggunakan import adalah dengan mengetikan nama filenya (matematika) lalu ketikan nama fungsi yang ada di dalam file tersebut di sebelah kanan filenya dan pisahkan dengan titik
print(f"hasil tambah = {hasil}")