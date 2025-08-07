# Nested list (list di dalam list)

data_0 = [1,2]
data_1 = [3,4]

data_list_biasa = [1,2,3,4]

print(f"list biasa = {data_list_biasa}")

list_2d = [data_0,data_1] # kita memasukkan list data_0 dan data_1 ke dalam variabel yang sama
print(f"list 2d ={list_2d}") # lalu ketika kita print, outputnya akan terlihat bahwa list ini terdiri dari 2 list yang sudah kita masukkan

# contoh penggunaan list dalam list ini

peserta_0 = ["Ryan",19,"Laki-laki"]
peserta_1 = ["Zidane",20,"Laki-laki"]
peserta_2 = ["Luna",18,"Perempuan"]

list_peserta = [peserta_0,peserta_1,peserta_2] # bisa dibilang kita membuatnya menjadi list terpisah terlebih dahulu dan menggabungkannya ke list yang sama dengan list yang lain agar datanya tidak keliru
# mungkin termasuk pengkategorian
print(f"peserta = {list_peserta}")

for peserta in list_peserta:
    print(f"Nama\t: {peserta[0]}")
    print(f"Umur\t: {peserta[1]}")
    print(f"Gender\t: {peserta[2]}\n")
    # di atas adalah contoh penggunaan nested list untuk pengkategorian