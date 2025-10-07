# jika kita belum memiliki package numpy
# maka kita perlu menginstallnya menggunakan pip

# pip install numpy

# numpy biasanya digunakan untuk operasi matematika, atau lebih tepatnya matriks

import numpy as np

# kita bisa membuat matriks menggunakan package numpy ini

# kita bandingkan dengan list
list_a = [1,2,3,4]
vector_a = np.array([1,2,3,4])
vector_b = np.array((1,2,3,4))
print(type(vector_b))
print(type(vector_a))

print(f"list_a = {list_a}")
print(f"vector_a = {vector_a}")

# perbedaannya adalah, vector a terlihat lebih rapi tanpa ada koma sebagai pemisahnya

# print(list_a ** 2) <- akan menjadi error
print(f"vector_a kuadrat = {vector_a ** 2}")

# kita bisa melakukan operasi pada vector_a, contohnya melakukan operasi kuadrat pada contoh di atas

print(f"vector_a kali 5 = {vector_a * 5}")

matrix_b = np.array([(1,2),(3,4)]) # membuat matrixnya menjadi 2 baris
print(f"matrix b =\n{matrix_b}")

print(f"matrix b^2 =\n{matrix_b ** 2}")

zeros_c = np.zeros((2,2)) # membuat matrix yang isinya 0 semua
print(f"zeros c =\n{zeros_c}")

ones_d = np.ones((2,2)) # membuat matrix yang isinya angka 1 semua
print(f"ones c =\n{ones_d}")

jumlah = matrix_b + matrix_b ** 2 + ones_d # kita juga bisa melakukan operasi pada matrix tadi
print(f"jumlah =\n{jumlah}")