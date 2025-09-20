# belajar import lebih dalam lagi

# cara kita menggunakan fungsi yang ada di dalam suatu module tergantung bagaimana cara kita mengimport packagenya
from ipa import matematika # as = alias/sebagai

# dari package ipa import module matematika

hasil_tambah = matematika.tambah(10,9,4) # ketika memanggil fungsinya, kita perlu menambahkan nama module tempat fungsi tersebut berasal sebagai namespace
print(f"Hasil tambah = {hasil_tambah}")

# --------------------------------------------------------------------
from ipa import fisika as fk
# dari package ipa import module fisika sebagai fk
# pada import pertama dan kedua, kita tidak perlu memanggil 'ipa' lagi untuk menggunakan fungsinya

hasil_berat = fk.berat(5, 9)
print(f"Hasil berat = {hasil_berat}")

# --------------------------------------------------------------------
from ipa.fisika import berat
# dari package ipa module fisika import berat
# jika menggunakan cara import yang ini, maka kita bisa langsung mengetik nama fungsinya tanpa perlu menambahkan namespace

hasil_berat2 = berat(20,5)
print(f"Hasil berat 2 = {hasil_berat2}")

# --------------------------------------------------------------------
import ipa
# import package ipa

# karena kita langsung mengimport package ipa
# maka ketika kita bisa mengakses semua module yang ada di package tersebut, dalam kasus ini berarti kita bisa mengakses module matematika dan fisika
# karena itu kita juga bisa menggunakan fungsi yang ada di dalam module matematika dan fisika

hasil_kali = ipa.matematika.kali(10,5) # caranya dengan mengetik nama package, module, dan fungsi yang akan digunakan
print(f"Hasil kali = {hasil_kali}")

hasil_gaya = ipa.fisika.gaya(100, 27) # caranya sedikit lebih panjang dari sebelumnya
print(f"Hasil gaya = {hasil_gaya}")

print(f"Hasil gaya 2 = {ipa.fisika.gaya(20, 4)}") # kelebihannya kita bisa mengakses seluruh fungsi yang ada di package tersebut

# pada akhirnya, cara memanggil dan menggunakan fungsi tadi tergantung dengan kebutuhan dan pengetahuan kita sendiri