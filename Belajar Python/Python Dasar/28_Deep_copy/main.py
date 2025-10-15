# Deep copy

data_0 = [1,2]
data_1 = [3.4]

data_2D = [data_0, data_1, 9]
data_2D_copy = data_2D.copy()

print(f'data = {data_2D}')
print(f'data = {data_2D_copy}')

# mengambil data dari nested list

data = data_2D[0][0] # mengambil data atau nilai dari list nested atau list yang berada di dala list adalah dengan menggunakan dua kurung persegi, fungsi kode ini adalah untuk mengambil nilai index ke-0 dari dalam list data_0 yang ada di dalam list nested

'''
1.) Kurung persegi yang pertama adalah list nestednya, karena di dalam list nested tersebut berisi 2 list yang berbeda (data_0 dan data_1). Jadi, jika kita ingin mengambil data dari list pertama, maka kita bisa memasukkan index ke-0, dan jika kita ingin mengambil data dari list kedua, maka kita bisa menggunakan index ke-1, sementara itu
2.) Kurung persegi kedua adalah list di dalam list nested tersebut. Jadi, jika kita ingin mengambil suatu nilai dari list di dalam list nested tersebut, maka kita bisa menggunakan kurung persegi yang kedua ini untuk menentukan indeksnya
'''

print(f"data = {data}") # outputnya adalah angka 1

# address semua listnya
print(f'\naddress asli = {hex(id(data_2D))}') # address list nya akan berbeda dengan copynya
print(f'address copy = {hex(id(data_2D_copy))}') # address list nya akan berbeda dengan aslinya

print("\naddress dari member ke-1")
print(f'address asli = {hex(id(data_2D[0]))}') # address list di dalam list nestednya akan sama dengan copynya
print(f'address copy = {hex(id(data_2D_copy[0]))}') # address list di dalam list nestednya akan sama dengan aslinya

data_2D[1][0] = 5 # Jika kita merubah nilai list yang ada di dalam nested list, maka semua nilai list di dalamnya akan ikut berubah, saat list pertama dicopy, maka akan menyalin address yang sama juga
data_2D[2] = 2 # Jika kita hanya merubah satu nilai di dalam nested list yang bukan di dalam list, maka akan menghasilkan salinan yang berbeda
print(f'\ndata asli = {data_2D}')
print(f'data copy = {data_2D_copy}')

# solusinya menggunakan deepcopy

from copy import deepcopy

data_2D = [data_0, data_1, 9]
data_2D_deepcopy = deepcopy(data_2D)

# masih akan menghasilkan address yang berbeda
print(f'\naddress asli = {hex(id(data_2D))}') 
print(f'address copy = {hex(id(data_2D_deepcopy))}')

# akan menghasilkan address yang berbeda
print("\naddress dari member ke-1")
print(f'address asli = {hex(id(data_2D[0]))}')
print(f'address copy = {hex(id(data_2D_copy[0]))}')

# Sekarang, saat kita merubah nilai lsit yang ada di dalam list nested, maka hasil deepcopy tidak akan berpengaruh karena deepcopy benar-benar membuat salian data yang baru dari aslinya
data_2D[1][0] = 30
print(f'\ndata asli = {data_2D}')
print(f'data copy = {data_2D_copy}')
print(f'data deepcopy = {data_2D_deepcopy}')
