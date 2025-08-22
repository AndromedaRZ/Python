# Copy dictionary

teman_teman = {
    "cup":"ucup surucup",
    "tong":"otong surotong",
    "dung":"dudung surudung",
    "sep":"asep si kasyep",
    "cuy":"ucuy surucuy"
}

friends = teman_teman # jika kita melakukan copy dengan cara seperti

print(f"teman_teman:\n{teman_teman}\n")
print(f"friends:\n{friends}\n")

teman_teman["cup"] = "ucup si keren" # maka ketika kita mengubah komponen yang ada di dalam dictionary teman-teman
# dictionary friends pun akan ikut berubah

print(f"teman_teman:\n{teman_teman}\n")
print(f"friends:\n{friends}\n")

# cara untuk agar dictionary yang lain tidak ikut berubah adalah dengan menambahkan method .copy() ketika menyalinnya seperti perintah di bawah ini
friends = teman_teman.copy() # tambahkan .copy()
# bahkan ketika kita mengubah komponen yang ada di dalam dictionary friends
# maka dictionary teman_teman tidak akan ikut berubah ketika kita menambahkan method .copy()

teman_teman["cup"] = "ucup si kece abis"

print(f"teman_teman:\n{teman_teman}\n")
print(f"friends:\n{friends}\n")

# pop dictionary (mengambil data berdasarkan key)
dataAsep = friends.pop('sep') # key 'sep' akan kita ambil menggunakan .pop() dan dimasukkan ke dalam variabel
print(f"data asep = {dataAsep}, bertipe data {type(dataAsep)}\n") # kita bisa memanggil variabelnya dan akan muncul isi dari key yang tadi kita ambil
print(f"friends = {friends}\n") # maka dictionary friends akan kehilangan salah satu key dan valuenya yaitu 'sep':'asep si kasyep' karena sudah kita ambil menggunakan .pop()

# popitem dictionary (mengambil data terakhir)
dataTerakhir = friends.popitem() # hampir mirip dengan pop
# hanya saja kita menggunakan popitem dan mengosongkan isi dari methodnya untuk mengambil data paling terakhir
# (kita juga bisa mengosongkan kurung pada method .pop() jika ingin mengambil data paling terakhir)
print(f"data terakhir = {dataTerakhir}, bertipe data {type(dataTerakhir)}\n") # sama halnya pop juga, kita bisa melihat data yang diambil
print(f"friends = {friends}\n") # dan nantinya dictionary tersebut akan kehilangan satu data yang sudah diambil

# kalo begitu apa perbedaan pop dan popitem?
# hasil pengambilan data dari pop akan bertipe string
# sedang popitem akan menghasilkan data bertipe tuples
# bisa dilihat ada yang berbeda diantara pernggunaan pop dan popitem
# ketika kita memunculkan data yang diambil menggunakan print()