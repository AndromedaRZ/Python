# Looping dictionary

teman_teman = {
    "cup":"ucup surucup",
    "tong":"otong surotong",
    "dung":"dudung surudung",
    "sep":"asep si kasyep",
    "cuy":"ucuy surucuy"
}

# first try looping

for i in teman_teman:
    print(i) # outputnya hanya key-nya saja yang terprint
    
# operator untuk mengambil item / iterables

keys = teman_teman.keys() # kode ini akan mengambil dan mengumpulkan key dari setiap value yang ada di dalam dictionarynya
print(keys)

for key in teman_teman.keys():
    print(teman_teman.get(key)) # method .get() ini akan menampilkan value atau isi dari setiap key yang sudah dikumpulkan tadi
    
values = teman_teman.values() # kode ini akan mengambil dan mengumpulkan value dari setiap key yang ada di dalam dictionarynya
print(values)

for value in teman_teman.values():
    print(value) # kita tinggal menggunakan perintah for loop untuk memunculkan setiap valuenya
    
items = teman_teman.items()
print(items)

for item in teman_teman.items(): # dengan menambahkan method .items()
    print(item) # hasilnya akan berupa tuples
    # maka data yang diprint adalah setiap item atau data bersama key dan valuenya yang berada di dalam dictionary tersebut
    
for key,value in teman_teman.items():
    print(f"Key = {key}, Value = {value}") # cara untuk mengambil item dengan key dan valuenya secara terpisah