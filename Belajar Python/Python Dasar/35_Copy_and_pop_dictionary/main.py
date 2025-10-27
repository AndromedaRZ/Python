# copy dictionary

teman_teman = {
    "riz":"rizky",
    "rif":"rifki",
    "ric":"ricky",
}

# akan menduplikat dictionary 'teman_teman' ke dictionary baru bernama 'friends'
friends = teman_teman.copy()

print("teman_teman =",teman_teman)
print("friends =",friends)

teman_teman["riz"]="rizky si keren"
print("\nteman_teman =",teman_teman)
print("friends =",friends)

# pop dictionary (berdasarkan key yang kita tentukan)
dataRic = friends.pop("ric") # kode .pop berfungsi untuk mengambil nilai atau data dari list yang kita tentukan, nilai atau data yang sudah kita ambil dari list tersebut akan kehilangan datanya sehingga saat kita print kembali list 'friends', maka nilai atau data yang sudah kita ambil dari list tersebut sudah tidak ada  
print(f'\ndataRic = {dataRic}') 
print(f'data friends = {friends}')

# pop item dictionary (hanya data terakhir saja)
dataTerakhir = friends.popitem() # kode .popitem hampir sama dengan .pop, tetapi hanya digunakan untuk mengambil data yang terakhir saja
print(f'\ndataTerakhir = {dataTerakhir}') 
print(f'data friends = {friends}')

