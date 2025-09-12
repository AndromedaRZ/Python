# Global dan local scope

nama_global = "Ucup" # <- variabel global, bisa digunakan secara global yakni bebas dipakai

# akses variabel global dalam fungsi
def fungsi():
    print(f"menampilkan nama {nama_global}")
    
fungsi()

# akses variabel global dalam for loop
print("\nFor loop")
for i in range(0, 5):
    print(f"loop {i} - {nama_global}")

# percabangan
print("\nPercabangan")
if True:
    print(f"if menampilkan {nama_global}")
    
## variabel local scope

def fungsi():
    nama_local = "Alisa" # <- variabel local scope, hanya berada di dalam fungsi dan tidak dapat dipanggil di luar fungsi

fungsi()
'''    
print(nama_local) <- jika dijalankan akan mengalami error karena variabel tersebut adalah variabel local scope
'''

## studi kasus penggunaan variabel local scope

# contoh kasus 1: penggunaan akses variabel
print("\nVariabel local scope")
def say_hi():
    print(f"Hi, {nama}")

nama = "Ray" # <- variabel nama harus didefinisikan terlebih dahulu nilainya, setelah itu baru fungsi di bawahnya dapat berjalan
say_hi()

# contoh kasus 2: merubah variabel global
print("\nMerubah variabel global")
angka = 0
nama = "Ucup"

def ubah(angka_baru, nama_baru):
    global angka # fungsi ini akan memberi akses global kepada variabel angka yang sebelumnya masih local
    global nama
    angka = angka_baru
    nama = nama_baru
    
print(f"sebelum berubah = {angka, nama}")
ubah(10, "Doni")
print(f"sebelum berubah = {angka, nama}")

# contoh 3
# setiap variabel local dalam for ataupun if bisa diakses dan diubah dari dalam maupun luar if atau for tersebut

angka = 0

for i in range(0, 5):
    angka += i
    angka_dummy = 0
    
print(angka)
print(angka_dummy)

if True:
    angka = 9
    angka_dummy = 10
    
print(angka)
print(angka_dummy)
    