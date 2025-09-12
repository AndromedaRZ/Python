'''Lambda function'''

# lambda berguna untuk membuat kode program yang kita buat menjadi lebih simpel

def f_kuadrat(angka):
    return angka ** 2

print(f"hasil fungsi kuadrat = {f_kuadrat(3)}")

# dengan lambda
# output = lambda argument: expression

kuadrat = lambda angka : angka ** 2
print(f"hasil dari lambda kuadrat = {kuadrat(5)}")

pangkat = lambda num, pow : num ** pow
print(f"hasil lambda pangkat = {pangkat(4, 2)}")

## kegunaan dari lambda

# sorting untuk list
data_list = ['Luna','Zidane','Andre']
data_list.sort()
print(f"sorted list = {data_list}")

# sorting list pakai panjang (len())
data_list.sort(key = len)
print(f"sorted list by len = {data_list}")

# sorting pakai lambda
data_list = ['Luna','Zidane','Andre']
data_list.sort(key=lambda nama:len(nama))
print(f"sorted list by lambda = {data_list}")

# filter
data_angka = [1,2,3,4,5,6,7,8,9,10,11,12]

# contoh menggunakan fungsi
def kurang_dari_lima(angka):
    return angka < 5

data_angka_baru = list(filter(kurang_dari_lima,data_angka))

# contoh menggunakan lambda
data_angka_baru = list(filter(lambda x:x < 7, data_angka))

print(data_angka_baru)

# kasus genap
data_genap = list(filter(lambda x:(x % 2 == 0), data_angka))
print(data_genap)

# kasus ganjil
data_ganjil = list(filter(lambda x:(x % 2 != 0), data_angka))
print(data_ganjil)

# kelipatan 3
data_3 = list(filter(lambda x:(x % 3 == 0), data_angka))
print(data_3)

'''anonymous function'''
# currying <- Haskel Curry

def pangkat(angka, n):
    hasil = angka ** n
    return hasil

print(f"hasil perpangkatan dari fungsi biasa = {pangkat(5,2)}")

# dengan currying

def pangkat(n):
    return lambda angka:angka ** n

pangkat2 = pangkat(2)
print(f"pangkat 2 = {pangkat2(5)}")

pangkat3 = pangkat(3)
print(f"pangkat 3 = {pangkat3(3)}")

print(f"pangkat bebas = {pangkat(2)(3)}") # jika ditempatkan dalam 1 baris yang sama
# artinya 3 pangkat 2 karena angka di depan menunjukkan pangkatnya
# dan angka di belakang menunjukkan bilangannya