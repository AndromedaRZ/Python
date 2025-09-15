# operator dictionary

data_dict = {
    'cup':'ucup surucup',
    'tong':'otong surotong',
    'dung':'dudung surudung'
}

# panjang dictionary
LENDICT = len(data_dict) # LENDICT dibuat uppercase karena itu adalah constant

print(f"Panjang dictionary: {LENDICT}")

# mengecek suatu 'key' apakah ada (exist) atau tidak

KEY = 'cup' # pertama-tama masukkan key ke dalam constant
CHECKKEY = KEY in data_dict # lalu buat fungsi untuk mengecek apakah key tersebut ada di dalam dictionary data_dict?
print(f"Apakah {KEY} ada di data_dict: {CHECKKEY}") # bisa kita lihat dengan menjalankan perintah ini, hasilnya akan menunjukkan True atau False

# mengakses value (read) dengan get
print(data_dict['cup'])
print(data_dict.get('cup')) # hasilnya akan sama seperti baris di atas karena data tersebut ada di dalam data_dict, bagaimana jika datanya tidak ada?
# contohnya di bawah ini
print(data_dict.get('kis')) # hasilnya akan menjadi 'none' ketika data yang kita cari tidak ada di dalam dictionary, jika kita menuliskan data yang tidak ada tanpa menggunakan fungsi .get() maka programnya akan langsung error
# fungsi lain dari .get() ini kita bisa menambahkan kata untuk ditampilkan ketika data yang diinginkan tidak ada di dalam dictionary
print(data_dict.get('kis','key tidak ditemukan')) # mengecek key dengan message tidak ditemukan


# mengupdate data (mengubahh data)
data_dict['cup'] = "ucup si ganteng"
print(data_dict)

data_dict['sep'] = "asep si kecee" # bisa dianggap menambahkan data
# dengan cara memasukkan 'key' yang baru menggunakan kurung siku, tambahkan sama dengan dan masukkan values yang kita inginkan untuk key tersebut
print(data_dict)

data_dict.update({'cup':'ucup surucup'}) # ketika kita menggunakan fungsi .update(), jika data sebelumnya telah ada, maka ia akan merubah atau mengupdate datanya sesuai perubahan terbaru
print(data_dict)
data_dict.update({'faqih':'faqihza si keren'}) # tetapi ketika sebelumnya datanya tidak ada di dalam dictionarynya, maka otomatis data yang kita tulis akan masuk ke dalam dictionary tersebut
print(data_dict)

# menghapus data pada dictionary
del data_dict['faqih'] # kita hanya perlu mengetik del lalu masukkan nama dictionary dan gunakan kurung siku untuk memasukkan key yang ingin dihapus
print(data_dict) # maka hasilnya key tersebut akan hilang

# menyatukan dua list menjadi satu dictionary
keys = ['Russia','USA','China'] 
# sebelumnya kita buat 2 list terlebih dahulu
values = ['Moscow','Washington D.C.','Beijing']

print(keys)
print(values)

data = dict(zip(keys, values)) # gunakan zip() di dalam dict() untuk membungkus kedua list tersebut agar menjadi satu seperti data dictionary yang kita inginkan

print(data)