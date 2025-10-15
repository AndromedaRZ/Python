'''
9) GLOBAL DAN LOCAL SCOPE

Apa itu scope?, singkatnya scope adalah lingkup atau ruang di mana sebuah variabel bisa digunakan, seperti wilayah kerja suatu variabel

Ada 2 scope utama dalam python:
Global Scope --> Variabel yang bisa diakses di mana saja dalam program
Local scope --> Variabel yang hanya bisa diakses dari fungsi tertentu
'''

# 1) Global scope, variabel yang bisa dipakai di luar fungsi, bisa dipakai dimana saja baik di dalam maupun di luar fungsi
# contoh global scope
print(f"Global Scope")
nama_global = "Rizky" # variabel global, bisa kita akses dari dalam fungsi 

def display_nama():
    '''menampilkan nilai dari variabel global'''
    print(f"menampilkan nilai variabel global dari fungsi = {nama_global}") # <-- mengakses variabel global dari dalam fungsi
    
display_nama()
print(f"menampilkan nilai variabel global dari luar fungsi = {nama_global}") # <-- mengakses variabel global dari luar fungsi

# akses variabel global menggunakan for loop

print('\nfor loop')
for i in range(0, 5):
    print(f'loop ke-{i} = {nama_global}')
    
# percabangan

print("\npercabangan")
if True:
    print(f"percabangan = {nama_global}")
    
'''
Seperti yang dapat kita lihat di atas, variabel global dapat kita akses dari mana saja
'''

# 2) Local scope, variabel yang dibuat di dalam fungsi dan hanya bisa diakses dari dalam fungsi tersebut
# contoh local scope
print(f"\nLocal Scope")

def display_name():
    '''fungsi menampilkan nilai dari variabel yang ada di dalam fungsi ini'''
    nama_local = "Aisa" # variabel local, hanya bisa diakses dari dalam fungsi ini
    print(f'menampilkan nilai variabel local dari dalam fungsi = {nama_local}') # <-- mengakses variabel local dari dalam fungsi
    
display_name()
# print(f'menampilkan nilai variabel local dari dalam fungsi = {nama_local}') # <-- jika kita berusaha mengakses variabel local dari luar fungsi maka programnya akan mengalami error

'''
Studi kasus penggunaan global dan local scope
'''

# contoh kasus 1
print(f'\ncontoh soal 1')
def say_hi():
    print(f"Halo, {nama}") # dalam fungsi ini, kita mengakses sebuah variabel yang ada di luar fungsi dari dalam fungsi
    
nama = "Rizwan" # variabel 'nama' ini baru didefinisikan setelah fungsi di atas memanggilnya, jika tidak kita denisikan maka fungsi di atas akan mengalami error ketika kodenya dijalankan
say_hi()

# contoh soal 2
# merubah variabel local menjadi global
print(f'\ncontoh soal 2')
def fungsi():
    global nama # <-- kita bisa merubah variabel local menjadi global, fungsi "global" akan memberi akses global kepada variabel angka yang sebelumnya masih local
    nama = "Rizky" # variabel local yang dibuah menjadi global
    print(f"variabel local di dalam fungsi = {nama}")
    
fungsi()
print(f"variabel local dari luar fungsi = {nama}") # kita bisa mengakses variabel local yang tadi sudah diubah menjadi global dari luar fungsi

# pertama-tama, kita buat terlebih dahulu nilai awal dari dua variabel di bawah ini
angka = 0
nama = "Ucup"


def fungsi(angka_baru, nama_baru):
    global angka # memberi akses global ke variabel local (angka) di dalam fungsi ini
    global nama # memberi akses global ke variabel local (nama) di dalam fungsi ini
    angka = angka_baru # kita ubah nilai dari variabel angka dari fungsi ini
    nama = nama_baru # kita ubah nilai dari variabel nama dari fungsi ini
    
print(f"angka sebelum diakses dari fungsi = {angka}")
print(f"nama sebelum diakses dari fungsi = {nama}")
fungsi(10, "Jajang")
print(f"angka sesudah diubah dari fungsi = {angka}")
print(f"nama sesudah diubah dari fungsi = {nama}")

# contoh soal 3
# setiap variabel local dalam for atau if bisa diakses dan diubah dari dalam maupun luar for atau if tersebut

print("\ncontoh soal 3")
angka = 0 # variabel global

for i in range(0, 5):
    angka += 1 # dapat kita akses dari dalam loop
    angka_dummy = 0 # variabel local atau variabel yang ada di dalam loop
    
print(angka)
print(angka_dummy) # variabel local dapat kita akses dari luar loop
    
if True:
    angka = 9
    angka_dummy = 10

print(angka)
print(angka_dummy)
