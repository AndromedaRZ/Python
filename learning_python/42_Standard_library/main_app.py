# apa maksudnya standard library?
# standard library adalah library umum bawaan python yang bisa kita gunakan

import datetime

data_waktu = datetime.datetime.now()
print(f"datetune now: {data_waktu}")
print(f"tahun: {data_waktu.year}") # kita bisa mengambil tahun dari data tersebut karena variabel data_waktu sifatnya menjadi object
print(f"tahun: {data_waktu.strftime('%A')}") # mengambil data hari

from collections import Counter
# count berguna untuk menghitung berapa banyak karakter di dalam suatu variabel

data = ['a', 'b', 'c', 'd', 'a', 'd', 'a']
data_count = Counter(data)

print(f"data count = {data_count}")
print(f"jumlah a = {data_count['a']}")
print(f"jumlah a = {data_count['d']}")

import io
# input/output

file = io.open("file_text.txt", "r") # membuka file eksternal
print(file.read()) # menampilkan isi dari file eksternal tersebut