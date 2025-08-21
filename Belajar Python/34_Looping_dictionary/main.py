# looping dictionary

teman_teman = {
    'cup':'ucup surucup',
    'tong':'otong surotong',
    'dung':'dudung surudung',
    'sep':'asep si kasyep',
    'cuy':'ucuy surucuy'
}

# looping first try (yang keluar adalah keynya)
for teman in teman_teman:
    print(teman)

# operator untuk mengambil item / iterables
keys = teman_teman.keys()
print(keys)

# untuk mengambil key beserta nilainya
for keys in teman_teman.keys():
    print(teman_teman.get(keys))
    
values = teman_teman.values()
print(values)

for values in teman_teman.values():
    print(values)
    
items = teman_teman.items()
print(items)

for item in teman_teman.items():
    print(item)

# kalau menggunakan items, kita bisa mengambil key beserta valuenya secara bersamaan
for key, value in teman_teman.items():
    print(f'key = {key}, value = {value}')
    
data_dict = {
    'nama':'Rizky',
    'jabatan':'pegawai',
    'id':'0023981'
}

for a in data_dict:
    print(a)
    
key = data_dict.keys()
print(key)

for key in data_dict.keys():
    print(data_dict.get(key))
    
nilai = data_dict.values()
print(nilai)

for nilai in data_dict.values():
    print(nilai)

items = data_dict.items()
for item in data_dict.items():
    print(item)