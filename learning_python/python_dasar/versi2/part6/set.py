'''set (himpunan)'''
# set adalah kumpulan data yang tidak berurutan dan tidak memiliki elemen duplikat
# set ditulis menggunakan kurawal {} atau fungsi set()
# untuk menambah data ke set, kita bisa menggunakan method 'add()'
# untuk menghapus data di set, kita bisa menggunakan mehtod 'remove(value)'
# set tidak memiliki index
# untuk mengakses data di dalam set, biasanya kita menggunakan perulangan for

buah = {'Apel', 'Jeruk', 'Pisang'}

# menambah elemen
buah.add('Mangga')
buah.add('Mangga')
print(buah)
# walaupun kita sudah mencoba menambah data 'Mangga' sebanyak dua kali, hasilnya hanya 1 saja yang akan masuk
# hal ini disebabkan karena set tidak memiliki elemen duplikat (tidak bisa menyimpan data yang sama lebih dari sekali)

# menghapus elemen
buah.remove('Jeruk')
print(buah)

# iterasi menggunakan for loop 
for a in buah:
    print(a)