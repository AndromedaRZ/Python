## Tutorial membaca file eksternal

print(4*'=', 'Membaca file txt', '='*4)
file = open('data.txt', mode='r') # mencoba membuka file eksternal dan memakai mode read ( mode='r' ) atau membaca file tersebut

# memeriksa apakah file tersebut bisa dibaca atau tidak
print(f'status read : {file.readable()}')

# memeriksa apakah file tersebut bisa ditulis (diedit) atau tidak
print(f'status read : {file.writable()}')

# baca isi seluruh file
print(file.read()) 

# baca per baris
# print(file.readline(), end='') # akan membaca teks pada baris pertama dari file tersebut
# print(file.readline(), end='') # akan membaca teks pada baris kedua dari file tersebut

## baca semua baris sebagai list
# print(file.readlines())

print(f'apakah file sudah diclose = {file.closed}')

# menutup file
file.close()

print(f'apakah file sudah diclose = {file.closed}')

# salah satu teknik membuka file di python
print('\n',4*'=', 'Membaca file txt dengan with', '='*4)

with open('data.txt', mode='r')  as file:
    content = file.readline()
    print(content, end='')
    print(f'apakah file sudah diclose = {file.closed}') # file belum diclose karena masih di dalam with
    
print(f'apakah file sudah diclose = {file.closed}') # file sudah diclose karena hanya diopen saat di dalam with