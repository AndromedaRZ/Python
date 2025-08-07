# operasi list

data_angka = [1,5,8,4,1,3,4,6,2,8,9,4,7,3]

print(f"Data angka = \n{data_angka}")

# count data

jumlah_data_4 = data_angka.count(4) # digunakan untuk menghitung berapa banyak data yang kita inginkan yang berada di dalam sebuah list
jumlah_data_8 = data_angka.count(8) # kita tinggal memasukkan data yang ingin kita hitung jumlahnya menggunakan .count()
# perhitungan banyaknya data ini biasanya digunakan untuk statistika
print(f"Jumlah angka 4 = {jumlah_data_4}")
print(f"Jumlah angka 8 = {jumlah_data_8}")

# mengambil posisi data berdasarkan index

data = ["Zidane","Ryan","Herman","Luna"]
print(f"Data = {data}")

# tapi kita harus mengetahui dulu apa data yang kita inginkan
index_ryan = data.index("Ryan") # penulisan data di dalam .index() juga bersifat case sensitive jadi jangan sampai ada kata yang keliru
index_luna = data.index("Luna")

print(f"Index si Ryan = {index_ryan}") # maka kita bisa melihat data "Ryan" ada di index ke berapa
print(f"Index si Luna = {index_luna}") # maka kita bisa melihat data "Luna" ada di index ke berapa

# mengurutkan list (sorting)

# data angka
print(f"\nData angka sebelum disorting:\n{data_angka}")
data_angka.sort() # kita tinggal menambahkan .sort() di belakang nama variabel data list yang ingin kita sorting
print(f"\nData angka setelah disorting:\n{data_angka}") # maka hasilnya akan mengurutkan dari angka terkecil ke angka terbesar

# data string
print(f"\nData string sebelum disorting:\n{data}")
data.sort() # cara menggunakan .sort() sama seperti pada data angka
print(f"\nData string setelah disorting:\n{data}") # hasilnya akan mengurutkan berdasarkan abjad alfabet dari A sampai Z, fungsinya sama seperti mengabsen nama dan hal yang sama berlaku ke setiap data list string walaupun bukan menyimpan data nama

# data reverse
# fungsinya untuk membalikkan urutan data list dari aslinya
# tapi bisa kita gunakan juga untuk mengurutkan angka secara terbalik dan mengurutkan abjad dari Z ke A

data_angka.reverse() # kita tinggal menambahkan .reverse() pada variabel data list yang sudah kita sorting
data.reverse() # sehingga akan membuat urutannya menjadi terbalik

# hasilnya data angka akan mengurutkan dari angka terbesar ke angka terkecil
# dan data string akan mengurutkan dari abjad Z ke abjad A
print(f"\nData yang sudah direverse:\n{data_angka}\n{data}")