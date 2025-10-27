'''Tuple'''
# tuple dibuat menggunakan kurung biasa ()
# tuple hampir mirip dengan list
# perbedaanya kita tidak bisa melakukan operasi pada tuple (mengubah data, menghapus data, menambah data)
# untuk fungsi seperti melihat data, melihat panjang data, dan iterasi masih bisa kita lakukan

point = (5, 10)
print(point)

print(point[0])
print(point[1])

# untuk data yang tidak berubah
tanggal_lahir = (22, 9, 2006)
print(f"Tanggal lahir: {tanggal_lahir}")

# melakukan iterasi pada tuple
for e in tanggal_lahir:
    print(e)
    
# melakukan iterasi pada tuple menggunakan index
for i in range(len(tanggal_lahir)):
    print(tanggal_lahir[i])