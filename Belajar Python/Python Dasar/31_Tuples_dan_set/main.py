# Tuples dan set

## TUPLES
# list
data_list = [1, 2, 3, 4] # menggunakan kurung siku
# tuples
data_tuples = (1, 2, 3, 4) # menggunakan kurung biasa

# sebelum diubah nilainya
print(data_list)
print(data_tuples)

# perbedaan data list biasa dengan data tuples adalah data tuples tidak bisa diubah isinya (immutable)

data_list[0] = 5
# data_tuples[0] = 5 # Jika kode ini diaktifkan maka akan menimbulkan error karena data_tupples tidak bisa diubah isinya

# sesudah diubah nilainya
print(data_list)
print(data_tuples)

# data tuples juga tidak bisa ditambahkan nilainya dengan menggunakan fungsi .append
data_list.append(8)
# data_tuples.append(8) # Jika kode ini diaktifkan maka akan menimbulkan error karena data_tuples tidak bisa menggunakan fungsi .append

# setelah ditambahkan nilai didalam listnya
print(data_list)
print(data_tuples) 

'''
data tuples dapat berguna ketika kita ingin mengirimkan program kita ke program lain, agar datanya tidak ada yang berubah maka kita bisa menggunakan data tuples
'''

## SETS (himpunan)
# sets adalah data yang mirip dengan list tetapi tidak memiliki index

data_sets = {1, 2, 3, 4, 5, 6, 7}
print(data_sets)

# karena data sets tidak memiliki index, kita tidak bisa mengambil index dari data sets
# print(data_sets[0]) # akan error jika diaktifkan

data_sets = {"ucup", "ucup", "ani", "ani", "dedi", "dedi"} # urutan data dalam sets juga tidak pasti
data_sets2 = {5, 5, 5, 2, 2, 2, 3, 3, 3, 4, 4, 4} # dalam data sets, tidak boleh ada nilai atau elemen yang sama dalam satu data sets tersebut. Jika ada yang sama, maka hanya akan mengambil satu nilai atau elemen yang sama tersebut
print(data_sets)
print(data_sets2)