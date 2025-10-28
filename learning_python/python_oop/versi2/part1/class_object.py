'''
# Class dan Object

Class adalah blueprint atau template untuk membuat object.
Bayangkan Class sebagai cetakan kue - dengan satu cetakan, kita bisa membuat kue dengan banyak bentuk yang sama

Object adalah instance (hasil pembuatan) dari Class - hasil 'produksi' dari blueprint atau template dari Class.
Setiap Object memiliki data dan behavior yang strukturnya sama, tapi valuenya berbeda
'''


# cara membuat class
class Kampus:
    pass # class Kampur digunakan untuk membuat project kampus

class Mahasiswa:
    pass # class Mahasiswa digunakan untuk membuat object Mahasiswa

# ketika membuat class, disarankan untuk menggunakan kapital pada huruf pertamanya


## berikutnya kita akan membuat objectnya

# cara membuat object hampir sama seperti cara memanggil function
kampus1 = Kampus()  # dengan cara memasukannya ke dalam sebuah variabel
kampus2 = Kampus()  # nantinya variabel tersebut bisa kita sebut sebagai object

print(type(kampus1))    # tipe classnya berasal dari Kampus
print(type(kampus2))

mahasiswa1 = Mahasiswa()
mahasiswa2 = Mahasiswa()

print(type(mahasiswa1)) # tipe classnya berasal dari Mahasiswa
print(type(mahasiswa2))