# Operator Dictionary

data_dict = {
    "cup":"ucup surucup",
    "tong":"otong surotong",
    "dung":"dung surudung",
}

print(data_dict)

# panjang dictionary
LENDICT = len(data_dict)
print(f'panjang dictionary: {LENDICT}')

# mengecek key nya ada atau tidak
KEY = "cup"
CHECKKEY = KEY in data_dict
print(f'apakah {KEY} ada di data_dict: {CHECKKEY}') # Jika key yang kita ingin periksa ada di dalam data_dict, maka hasilnya adalah True, jika sebaliknya maka hasilnya adalah False

# mengakses value (read) atau nilai di dalam dictionary menggunakan get
print(data_dict["cup"])
print(data_dict.get("cup")) # untuk memastikan bahwa data yang ingin diakses adalah dictionary dan bukan data yang lain
print(data_dict.get("kis")) # saat menggunakan get, jika kita mengakses data yang tidak ada di dalam dictionary tersebut, maka tidak akan error, melainkan hanya menampilkan pesan 'none' saja.
print(data_dict.get("kis", "key tidak ditemukan")) # atau kita juga bisa menambahkan pesan tambahan jika key yang ingin diakses tidak tersedia

# mengupdate data
# mengubah nilai dari data yang sudah ada
data_dict["cup"] = "ucup si ganteng"
print(data_dict)

# menambahkan data baru yang belum ada
data_dict["sep"] = "asep si kasyep"
print(data_dict)

# mengubah nilai dari data yang sebelumnya ada
data_dict.update({"cup": "ucup surucup"})
print(data_dict)

data_dict.update({"rizky": "rizky si programmer handal"}) # jika memakai fungsi .update untuk data yang belum ada, maka akan otomatis menambahkan data yang baru ini ke dalam data yang sudah ada
print(data_dict)

# delete data pada dictionary
del data_dict["rizky"] # Jika ingin menghapus data yang ada di dalam dictionary, maka kita bisa gunakan kode del dan pada kurung perseginya kita masukan key dari data yang ingin kita hapus
print(data_dict)