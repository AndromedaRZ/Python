# list
# menggunakan kurung siku
data_list = [2,1,5,10,6]

# tuples
# menggunakan kurung biasa
data_tuples = (1,3,5,7,9)

print(data_list)
print(data_tuples)

# apa perbedaan data list dan tuples?

# data tuples tidak bisa menggunakan assigntment untuk mengganti salah satu index di dalam list tuplesnya

# contoh dengan list
data_list[0] = 100 # kita mengubah index ke-0 menjadi 100
print(data_list) # maka outputnya akan ada perubahan data pada index ke-0

# jika kita menggunakan cara yang sama pada data tuples
# data_tuples[0] = 100

# maka outputnya akan menjadi error, menunjukkan bahwa kedua list tersebut memiliki fungsi yang berbeda

# kita juga tidak bisa menggunakan fungsi .append untuk list tuples

# bisa dikatakan bahwa fungsi tuples ini digunakan untuk memberitahu data fix yang tidak akan ada perubahan lagi, biasanya ketika ingin menunjukkan data akhir atau mengumpukan data akhir tanpa penelitian lebih lanjut lagi

# berikutnya adalah data sets

data_sets = {10,5,3,7,23,0}
# untuk data sets ini perbeaannya ada pada indexnya
# data sets tidak memiliki index data, kita bisa menyebutnya sebagai himpunan

print(data_sets)
# fungsi di bawah ini tidak akan berfungsi karena kita ingin menunjukkan isi dari index ke-0
# print(data_sets[0])
# padahal data sets tidak memiliki index sehingga hasilnya akan error

# akan tetapi untuk fungsi lainnya masih bisa digunakan layaknya list biasa
# hanya fungsi yang berhubungan dengan index saja yang tidak bisa digunakan