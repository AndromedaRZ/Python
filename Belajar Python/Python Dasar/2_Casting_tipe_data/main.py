# Casting tipe data
# Merubah tipe data ke tipe data lain
# tipe data: int, float, str, bool

# Mengubah tipe data integer ke float, str, dan bool
print("\nCasting tipe data integer\n")

data_int = 30
print("data: ", data_int, "bertipe:", type(data_int))

print("\nDiubah ke tipe data float, str, dan bool")
print("     V     V     V     ") 

data_float = float(data_int)
data_str   = str(data_int)
data_bool  = bool(data_int)
print("data: ", data_float, "bertipe:", type(data_float)) # data int akan berubah menjadi float (angka desimal/berkoma)
print("data: ", data_str, "bertipe:", type(data_str)) # data int akan berubah menjadi string atau karakter 
print("data: ", data_bool, "bertipe:", type(data_bool)) # true karena data_int tidak 0, jika data_int = 0 maka akan False

# Mengubah tipe data float int, str, dan bool
print("\nCasting tipe data float\n")

data_float = 30.5
print("data: ", data_float, "bertipe:", type(data_float))

print("\nDiubah ke tipe data int, str, dan bool")
print("     V     V     V     ")

data_int = int(data_float)
data_str = str(data_float)
data_bool = bool(data_float)
print("data: ", data_int, "bertipe:", type(data_int)) # data float akan berubah menjadi int (angka bulan/satuan)
print("data: ", data_str, "bertipe:", type(data_str)) # data float akan berubah menjadi string atau karakter
print("data: ", data_bool, "bertipe:", type(data_bool)) # true karena data_float tidak 0.0, jika data_float = 0.0 maka akan False

# Mengubah tipe data string ke int, float, dan bool
print("\nCasting tipe data string\n")

data_str = "50" # string yang berisi angka, akan error jika string berisi huruf atau karakter lain
print("data: ", data_str, "bertipe:", type(data_str))

print("\nDiubah ke tipe data int, float, dan bool")
print("     V     V     V     ")

data_int = int(data_str)
data_float = float(data_str)   
data_bool = bool(data_str) # true karena data_str tidak kosong, jika data_str = "" maka akan False
print("data: ", data_int, "bertipe:", type(data_int)) # data string akan berubah menjadi int atau angka bulat
print("data: ", data_float, "bertipe:", type(data_float)) # data string akan berubah menjadi float atau angka desimal/berkoma
print("data: ", data_bool, "bertipe:", type(data_bool)) # true karena data_str tidak kosong, jika data_str = "" maka akan False

# Mengubah tipe data boolean ke int, float, dan str
print("\nCasting tipe data boolean\n")  

data_bool = True
data_bool2 = False
print("data: ", data_bool, "bertipe:", type(data_bool))
print("data: ", data_bool2, "bertipe:", type(data_bool2))

print("\nDiubah ke tipe data int, float, dan str")
print("     V     V     V     ")

data_int = int(data_bool) # jika True menjadi 1
data_int2 = int(data_bool2) # jika False akan menjadi 0
data_float = float(data_bool) # True menjadi 1.0
data_float2 = float(data_bool2) # jika False akan menjadi 0.0
data_str = str(data_bool) # True menjadi "True", False menjadi "False"
data_str2 = str(data_bool2) # jika False akan menjadi "False"
print("data: ", data_int, "bertipe:", type(data_int)) # data boolean akan berubah menjadi int
print("data: ", data_int2, "bertipe:", type(data_int2))
print("data: ", data_float, "bertipe:", type(data_float)) # data boolean akan berubah menjadi float
print("data: ", data_float2, "bertipe:", type(data_float2))
print("data: ", data_str, "bertipe:", type(data_str)) # data boolean akan berubah menjadi string   
print("data: ", data_str2, "bertipe:", type(data_str2))

# Catatan:
# - Jika tipe data tidak sesuai, akan terjadi error saat casting.  
# - Pastikan data yang akan di-cast sesuai dengan tipe data yang diinginkan.
# - Casting tidak mengubah nilai asli, hanya membuat salinan dengan tipe data baru.
# - Casting dapat digunakan untuk menghindari error saat operasi antar tipe data yang berbeda.
# - Casting dapat digunakan untuk mengubah tipe data sesuai kebutuhan program.