# Materi tambahan mengenai List

buah = ["jeruk", "pisang", "semangka", "kelapa"] # di dalam list 'buah' ini berisi beberapa string

for item in buah: # kondisi untuk setiap item atau isi di dalam list buah, lakukan:
    print(item) # akan melakukan print pada setiap item atau isi list 'buah' tersebut

# Misalkan kita hanya ingin mengambil salah satu item dari list buah tersebut, maka kita bisa menggunakan perintah berikut:
print(buah[0]) # nama pemanggilannya disebut index

'''
dalam python, index dimulai dari angka 0,1,2 dan seterusnya, jadi keterangan urutan index dalam list 'buah' adalah sebagai berikut
index ke-1 = jeruk
index ke-2 = pisang
index ke-3 = semangka
index ke-4 = kelapa
'''

# kita bisa melakukan print untuk setiap index menggunakan for loop seperti berikut: 
for index, item in enumerate(buah): 
    print(f"index ke-{index} : {item}")

