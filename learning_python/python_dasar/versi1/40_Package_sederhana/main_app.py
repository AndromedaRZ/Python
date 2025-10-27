# apa itu package?
# package adalah sebuah program atau tempat kita menaruh modul-modul kita

# cara memanggil package adalah dengan cara menggunakan fungsi import
import sains.matematika # sains ini adalah sebuah nama folder yang kita definisikan sebagai package-nya dan matematika adalah module yang ingin kita ambil

from sains import fisika # dari package sains kita mengimport module fisika
from sains.fisika import gaya as force # dari module fisika package sains kita mengimport fungsi gaya sebagai force

hasil_tambah = sains.matematika.tambah(1,2,3,4,5)
# cara menggunakannya dengan mengetik nama package (sains), lalu nama module (matematika) dan di dalam module matematika mengakses fungsi tambah
print(f"Hasil tambah dari package adalah = {hasil_tambah}")

gaya = fisika.gaya(90,10)
print(f"Gaya adalah = {gaya}")

gaya = force(90,10) # kita juga bisa memanggil fungsi dari module dan package dengan cara seperti ini
print(f"Gaya adalah = {gaya}") # karena pada saat mengimport-nya kita menggunakan alias

# Note:
# ketika kita menjalankan sebuah perintah import pada program file python kita
# maka pada direktori tempat file python tersebut berada akan otomatis membuat file baru bernama __pycache__
# __pycache__ ini berguna untuk menyimpan data agar bisa digunakan ulang oleh sistem ketika kita menjalankan program pythonnya kembali
# sehingga sistem tidak perlu repot-repot untuk mengambil data ulang dari package dan module yang kita gunakan berada
# sistem tinggal mengambil data yang disimpan di __pycache__ untuk mempersingkat waktu pengeksekusian file
# yang membuat program pythonnya akan berjalan sedikit lebih cepat dari pada sebelumnya
# __pycache__ ini berisi data-data yang hanya bisa dimengerti oleh mesin (machine readable)