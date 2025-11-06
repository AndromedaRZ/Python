'''
Apa itu Constructor?

- Constructor adalah method special yang otomatis dipanggil pada saat object dibuat
- Dalam Python, contructor adalah method __init__()
- Constructor digunakan untuk initialize (setup awal) object dengan data default yang diperlukan
'''

class Mahasiswa:
    nim = 0
    nama = ''
    
    def __init__(self, nama, nim):
        self.nama = nama
        self.nim = nim
        
# jika kita menggunakan initialize, pada saat pembuatan objectnya
# kita harus memasukkan argument untuk mengisi parameter yang tersedia
mhs1 = Mahasiswa('Ucup', 123)
print(mhs1.nama)
print(mhs1.nim)

# jadi pada saat kita membuat sebuah object
# maka __init__ akan otomatis terpanggil

'''Constructor dengan validation'''
# salah satu keuntungan menggunakan Constructor adalah kita bisa menambahkan validasi saat object pertama kali dibuat secara otomatis
# contohnya kita bisa cek nilai parameter, jika tidak valid, kita bisa raise error

class BankAccount:
    no = ''
    saldo = 0
    
    def __init__(self, no, saldo=0):
        # validasi saldo
        if saldo < 0:
            raise ValueError("Saldo tidak boleh negatif")
        
budi = BankAccount('12345', 1000)   # sukses
# anto = BankAccount('45678', -1000)  # error

