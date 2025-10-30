# import

# fungsi dari import adalah untuk mengambil program dari file eksternal .py

# 1. untuk menyambung program dari file eksternal dan menjalankannyaa
import program_print
import program_ucup

# 2. import dengan data
import variabel
import cukurukuk

# print(data) -> hasilnya akan error karena variabel data tidak terdefinisi

# 'data' berada di namespace 'variabel'

print(variabel.data) # maka dari itu kita tambahkan nama filenya yaitu 'variabel' lalu tambahkan titik dan nama variabel yang ingin dipanggil
print(cukurukuk.data) # kita juga harus menambahkan namespace pada fungsi import yang lain

# 3. import dengan fungsi dari file eksternal
import matematika

hasil = matematika.tambah(10, 5)
print(hasil)

# fungsi yang diambil harus berada di direktori yang sama dengan file python di mana kita menggunakan import tersebut