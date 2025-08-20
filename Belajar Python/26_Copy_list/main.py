# Copy list
## Teknik menduplikat list

a = ["Ucup", "Otong", "Dudung"]
print(f'a = {a}')

b = a # pass preference / hanya membuat referensi, tidak membuat data baru
print(f'b = {b}')

# kita akan merubah salah satu nama di dalam list a

# ini akan merubah kedua list. Jadi, jika salah satu nilai di dalam list a berubah maka nilai dalam list b juga ikut berubah, begitupun sebaliknya

a[1] = "Michael" # artinya kita akan mengubah nama dari index ke-1 yang ada di dalam list a menjadi "Michael", maka yang hilang adalah nama "Otong" dan nilai dalam list b juga akan berubah sama persis dengan nilai list a
b.sort()

print(f'a = {a}')
print(f'b = {b}')

# address dari kedua list a dan b
print(f'address a = {hex(id(a))}')
print(f'address b = {hex(id(b))}')
# kedua address dari list di atas akan sama karena list b tidak benar-benar membuat list baru, melainkan hanya membuat listnya menjadi dua

# menduplikat list dengan copy

print(f'mmembuat list c  dengan a.copy()')
c = a.copy() # full duplicate / data baru
# kode .copy() di atas akan membuat copy atau duplikat dari list a dengan address yang berbeda 

print(f'address a = {hex(id(a))}')
print(f'address b = {hex(id(b))}')
print(f'address c = {hex(id(c))}')

print(f'a = {a}')
print(f'b = {b}')
print(f'c = {c}')

# Jika kita merubah nilai dalam list c, maka nilai dalam list a dan b tidak akan berubah karena list c berbeda address dengan a dan b
print('\nMerubah nilai index ke-0 dari c')
c[0] = "Dadang"

print(f'a = {a}')
print(f'b = {b}')
print(f'c = {c}')
