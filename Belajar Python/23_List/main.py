# --- LIST ---

# List berisi kumpulan data numbers
data_angka = [1, 5, 2, 3]
print(data_angka)

# List berisi kumpulan data string
data_string = ["otong", "ucup", "putri" ]
print(data_string)

# List berisi kumpulan data boolean
data_boolean = [True, False, True, True, False]
print(data_boolean)

# Liat berisi kumpulan data campuran (string, integer, dll)
data_campuran = [3, "ribu", 5, "bola"]
print(data_campuran)

# cara alternatif membuat list 
data_range = range(0, 10)
print(data_range)
data_list = list(data_range)
print(data_list)

# membuat list dengan for loop, list comprehension
list_for = [i**2 for i in range(0, 10)] # di dalam list dimasukan 'i' dimana 'i' untuk 'i' di dalam range (0 ,10)

# membuat list dengan menggunakan for loop dan if
list_for = [i for i in range(0, 10) if i != 5]
print(list_for)

list_for = [ i for i in range(0, 10) if i % 2 == 0] # hanya akan mengambil nilai genap dari angka 0 sampai dengan 10
print(list_for)

list_for = [ i for i in range(0, 10) if i % 2 != 0] # hanya akan mengambil nilai ganjil dari angka 0 sampai dengan 10
print(list_for)

