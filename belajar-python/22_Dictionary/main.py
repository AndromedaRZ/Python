# list -> array, di mana kita mengakses datanya dengan menggunakan index

data_list = ['Ucup','Otong','Dudung']
print(data_list[1])

# Dictionary (dict) -> associative array, berbeda dengan list atau array
# dict ini kita mengakses datanya dengan menggunakan identifier -> key

data_dict = {
    'key1':'value1',
    'key2':'value2'
}

print(data_dict) # lalu apa perbedaannya dengan list array?

# dictionary dibuat menggunakan kurung kurawal untuk membuat listnya
# singkatnya, dictionary ini bisa berfungsi untuk pengkategorian data di dalam sebuah list
# seperti contoh di atas, kita membuat sebuah 'key' dan sebuah 'value' yang dipisahkan dengan titik dua (:)

data_dict2 = {
    'cp':'Ucup', # 'cp' sebagai 'key1', dan 'Ucup' sebagai value1
    'tg':'Otong', # 'tg' sebagai 'key2', dan 'Otong' sebagai value2
    'dg':'Dudung' # 'dg' sebagai 'key3', dan 'Dudung' sebagai value3
}

print(data_dict2)
# jika pada list array kita menggunakan index untuk memanggil data yang kita inginkan di dalamnya
# maka untuk dictionary ini kita tinggal menggunakan key untuk memanggil data atau value yang kita inginkan

print(data_dict2['cp']) # gunakan key1 yaitu 'cp' untuk memanggil valuenya yaitu 'Ucup'
print(data_dict2['tg']) # kita juga bisa menggunakan key yang lain untuk memanggil value yang berbeda juga
print(data_dict2['dg'])

# selain string yang tadi, kita juga bisa memasukkan angka ataupun data list ke dalam valuenya

data_dict3 = {
    'nmbr':100,
    'list':data_list
}

print(data_dict3)
print(data_dict3['nmbr']) # kita tinggal memasukkan key yang sesuai dengan value yang kita inginkan
print(data_dict3['list'])