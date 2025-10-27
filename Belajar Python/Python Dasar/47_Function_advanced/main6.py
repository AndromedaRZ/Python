'''
8) ANONYMUS DAN LAMBDA FUNCTION

Anonymus function adalah fungsi yang tidak memiliki nama, dalam python, anonymus dibuat dengan keyword lambda makanya disebutnya lambda function, lambda function juga bisa mempersingkat kode kita agar terlihat lebih simple dan tidak memakan banyak baris kode
'''

# fungsi biasa
def f_kuadrat(angka):
    '''fungsi kuadrat'''
    return angka ** 2

print(f"hasil kuadrat = {f_kuadrat(4)}")

# menggunakan lambda
'''
Aturan menggunakan lambda function

lambda parameter: ekspresi

lambda --> kata kunci
parameter --> input ke fungsi
ekspresi --> hasil yang dikembalikan (return otomatis, tidak perlu menambahkan return lagi)
'''

# contoh
# fungsi kuadrat
kuadrat = lambda x:x ** 2 
print(f"hasil lambda kuadrat = {kuadrat(4)}") # akan berfungsi sama seperti fungsi yang kita buat di atas tadi tetapi dengan fungsi lamda akan meringkas kode yang kita buat

# fungsi tambah
tambah = lambda a, b: a + b
print(f"hasil lambda tambah = {tambah(5, 6)}") 

# fungsi kurang
kurang = lambda c, d:c - d
print(f"hasil lambda kurang = {kurang(8, 4)}")

# studi kasus lainnya menggunakan lambda

# sorting
# sorting untuk list biasa 
data = ["Budi", "Aisa", "Lucia", "Eka", "Yusuf"]
print(f"\nsebelum disortir = {data}")
data.sort()
print(f"sesudah disortir = {data}")

# sorting sesuai panjang namanya (panjang nama terpendek)
def panjang_nama(nama):
    return len(nama)

data.sort(key = panjang_nama)
print(f"sorting sesuai panjang namanya = {data}")

# sort menggunakan lambda
data = ["Budi", "Aisa", "Lucia", "Eka", "Yusuf"]
data.sort(key=lambda nama:len(nama))
print(f"disortir menggunakan lambda = {data}")

# filter

data_angka = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# filter angka genap biasa

def genap(angka):
    '''fungsi memilah angka genap'''
    return angka % 2 == 0

data_angka_baru = list(filter(genap, data_angka))
print(f"\nfilter angka genap biasa = {data_angka_baru}")

# filter angka genap menggunakan lambda
data_angka_baru = list(filter(lambda x:( x % 2 == 0), data_angka))
print(f"filter angka genap dengan lambda = {data_angka_baru}")

'''
seperti yang dapat kita lihat di atas, lambda function membuat kode yang kita buat menjadi lebih simple dan tidak memakai banyak baris kode. Agar lebih jelas lagi, perhatikan beberapa contoh studi kasus di bawah ini
'''

# filter angka ganjil
data_angka_baru = list(filter(lambda x:( x % 2 != 0), data_angka))
print(f"filter angka ganjil dengan lambda = {data_angka_baru}")

# filter angka kelipatan tiga
data_angka_baru = list(filter(lambda x:(x % 3 == 0), data_angka))
print(f"filter angka kelipatan tiga dengan lambda = {data_angka_baru}")

# filter angka kurang dari 5
def kurang_dari(n):
    return lambda x: x < n

kurang_dari_5 = kurang_dari(5)

data_angka_baru = list(filter(kurang_dari_5, data_angka))
print(f"filter angka kurang dari 5 = {data_angka_baru}")

'''
Anonymus
'''

# currying, Currying adalah teknik memecah sebuah fungsi yang punya banyak parameter menjadi beberapa fungsi yang masing-masing hanya menerima satu parameter.

# fungsi pangkat
# fungsi biasa

def pangkat(angka, n):
    hasil = angka ** n
    return hasil

data_hasil = pangkat(5, 2)
print(f"\nfungsi pangkat biasa = {data_hasil}")

# menggunakan currying
def pangkat(n):
    return lambda angka:angka ** n

pangkat2 = pangkat(2) # membuat fungsi terpisah untuk memangkatkan 2 suatu bilangan atau angka
print(f"pangkat dua (currying) = {pangkat2(5)}") # memangkatkan angka 5 dengan pangkat 2 yang tadi dibuat

pangkat3 = pangkat(3) # membuat fungsi terpisah untuk memangkatkan 3 suatu bilangan atau angka
print(f"pangkat tiga (currying) = {pangkat3(5)}") # memangkatkan angka 5 dengan pangkat 3 yang tadi dibuat

# fungi penjumlahan 3 angka
# fungsi biasa
def tambah(a, b, c):
    return a + b + c

print(f"fungsi tambah biasa = {tambah(1, 2, 3)}")

# menggunakan currying
def tambah(a):
    def angka1(b):
        def angka2(c):
            return a + b + c
        return angka2
    return angka1

print(f"fungsi tambah (currying) = {tambah(1)(2)(3)}")
            
# fungsi kali
# fungsi biasa

def kali(a, b):
    return a * b

print(f"fungsi kali biasa = {kali(10, 3)}")

# menggunakan currying (perkalian bertahap)

def kali(n):
    return lambda x:x * n

kali2 = kali(2)
kali3 = kali(3)

print(f"Menggunakan currying kali 2 = {kali2(5)}")
print(f"Menggunakan currying kali 3 = {kali3(5)}")