# contoh mengimpor sebuah modul dari library python

import datetime

# dalam mengimpor sebuah library dalam python, 'datetime' adalah nama modulnya, lalu 'datetime' yang kedua adalah nama class dalam modul tersebut, dan yang terakhir 'now' adalah methodnya
data_waktu = datetime.datetime.now()
print(f'datetime now = {data_waktu}')
print(f'datetime tahun = {data_waktu.year}') # untuk mengspesifikan waktu yang dihasilkan menjadi tahun
print(f'datetime hari = {data_waktu.strftime('%A')}') # untuk mengspesifikan waktu yang dihasilkan menjadi hari

from collections import Counter

data = ['a', 'b', 'c', 'd', 'e', 'a', 'e', 'b', 'b', 'c', 'e', 'a']

# dengan mengimpor class 'Counter' dari library 'collections, kita bisa menghitung jumlah karater yang sama di dalam list di atas
data_count = Counter(data)
print(f'jumlah data = {data_count}')
print(f'jumlah data a = {data_count['a']}') # untuk menghitung jumlah data spesifik
print(f'jumlah data d = {data_count['d']}') # untuk menghitung jumlah data spesifik

# impor modul untuk membaca file
import io

file = io.open("file_text.txt", "r") # file yang ingin kita baca harus berada di folder terluar, tidak akan berfungsi jika berada di folder yang sama dengan file pythonya
print(file.read())