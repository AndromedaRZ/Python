# looping list dan enumerate

# looping dari list
print('For loop')
kumpulan_angka = [4, 3, 2, 5, 6, 1]

for angka in kumpulan_angka: # akan melakukan pengulangan 'angka' dari isi list 'kumpulan angka' 
    print(f'angka = {angka}')
    
peserta = ["Ucup", "Adit", "Dimas", "Nabila"]

for nama in peserta:
    print(f'peserta = {nama}')   
print()
# for loop dan range

print("For loop and range")
kumpulan_angka = [10, 9, 8, 5, 3, 1, 0]

panjang = len(kumpulan_angka)

for i in range(panjang): # akan melaukan pengulangan dari range 'kumpulan angka'
    print(f'angka = {kumpulan_angka[i]}')
print()

# while
print('while loop')

kumpulan_angka = [1, 3, 4, 5, 7, 9, 10]
panjang = len(kumpulan_angka)
i = 0

while i < panjang: # kondisi selama 'i' lebih kecil dari panjang data 'kumpulan angka', maka program ini akan terus berjalan sampai angka dari 'kumpulan angka' sudah keluar semua
    print(f'angka = {kumpulan_angka[i]}')
    i += 1
    
# list comprehension
print('\nlist comprehension')
data = ["ucup", 1, 2, 4, 'dudung']

[print(f'data = {i}') for i in data] # akan melakukan print pada setiap item (i) di dalam list 'data'

angka = [10, 5, 2, 4, 8]

angka_kuadrat = [i**2 for i in angka] # akan mengkuadratkan atau mempangkatkan nilai angka-angka yang ada di dalam list 'angka'
print(angka_kuadrat)

# menggunakan enumerate
# dengan enumerate, kita bisa mengambil index dari list menggunakan for loop
print("\nEnumerate")
list_data = ["Ucup", "Otong", "Putri", "Nina", "Febri"]

for index, data in enumerate(list_data): # pada setiap pengulangan, for akan mengambil indexnya dan data dari list 'list_data' tersebut
    print(f'index ke-{index} = {data}')
    
    
# jika di dalam list terdapat list lagi

data_siswa = [{
    'nama':'rizky',
    'jurusan':'informatika',
    'hobi':'program game'
}]

for i in data_siswa:
    print(f'nama = {i['nama']}, jurusan = {i['jurusan']}, hobi = {i['hobi']}')