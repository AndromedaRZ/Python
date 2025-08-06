## ---- LIST ----

# list adalah kumpulan data

# kumpulan data angka
data_angka = [1,3,6,3,7] # sebuah list atau kumpulan data biasanya dibuat dengan menggunakan kurung siku-siku ([...])
print(data_angka)

# kumpulan data string
data_string = ["Aaron","Zidane","Luna"]
print(data_string)

# kumpulan data boolean
data_boolean = [True,False,True,True]
print(data_boolean)

# kumpulan data campuran
data_campuran = [1,"andi",5,"bla-bla-bla","ucup",True]
print(data_campuran)

## cara alternatif membuat list
data_range = range(0,10) # nanti outputnya adalah range dari 0 sampai 9 atau sebelum 10 (bukan 10 karena angka 10nya tidak akan dianggap)
# rumus = range(start,stop,step)
data_range = range(0,10,2) # hampir sama seperti baris di atas hanya saja di sini ditambahkan 2 step atau melewati 2 nilai/angka
print(data_range) # pada baris ini data range belum berupa deretan angka dari 0 sampai 9

data_list = list(data_range) # tapi kita bisa mengubahnya menjadi sebuah data list dengan menggunakan list()
print(data_list)

# membuat list dengan for loop, list comprehension
list_pake_for = [i for i in range(0,10)] # i di mana i yang ada di dalam range(0,10)
print(list_pake_for)

# kita juga bisa membuat i nya menjadi berpangkat seperti contoh di bawah
list_pake_for = [i**2 for i in range(0,10)] # i pangkat 2 di mana i yang ada di dalam range(0,10)
print(list_pake_for)

# membuat list pake for pake if
list_pake_for_if = [i for i in range(0,10) if i != 5] # fungsi if di sini untuk menghilangkan angka 5
print(list_pake_for_if)

list_pake_for_if = [i for i in range(0,10) if i % 2 == 0] # di sini untuk membuat outputnya hanya bilangan genap (dengan cara menghitungnya menggunakan modulus dan jika di modulus 2 hasilnya 0 berarti itu bilangan genap)
print(list_pake_for_if)

list_pake_for_if = [i for i in range(0,10) if i % 2 != 0] # dan di sini untuk membuat outputnya hanya bilangan ganjil (dengan cara menghitungnya menggunakan modulus dan jika di modulus 2 hasilnya bukan 0 berarti itu bilangan ganjil)
print(list_pake_for_if)