# Lambda function
'''berguna untuk membuat kode yang kita buat menjadi lebih simple'''

# fungsi biasa
def f_kuadrat(angka):
    '''fungsi kuadrat'''
    return angka ** 2

print(f"hasil kuadrat = {f_kuadrat(4)}")

# menggunakan lambda
# output = lambda argument:experssion

kuadrat = lambda angka:angka ** 2
print(f"hasil lambda kuadrat = {kuadrat(4)}")

pangkat = lambda num, rank: num ** rank
print(f"hasil lambda pangkat = {pangkat(10, 3)}")

# studi kasus penggunaan lambda

# sorting untuk list biasa
data_list = ["Ucup", "Nanang", "Andin"]
data_list.sort()
print(f"sorted list = {data_list}")


# sorting pakai panjang kata dari setiap indexnya
def panjang_nama(nama):
    return len(nama)

data_list.sort(key=panjang_nama)
print(f"sorted list by len/panjang = {data_list}")

# sort menggunakan lambda
data_list = ["Ucup", "Nanang", "Andin"]
data_list.sort(key=lambda nama:len(nama))
print(f"sorted list by lambda = {data_list}")

# filter
# memfilter angka yang besarnya kurang dari 5
data_angka = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

def kurang_dari_lima(angka):
    return angka < 5

data_angka_baru = list(filter(kurang_dari_lima, data_angka))
data_angka_baru = list(filter(lambda x:x<5, data_angka))

print(data_angka_baru)


# filter angka genap
data_genap = list(filter(lambda x:(x%2 == 0), data_angka))
print(data_genap)

# filter angka ganjil
data_ganjil = list(filter(lambda x:(x%2 != 0), data_angka))
print(data_ganjil)

# filter angka kelipatan 3
data_3 = list(filter(lambda x:(x%3 == 0), data_angka))
print(data_3)

# anonymous function
# currying <- diciptakan orang bernama haskell curry

# fungsi biasa

def pangkat(angka, n):
    hasil = angka ** n
    return hasil

data_hasil = pangkat(5, 2)
print(f"fungsi pangkat biasa = {data_hasil}")

# dengan currying

def pangkat(n):
    return lambda angka:angka ** n

pangkat2 = pangkat(2) # membuat fungsi untuk memangkatkan 2 suatu bilangan
print(f"pangkat2 = {pangkat2(5)}") # memangkatkan angka 5 dengan pangkat 2 yang tadi dibuat

pangkat3 = pangkat(3) # membuat fungsi untuk memangkatkan 3 suatu bilangan
print(f"pangkat3 = {pangkat3(5)}") # memangkatkan angka 5 dengan pangkat 3 yang tadi dibuat

pangkat2 = pangkat(2)
angka_pangkat = pangkat2(4)

print(f"4^2 = {pangkat2(angka_pangkat)}")