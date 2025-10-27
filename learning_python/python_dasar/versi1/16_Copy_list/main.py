## Teknik duplikasi list

a = ["Zidane","Ryan","Herman"]
print(f"a = {a}")

b = a # kita mendefinisikan variabel b sama seperti a
# atau bisa dikatakan 'pass by reference'
print(f"b = {b}")

# percobaan
a[1] = "Michael"
b.sort()
print(f"a = {a}")
print(f"b = {b}")
# ketika kita mengubah salah satu list, maka list yang lain akan ikut berubah

# address dari list a dan b
print(f"Address a = {hex(id(a))}")
print(f"Address b = {hex(id(b))}") # kita bisa lihat di sini bahwa list a dan b memiliki address yang sama
# pada kasus ini kita menduplikasi list namun masih memiliki struktur data yang sama
# agar struktur datanya berbeda, kita bisa gunakan cara di bawah ini:

print("\nMenduplikasi data list menggunakan '.copy()'")
c = a.copy() # kita tambahkan fungsi .copy() setelah variabel list yang ingin kita salin dan masukkan ke dalam variabel yang baru
# full duplikat/data baru

print(f"Address a = {hex(id(a))}")
print(f"Address b = {hex(id(b))}")
print(f"Address c = {hex(id(c))}") # maka hasilnya variabel c ini akan memiliki struktur data yang berbeda namun masih memiliki nilai yang sama, sehingga ketika kita memanipulasi list c ini tidak akan berpengaruh ke list yang lain

# contoh perubahan
a[2] = "Vera" # kita mengubah data list a, maka nantinya list b juga akan ikut berubah, tetapi list c tidak akan berubah
print("\nContoh perubahan list a dan b")
print(f"a = {a}")
print(f"b = {b}")
print(f"c = {c}")

c[1] = "Tono" # ketika kita mengubah data list c, maka data list a dan b tidak akan ikut berubah
print("\nContoh perubahan list c")
print(f"a = {a}")
print(f"b = {b}")
print(f"c = {c}")