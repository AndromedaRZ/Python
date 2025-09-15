data_0 = [1,2]
data_1 = [3,4]

data_2d = [data_0, data_1,10]
data_2d_copy = data_2d.copy()

print(f"Data = {data_2d}")
print(f"Data copy = {data_2d_copy}")

# mengambil data dari nested list

data = data_2d[0][1] # mengambil isi data list dari index ke 1 di dalam nested list index ke 0
# [0] adalah lokasi index nested listnya, sementara [1] adalah lokasi di dalam nested list index ke-0 dan kita mengambil data dari index ke-0
print(f"Data = {data}")

# mengecek address semuanya
print(f"Address asli = {hex(id(data_2d))}")
print(f"Address copy = {hex(id(data_2d_copy))}") # address dari kedua 'list' di atas terlihat berbeda



print("\nAddress dari index ke-0")
print(f"Address index ke-0 asli = {hex(id(data_2d[0]))}") # tetapi address dari index di dalamnya (contohnya index ke-0) dari kedua data list tersebut masih sama 
print(f"Address index ke-0 copy = {hex(id(data_2d_copy[0]))}")

data_2d[0][1] = 5 # sehingga menyebabkan data copy pada index ke-0 dari list ke-0 akan ikut berubah mengikuti index ke-0 dari data list aslinya
data_2d[2] = 9 # tetapi jika komponennya bukan sebuah list maka perubahannya tidak akan mempengaruhi data list copynya
print(f"Data = {data_2d}")
print(f"Data copy = {data_2d_copy}")

# untuk mencegah hal tersebut, kita bisa mengunakan yang namanya 'deepcopy' agar index yang ada di dalam listnya pun memiliki address yang berbeda

# deepcopy

from copy import deepcopy

data_0 = [1,2]
data_1 = [3,4]

data_2d = [data_0, data_1,10]
data_2d_copy = data_2d.copy()

data_2d = [data_0,data_1,10]
data_2d_deepcopy = deepcopy(data_2d) # variabel data_2d kita salin menggunakan 'deepcopy' dan memasukannya ke variabel yang baru

print(f"\nAdress asli = {hex(id(data_2d))}")
print(f"Adress deepcopy = {hex(id(data_2d_deepcopy))}") # address list yang asli dan deepcopy sudah berbeda

print("Address dari index ke-0")
print(f"\nAddress index ke-0 yang asli = {hex(id(data_2d[0]))}")
print(f"Address index ke-0 yang deepcopy = {hex(id(data_2d_deepcopy[0]))}") # begitupun address pada index ke-0 keduanya juga sudah berbeda

data_2d[1][0] = 20 # jika kita mengubah index ke-0 dari data nested list index ke-1
print(f"\nData = {data_2d}")
print(f"Data copy = {data_2d_copy}")
print(f"Data deepcopy = {data_2d_deepcopy}") # maka data list yang sudah kita salin menggunakan deepcopy tidak akan ikut berubah karena index di dalam listnya sudah memiliki address yang berbeda