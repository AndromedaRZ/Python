# Membuat package sederhana


'''
Package adalah sebuah program dimana kita menyimpan semua modul yang kita buat.

Tambahan:
Saat kita menggunakan import pada python, akan muncul sebuah folder bernama '_pycache' pada folder python kita, isi file tersebut adalah bytecode python dengan ekstensi .pyc, fungsi file tersebut adalah untuk mengingkatkan kecepatan eksekusi file python milik kita.
'''

# cara memanggil suatu modul dari dalam package (folder sains) adalah dengan memasukan 'nama_package.nama_module' contohnya seperti di bawah ini

import time
import sains.matematika
from sains import fisika
from sains.fisika import gaya as force

hasil_tambah = sains.matematika.tambah(1, 2, 3, 4)
print(f'hasil tambah = {hasil_tambah}')

gaya = fisika.gaya(10, 90)
print(f'gaya adalah = {gaya}')

gaya = force(10, 90)
print(f'gaya adalah = {gaya}')