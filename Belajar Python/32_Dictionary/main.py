# list adalah contoh dari array, dan diakses dengan menggunakan index

data_list = ["Ucup", "Otong", "Dudung"]
print(data_list[0])

# dictionary (dict) --> associative array
# dalam associative array, untuk mengakses datanya menggunakan identifier atau key

'''
format dictionary adalah
'key':'nilai atau isinya'
'''

data_dict = {
    'key':'value',
    'cp':'Ucup',
    'tg':'Otong',
    'pt':'Putri',
    'nmbr':100,
    'list':data_list
}

print(data_dict)

# jika kita ingin mengambil salah satu nilai saja dari dalam dictionary, maka kita bisa memanggilnya dengan menggunakan keynya:
print(data_dict['cp'])
print(data_dict['nmbr'])
print(data_dict['list'])