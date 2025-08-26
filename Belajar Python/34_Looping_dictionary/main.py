# looping dictionary

# teman_teman = {
#     'cup':'ucup surucup',
#     'tong':'otong surotong',
#     'dung':'dudung surudung',
#     'sep':'asep si kasyep',
#     'cuy':'ucuy surucuy'
# }

# # looping first try (yang keluar adalah keynya)
# print('\nfor teman in teman_teman: print(teman)')
# for teman in teman_teman:
#     print(teman)

# # operator untuk mengambil keynya
# print('\nkeys = teman_teman.keys(), print(keys)')
# keys = teman_teman.keys()
# print(keys)

# print("\nfor key in teman_teman.keys(): print(f'key = {key}')")
# for key in teman_teman.keys():
#     print(f'key = {key}')

# # untuk print value dari dictionary berdasarkan urutan keynya
# print("\nfor keys in teman_teman.keys(): print(teman_teman.get(keys))")
# for keys in teman_teman.keys():
#     print(teman_teman.get(keys))
    
# # untuk mengambil value dari dictionary
# print('\nvalues = teman_teman.values(), print(values)')
# values = teman_teman.values()
# print(values)

# # untuk mengambil value dari dictionary menggunaka for loop
# print('\nfor values in teman_teman.values(), print(values)')
# for values in teman_teman.values():
#     print(values)

# print('\nitems = teman_teman.items(), print(items)')
# items = teman_teman.items()
# print(items)

# print('\nfor item in teman_teman.items(): print(item)')
# for item in teman_teman.items():
#     print(item)

# # kalau menggunakan items, kita bisa mengambil key beserta valuenya secara bersamaan
# print('\nfor key, value in teman_teman.items(): print(key,value)')
# for key, value in teman_teman.items():
#     print(f'key = {key}, value = {value}')
    
data_diri = {
    'nama':'Rizky',
    'jabatan':'pegawai',
    'alamat':'Jalan alam sutera',
    'status':'belum kawin'
}

# print hanya keynya saja
print('\nfor item in data_diri: print(item)')
for item in data_diri:
    print(item)
    
# print hanya value atau nilainya saja
print('\nfor item in data_diri: print(data_diri[item])')
for item in data_diri:
    print(data_diri[item])
    
# print key dan valuenya
print('\nfor item in data_diri: print(item, data_diri[item])')
for item in data_diri:
    print(item,":",data_diri[item])
    
print('\nfor key, item in data_diri.items(): print(key, item)')
for key, item in data_diri.items():
    print(key,":",item)

print('\nfor item in data_diri.items(): print(item)')
for item in data_diri.items():
    print(item)

buah = {
    'apple':'merah',
    'jeruk':'orange',
    'anggur':'ungu',
    'pisang':'kuning'
}

    
## looping dan print semua key dalam dictionary buah
for item in buah:
    print(item)
    
# looping dan print semua value dalam dictionary buah
for item in buah:
    print(buah[item])
    
## operator untuk mengabil key dari dictionary buah
print('\n> menggunakan keys(): ')
key = buah.keys()
print(key)

# memakai for loop untuk mengambil key
for key in buah.keys():
    print(buah[key]) 

# mengambil setiap value atau nilai berdasarkan key di dalam dictionary buah
print("\n> menambah get()")
print('- for key in buah.keys(): print(buah.get(key))')
for key in buah.keys():
    print(buah.get(key))
    
## operator untuk mengabil value dari dictionary buah
print('\n> menggunakan values()')
value = buah.values()
print(value)

# memakai for loop untuk mengambil value
for value in buah.values():
    print(value)

## operator untuk mengambil key dan valuenya secara bersamaan
item = buah.items()
print(item)

# memakai for loop untuk mengambil key dan valuenya secara bersamaan
for item in buah.items():
    print(item)

# menempatkan secara spesifik key dan value di dalam loopnya
for key, value in buah.items():
    print(f'key: {key}, dan value: {value}')
    
