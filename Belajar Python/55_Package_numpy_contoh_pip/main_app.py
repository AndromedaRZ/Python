# Package pip sebagai contoh pip

# mengimpor package numpy dari pip
import numpy as np

list_a = [1, 2, 3, 4]
vector_a = np.array([1, 2, 3, 4])

print(f'list a = {list_a}')
print(f"vector a = {vector_a}")

'''
perbedaan dari list biasa dan list array numpy di atas adalah pada list numpy kita bisa menggunakan operasi pangkat pada bilangan di dalamnya
'''

# print(f'pangkat 2 = {list_a**2}') # akan error karena bilangan di dalam list tersebut tidak bisa menggunakan operasi aritmatika seperti pada numpy
print(f'pangkat 2 = {vector_a**2}') # dengan ini kita menggunakan operasi pangkat 2 pada setiap bilangan di dalam list tersebut
print(f'kali 2 = {vector_a*2}') # kita juga bisa menggunakan operasi aritmatika lainnya

# kita juga bisa membuat dua baris list di dalam satu list yang sama
matrix_b = np.array([(1, 2), (3, 4)])
print(f'matrix b = {matrix_b}')
print(f'matrix b x 2 = \n{matrix_b*2}')

zeros_c = np.zeros((2, 2))
print(f'zeros c = \n{zeros_c}')

ones_d = np.ones((2, 2))
print(f'ones d = \n{ones_d}')

# menjumlahkan seluruh operasi matrix tadi
jumlah = matrix_b + matrix_b**2 + ones_d
print(f'jumlah = \n{jumlah}') 