'''
# Class dengan attributes

Attributes adalah variables yang menyimpan data di dalam object
(menambahkan karakteristik ke dalam object)

'''

class Mahasiswa():
    pass


# membuat object menggunakan class (template) dari Mahasiswa
mahasiswa1 = Mahasiswa()

'''Instance Attributes'''
# (attribute yang menempel di objectnya)

# cara membuatnya dengan mengetik nama object, lalu titik, dan nama variabel atau attribute yang ingin ditambahkan
mahasiswa1.nim = '12345'
mahasiswa1.nama = 'Luna'

# untuk menampilkan attributenya
# kita tinggal menggunakan fungsi print lalu masukkan nama object, lalu titik, dan nama attribute yang ingin ditampilkan
print(mahasiswa1.nim)
print(mahasiswa1.nama)

# instance attribute yang kita buat tadi hanya menempel di salah satu object saja
# artinya attribute tersebut tidak akan ada di object lain walaupun dari class yang sama
# cara menambahkan attribute seperti ini tidak direkomendasikan


# maka kita perlu membuat Class Attribute, yaitu attribute yang akan didefinisikan di dalam classnya
# sehingga kita bisa membuat attribute default yang sama untuk semua object hasil instanisasi

'''Class Attribute'''

class Kampus:
    nama = ''
    alamat = ''
    
kampus1 = Kampus()
print(kampus1.nama)
print(kampus1.alamat)
# secara otomatis, semua object yang kita buat akan memiliki attribute yang sama
# (yaitu attribute 'nama' dan 'alamat')


class Mahasiswa:
    nim = 0
    nama = ''
    
mahasiswa1 = Mahasiswa()
print(mahasiswa1.nim)
print(mahasiswa1.nama)
# secara otomatis, semua object yang kita buat akan memiliki attribute yang sama
# (yaitu attribute 'nim' dan 'nama')


'''Class dengan Method'''
# methods adalah function yang berada di dalam class dan bisa dipanggil oleh object

class Mahasiswa:
    nim = 0
    nama = ''
    
    def perkenalan(self):
        # arti dari parameter self, adalah referensi ke dalam si object saat ini
        # hampir mirip seperti parameter pada function
        print(f"Halo nama saya {self.nama}")
        
        
mahasiswa1 = Mahasiswa()
mahasiswa1.nama = 'Arya'
mahasiswa1.perkenalan() # ini adalah cara menggunakan method yang tadi dibuat
# walaupun kita membuat semacam fungsi di dalam class tadi
# tapi cara memanggilnya mirip seperti method pada biasanya

# semua object yang dibuat dari class Mahasiswa bisa menggunakan method perkenalan
# karena mereka berbagi mehtod yang sama dengan template yang sama

# note:
# parameter 'self' sangat penting pada saat pembuatan method
# 'self' adalah parameter khusus yang merujuk pada instance/object yang sedang memanggil method
# ini juga menunjukkan perbedaan method dengan function yang tidak menggunakan class

'''Method dengan Parameter'''
# bagaimana jika kita ingin menambahkan parameter lain selain 'self' ke dalam function atau methodnya?
# jawabannya, bisa
# parameter di method tidak hanya self, kita bisa menambahkan parameter lain seperti function biasanya
# dan semua yang bisa kita lakukan di function juga bisa kita lakukan di method
# namun, perbedaannya jika ingin memasukkan parameter lain ke dalam methodnya
# parameter pertama harus diisi dengan 'self'

class Mahasiswa:
    nim = 0
    nama = ''
    
    def perkenalan(self):
        print(f"Halo, nama saya {self.nama}")
        
    def hello(self, nama):
        print(f"Halo {nama}, nama saya {self.nama}")
        
        
mahasiswa1 = Mahasiswa()
mahasiswa1.nama = 'Isla'
mahasiswa1.perkenalan()
mahasiswa1.hello('Tsukasa') # pada saat menggunakan method 'hello', kita perlu memasukkan argument

'''Naming Conventions'''
# penamaan yang disarankan
# Class Names: PascalCase
# -> misal mahasiswa, MataPelajaran, Mobil, KatehgoriBarang
# huruf awal setiap kata harus menggunakan kapital dan tanpa menggunakan spasi jika lebih dari satu kata

# Mehtod Names: snake_case (mirip seperti function)
# -> misal perkenalan(), lari_ke_depan(), jalankan(), dll
# menggunakan huruf kecil semua dan dipisahkan menggunakan garis bawah jika lebih dari satu kata

# Attributes Names: snake_case
# -> misal nama, nama_depan, nama_belakang, dll