# operasi list

data_angka = [1,4,5,1,3,1,4,5,1,6,7,8,1,9,5,4,5,5,3,2,1,7,9,0]
print(f"data angka = \n {data_angka}")

# count data atau menghitung data tertentu
jumlah_data_1 = data_angka.count(1) # menghitung jumlah angka 1 yang ada di dalam list data_angka
jumlah_data_5 = data_angka.count(5) # menghitung jumlah angka 5 yang ada di dalam list data_angka

print(f"jumlah angka 1 = {jumlah_data_1}")
print(f"jumlah angka 5 = {jumlah_data_5}")

# ambil posisi data (index)
data = ["Ucup", "Putri", "Fajar", "Ujang"]
print(f"data = \, {data}")

index_putri = data.index("Putri") # mengambil data index dari nilai 'Putri' yang ada di dalam list 'data'
index_ujang = data.index("Ujang") # mengambil data index dari nilai 'Ujang, yang ada di dalam list 'data'
print(f'index si putri = {index_putri}')
print(f'index si putri = {index_ujang}')

# mengurutkan list
# jika nilai di dalam list adalah integer
print(f'data angka sebelum disort = \n{data_angka}')
data_angka.sort()
print(f'data angka sesudah disort = \n{data_angka}')

# jika nilai di dalam list adalah string, maka pengurutannya akan sesuai abjad
print(f'data sebelum disort = {data}')
data.sort()
print(f'data sesudah disort = {data}')

# membalik list (bukan mengembalikan ke semula)
data_angka.reverse()
data.reverse()

print(f'data di reverse = \n{data_angka}')
print(f'data di reverse = \n{data}')

