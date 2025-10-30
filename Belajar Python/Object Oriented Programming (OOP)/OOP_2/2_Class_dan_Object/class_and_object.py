'''
- Class adalah blueprint atau template untuk membuat objek. Bayangkan class seperti cetakan kue, dengan satu cetakan kita bisa membuat banyak kue dengan bentuk yang sama
- Object adalah instance dari Class atau hasil "produksi" dari blueprint Class. Setiap object memiliki data dan behavior yang sama strukturnya, tapi valuenya bisa berbeda.
'''


'''
Class dengan Attributes
- Attributes adalah variabel yang menyimpan data dalam object

Class Attribute
- Instance attributes hanya akan ada di object hasil dari instansiasi dari class, dan tidak akan ada di object lain walaupun dari class yang sama
- Jika kita ingin membuat atribut yang secara default bawaan ada di semua object hasil insansiasi, maka kita perlu membuat Class Attribute, yaitu attribut yang didefinisikan di dalam classnya

Class dengan Methods
- Methods adalah function yang berada dalam class dan bisa dipanggil oleh object

Parameter self
- Parameter self sangat penting
- self adalah parameter khusus yang merujuk pada instance/object yang sedang memanggil method

Method dengan parameter
- Parameter di method tidak hanya self, kita bisa menambahkan parameter lain seperti function biasanya
- Semua yang bisa kita lakukan di function bisa kita lakukan juga di method

Naming Conventions/Cara penamaaan
- Class Names: PascalCase, misalnya Mahasiswa, MataPelajaran, Mobil, KategoriBarang
- Method Names: snake_case, misalnya perkenalan, lari_ke_depan, jalankan() dan lain-lain
- Attributes Names: snake_case, misalnya nama, nama_depan, nama_belakang, dan lain-lain
'''


# dalam pembuatan nama class, buatlah menggunakan huruf kapital di awal kalimatnya dan jika nama classnya lebih dari 2 kalimat maka jangan dipisahkan menggunakan spasi atau underscore, tetapi gunakan huruf kapital juga pada kalimat kedua seperti contoh: (IniClass) untuk membedakan saat pemanggilan class dan function

# Class/blueprint untuk pembuatan object Kampus
class Kampus:
    # class attribut
    name = ""
    alamat = ""

# Class/blueprint untuk pembuatan object Mahasiswa
class Mahasiswa:
    # class attribut
    nim = 0
    name = ""
    
    # method
    def perkenalan(self,): # self adalah referensi atau merujuk kepada objek saat ini yang menggunakan method ini
        print("Halo, nama saya {}".format(self.name))
    
    def hello(self,nama):
        print(f'Halo {nama}, nama saya {self.name}')
    

# cara membuat object dari class Kampus
kampus1 = Kampus()
kampus2 = Kampus()

# jika kita menggunakan perintah type pada sebuah object, maka kita dapat melihat tipe class dari objek tersebut
print(type(kampus1)) # tipe class = Kampus
print(type(kampus2))

# cara membuat object dari class Mahasiswa
mahasiswa1 = Mahasiswa()
# instance attributes
mahasiswa1.nim = 12345
mahasiswa1.name = "Budi"

# memanggil method perkenalan() dari class mahasiswa
mahasiswa1.perkenalan()
mahasiswa1.hello("Aisa")

mahasiswa2 = Mahasiswa()
mahasiswa2.nim = 12345
mahasiswa2.name = "Aisa"

# print(type(mahasiswa1)) # tipe class = Mahasiswa
# print(mahasiswa1.name) # memanggil atribut nama dari object mahasiswa1
# print(type(mahasiswa2))
