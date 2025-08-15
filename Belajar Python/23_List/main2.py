# operasi

# index  0,(-3)  1,(-2)    2,(-1)
data = ["Ucup", "Otong", "Dudung"]

# mengambil data dari list ini menggunakan variabel lain
data_0 = data[0]
print(f"data pertama (index ke-0) = {data_0}")

data_terakhir = data[-1] # jika kita tidak tahu berapa index terakhir yang ada di dalam variabel 'data', maka kita bisa menggunakan index -1
print(f"data terakhir (index ke-2) = {data_terakhir}")

data_ucup = data[-3] # akan mengambil nilai index pertama di dalam variabel 'data'

# mengambil info jumlah data dalam list
panjang_data = len(data) # akan mendeteksi berapa jumlah data atau nilai yang ada di dalam variabel 'data'
print(f"panjang data = {panjang_data}")

## Manipulasi data list

# menambahkan item di dalam list sesuai posisi
print(f"data sebelum ditambah = \n{data}")

data.insert(1, "Asep") # format (posisi index, data yang ingin ditambahkan)
print(f"data sesudah ditambah = \n{data}")

# menambah item di akhir list
data.append("jamal")
print(f"data sesudah ditambah lagi = \n{data}")

# menambah list dengan list
data_baru = ["Ujang", "Yusuf", "Dadang"]
data.extend(data_baru) # menambah nilai atau item yang ada di dalam variabel 'data' dengan nilai yang ada di dalam 'data_baru'

## merubah data
# mengubah nilai index ke-2 menjadi 'michael'
data[2] = "michael"
print(f"data yang berubah = \n{data}")

## remove data
# menghapus data
data.remove("Ujang") # formaat (masukkan data atau nilai yang ingin dihapus dari suatu variabel)
print(f"data yang sudah dihapus = \n{data}")
# jika data yang ingin dihapus tidak ada, maka hasilnya akan error

# menghapus data paling belakang
data_akhir = data.pop()
print(f"data yang dihapus = {data_akhir}")
print (f'data akhir = \n{data}')

