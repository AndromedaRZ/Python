'''Global dan Local scope variabel'''

nama_global = 'otong' # <- ini disebut sebagai variabel global
# di mana kita bisa mengaksesnya bahkan ketika di dalam fungsi

# akses variabel global dalam fungsi
def fungsi():
    print(f"fungsi menampilkan {nama_global}")

fungsi()

# akses variabel global dalam loop
for i in range(0,5):
    print(f"loop ke-{i} = {nama_global}")

# percabangan
if True:
    print(f"if menampilkan {nama_global}")

# jadi kita bisa mengakses variabel global di manapun seperti looping, fungsi, maupun percabangan (if else)

## Variabel Local Scope

def fungsi2():
    nama_local = "Ucup" # iini adalah Variabel local scope

fungsi2()
# print(nama_local) baris ini akan menjadi error

## contoh 1: penggunaan akses variabel
def say_otong():
    print(f"Hello {nama}")

nama = "Otong" # urutan variabel ini harus ada di atas pemanggilan fungsi agar fungsi say_otong bisa berjalan
say_otong() # jika ini ada di atas variabel, maka kodenya akan menjadi error

## contoh 2: mengubah variabel global
angka = 0
name = "Ucup"

def ubah(nilai_baru, nama_baru):
    global angka # fungsi ini mendapat akses mengubah angka
    global name
    angka = nilai_baru
    name = nama_baru 

# jika kita tidak menambahkan 'global' di dalam fungsinya
# variabel tersebut akan dianggap sebagai local variabel
# dan tidak bisa diakses di luar fungsi tersebut

print(f"Sebelum {angka, name}")
ubah(10, "Otong")
print(f"Sesudah {angka, name}")

## contoh 3:
angka = 0

for i in range(0, 5):
    angka += i
    angka_dummy = 0

print(angka)
print(angka_dummy)

if True:
    angka = 10
    angka_dummy = 10

print(angka)
print(angka_dummy)

'''
Local variabel hanya berdampak pada fungsi (def).
Jadi, misalnya seperti for loop, maupun percabangan tidak perlu mengetik 'global'
Karena variabel yang ada di dalam looping dan percabangan bisa kita akses bahkan ketika di luar looping maupun percabangan tersebut.
Beda halnya dengan fungsi yang perlu mengetik 'global' agar variabelnya bisa diakses di luar fungsi tersebut

'''