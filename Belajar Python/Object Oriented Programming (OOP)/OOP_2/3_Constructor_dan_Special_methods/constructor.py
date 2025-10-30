'''
Apa itu Constructor?
- Constructor adalah method spesial yang otomatis dipanggil saat object dibuat
- Dalam python, constructor adalah method __init__()
- Constructor digunakan untuk initialize (setup awal) object dengan data yang diperlukan

Constructor dengan Validation
- Salah satu menggunakan consructor adalah, kita bisa menambahkan validasi saat objek pertama kali dibuat secara otomatis
- Contohnya misal kita bisa cek nilai dari parameter, jika tidak valid, kita bisa raise error

Method __str__() - String Representation
- Method __str__() menentukan bagaimana objek ditampilkan sebaga string

Method untuk Object Comparison
- Method __eq__() - Equality, bisa digunakan untuk membandingkan object dengan object lainnya
- Saat kita menggunakan operator perbandingan ==, maka method ini yang akan dipanggil

Method comparison lainnya
__it__(self, other) untuk < (kurang dari)
__gt__(self, other) untuk > (lebih dari)
__le__(self, other) untuk <= (kurang atau sama dengan dari)
__ge__(self, other) untuk <= (lebih atau sama dengan dari)

'''

# tanpa consructor
class Siswa:
    nik = 0
    nama = ""
    
    def setup(self, nik, nama): # manual setup
        self.nik = nik
        self.nama = nama
        
        
siswa1 = Siswa()
siswa1.setup(12345, "Doni")

# print(siswa1.__dict__)

# dengan constructor
class Mahasiswa:
    nim = 0
    nama = ""
    
    def __init__(self, nim, nama): # manual setup
        self.nim = nim
        self.nama = nama
    
    # method __str__(), untuk representasi string
    def __str__(self): # akan menampilkan objek sebagai string
        return f"Mahasiswa : {self.nim} - {self.nama}"
    
    # method __eq__(), untuk perbandingan
    def __eq__(self, other): # akan membandingkan kedua object apakah nilainya sama atau tidak
        return self.nim == other.nim and self.nama == other.nama
        
mahasiswa1 = Mahasiswa(12345, "Agus")
mahasiswa2 = Mahasiswa(12345, "Agus")
print(mahasiswa1 == mahasiswa2)


# construcor dengan validator
class BankAccount:
    no = ""
    saldo = 0
    
    def __init__(self, no, saldo=0): # saldo=0 adalah nilai defaultnya
        # validasi saldo
        if saldo < 0: # raise error 
            raise ValueError("Saldo tidak boleh negatif")
        
        self.no = no
        self.saldo = saldo

budi = BankAccount("12345678", 500000) # sukses
# eko = BankAccount("123456", -10000) # error karena nilai saldo negatif 