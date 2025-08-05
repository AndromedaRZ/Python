# eksperimen menggunakan librart datetime

from datetime import date

today = date.today()
print(today)
print(f"Today is {today:%A}")
print(f"Today is {date.today().strftime('%A')}")

# kedua fungsi print di atas sama-sama akan menampilkan keterangan hari apakah hari ini

# Dataset
data = [
    {"buah": "semangka", "ukuran": "besar"}, # index ke 0
    {"buah": "ceri", "ukuran": "kecil"}, # index ke 1
    {"buah": "jeruk", "ukuran": "sedang"} # index ke 2
]

for item in data:
    print(f"Buah {item["buah"]} berukuran {item["ukuran"]}")
    
# dalam perintah for item in data di atas, perintah for akan print data sebanyak isi dari data (3 kali), lalu akan melakukan print nama buah beserta ukurannya dari list di dalam variabel data, variabel data berisi list yang terdiri dari beberapa dictionary dimana setiap dictionary menyimpan informasi tentang nama buah ("buah") dan ukurannya ("ukuran")

print(data[0]) # akan print index ke 0 dari list di dalam data
print(data[1]) # akan print index ke 1 dari list di dalam data
print(data[2]) # akan print index ke 2 dari list di dalam data

