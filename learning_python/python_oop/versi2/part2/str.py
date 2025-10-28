'''Method __str__(): String Representation'''
# method __str__() digunakan untuk menentukan bagaimana object ditampilkan sebagai string

class Mahasiswa:
    nim = 0
    nama = ''
    
    def __init__(self, nama, nim):
        self.nama = nama
        self.nim = nim
        
    def __str__(self):
        return f"Mahasiswa nim: {self.nim}, nama: {self.nama}"

class Kampus:
    pass

    
mhs = Mahasiswa("Luna", "1234")
print(mhs)    # __str__ digunakan untuk menampilkan sesuatu jika kita menggunakan fungsi print pada objectnya langsung seperti ini

kampus1 = Kampus()
print(kampus1)  # ini adalah contoh jika kita tidak menggunakan __str__


'''Method untuk Object Comparison'''
# method __eq__() - Equality, bisa digunakan untuk membandingkan object dengan object yang lainnya
# saat kita menggunakan operator perbandingan ==, maka method inilah yang akan dipanggil

class Mahasiswa:
    nim = 0
    nama = ''
    
    def __init__(self, nama, nim):
        self.nama = nama
        self.nim = nim
        
    def __eq__(self, other):
        return self.nim == other.nim and self.nama == other.nama
    
mhs1 = Mahasiswa("Luna", "123456")
mhs2 = Mahasiswa("Luna", "123456")

print(mhs1 == mhs2) # hasilnya akan berupa boolean
# kita bisa menggunakan cara di atas untuk membandingkannya
# jika sama maka hasilnya akan True
# jika berbeda maka hasilnya akan False

mhs2.nim = '1234'
print(mhs1 == mhs2)