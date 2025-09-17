# import menggunakan alias

from matematika import tambah as add
from matematika import kali as k
from matematika import pangkat as apa_saja_terserah

# alias menggunakan 'as' berguna untuk mengganti nama salah satu fungsi dari sebuah module yang kita import
# 'as' juga berguna untuk memudahkan pengetikan kita ketika menggunakan fungsi tersebut
# untuk aturan penamaan alias hampir mirip seperti cara penamaan variabel dan bersifat case sensitive

import matematika as math # <- nama module juga bisa kita ganti menggunakan alias
# hanya saja ketika menggunakan fungsinya tetap perlu menambahkan namespace-nya

hasil_tambah = add(1,2,3,4,5)
print(f"Hasil tambah = {hasil_tambah}")

hasil_kali = k(1,2,3,4,5)
print(f"Hasil kali = {hasil_kali}")

pangkat_3 = math.pangkat(3)
print(f"Pangkat 3 dari 3 = {pangkat_3(3)}")

pangkat_5 = apa_saja_terserah(5) # argument dari fungsi di baris ini adalah jumlah pangkat yang diinginkan
print(f"Pangkat 5 dari 2 = {pangkat_5(2)}") # dan argument dari fungsi di baris ini adalah angka yang ingin kita pangkatkan
