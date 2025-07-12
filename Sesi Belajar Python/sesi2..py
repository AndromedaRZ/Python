# Data list
# Data list ini digunakan untuk memasukkan lebih dari satu nilai pada satu variabel

# Panjang data variabel kardus
#             1         2         3        4
# Dalam array list, ada yang namanya index
# index       0         1         2        3
kardus = ["semangka", "melon", "nanas", "durian"]
# print(len(kardus)) # Untuk menghitung panjang data dari variabel kardus
kardus.append("jeruk")
kardus.append("kelapa")

# Dalam data array list, kita bisa melakukan print pada satu nilai saja di dalam variabel kardus, contoh:
print(kardus)
print(kardus[4])
print(kardus[5 - 3])
# 5 - 3 = 2, ini setara dengan:
print(kardus[2]) # maka hasilnya tetap sama yaitu index ke 2 atau nanas
