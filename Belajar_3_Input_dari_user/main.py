# Mengambit data dari input user

data = input("Masukkan data: ")
# data yang diambil dari input user akan bertipe string
print("Data :", data, "bertipe: ", type(data))

# Untuk mengubah tipe data inputan user, kita bisa menggunakan fungsi bawaan Python
# seperti int() untuk mengubah menjadi integer, float() untuk mengubah menjadi float, dan bool() untuk mengubah menjadi boolean.

# Jika kita ingin mengambil data integer
data_int = int(input("Masukkan data integer: "))
print("Data: ", data_int, "bertipe: ", type(data_int))

# Jika kita ingin mengambil data float
angka = float(input("Masukkan data float: "))
print("Data: ", angka, "bertipe: ", type(angka)) 

# Jika kita ingin mengambil data boolean
# Untuk mengambil input 1 dan 0 sebagai boolean, kita harus mengkonversinya ke integer terlebih dahulu
# karena input() akan mengembalikan string, lalu kita bisa mengkonversinya ke integer lalu ke boolean
# Jadi, input 1 akan menjadi True dan input 0 akan menjadi False
biner = bool(int(input("Masukkan data boolean 1/0: ")))
print("Data: ", biner, "bertipe: ", type(biner))