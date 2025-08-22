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
    
data_diri = {
    'nama':'Rizky',
    'jabatan':'pegawai',
    'alamat':'Jalan alam sutera',
    'status':'belum kawin'
}

# print hanya keynya saja
for item in data_diri:
    print(item)
    
# print hanya value atau nilainya saja
for item in data_diri:
    print(data_diri[item])
    
# print key dan valuenya
for item in data_diri:
    print(item,":",data_diri[item])
    
for key, item in data_diri.items():
    print(key,":",item)
    
for item in data_diri.items():
    print(item)