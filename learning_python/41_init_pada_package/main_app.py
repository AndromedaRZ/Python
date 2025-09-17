import sains
from sains.matematika import scientific

# jika kita mencoba menjalankan program seperti sebelumnya, maka hasilnya akan error
# karena kita tidak bisa memanggil fungsi tambah dari module matematika dari package sains
# jika ingin kodenya berjalan, kita harus mengetik 'import sains.matematika' pada saat mengimport package
hasil_tambah = sains.matematika.tambah(1,2,3,4,5)
print(f"Hasil tambah = {hasil_tambah}")

# tapi ada alternatif lain
# kita tinggal menambahkan baris:
# from . import matematika
# di dalam file __init__.py
# maka cara memanggil fungsi, module, dan package di atas akan berfungsi

hasil_fisika = sains.fisika.gaya(50,10) # cara yang sama juga berlaku pada module yang lain
print(f"Hasil gaya = {hasil_fisika}")

hasil_kali = sains.matematika.kali(1,2,3,4,5)
print(f"Hasil kali = {hasil_kali}")

pangkat_3 = scientific.pangkat(3)
print(f"Hasil pangkat 3 = {pangkat_3(5)}")

# from sains import *
# # cara mengimport menggunakan * hanya bisa berfungsi ketika kita menambahkan __all__ di dalam file __init__.py

# hasil_tambah = sains.matematika.basic.tambah(1,2,3,4,5)
# print(f"Hasil tambah = {hasil_tambah}")

# hasil_fisika = sains.fisika.gaya(50,10)
# print(f"Hasil gaya = {hasil_fisika}")

# hasil_kali = sains.matematika.basic.kali(1,2,3,4,5)
# print(f"Hasil kali = {hasil_kali}")