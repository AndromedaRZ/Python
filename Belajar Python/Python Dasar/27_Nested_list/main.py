# Nested list atau list di dalam list

data_0 = [1,2]
data_1 = [3,4]

data_list_biasa = [1,2,3,4]

print(f'list biasa = {data_list_biasa}')

list_2D = [data_0,data_1,data_list_biasa, "data_list_string", 3, 5] # di dalam data list ini kita bisa memasukkan list-list lainnya, kita juga dapat memasukkan nilai tipe data lain seperti integer dan string

print(f'list 2D = {list_2D}') # outputnya akan menjadi list didalam list 

# contoh penggunaan

peserta_0 = ["ucup", 25, "Laki-laki"]
peserta_1 = ["otong", 27, "Laki-laki"]
peserta_2 = ["Lisa", 23, "Wanita"]

list_peserta = [peserta_0, peserta_1, peserta_2]
print(f'peserta = {list_peserta}')

# print setiap nilai yang ada di dalam list_peserta
for peserta in list_peserta:
    print(f'nama = {peserta[0]}')
    print(f'umur = {peserta[1]}')
    print(f'gender = {peserta[2]}\n')
    
# beberapa operasi yang tidak bisa digunakan pada nested list

# dengan reference
list_copy = list_peserta.copy();
print(f'peserta = {list_copy}')

peserta_0[0] = "Michael"
print(f'peserta = {list_peserta}')
print(f'peserta = {list_copy}')

