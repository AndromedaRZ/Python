# for loop (perulangan)

# digunakan untuk mengulang sebuah perintah ataupun kondisi ketika kondisinya sudah terpenuhi ataupun belum terpenuhi seusai yang kita atur

angka = 1
print(angka)
angka = angka + 1
print(angka)
angka = angka + 1
print(angka)

# di atas adalah baris contoh perulangan
# # tapi bagaimana jika kita ingin membuat kode yang sama sangat banyak? tidak mungkin kan harus membuat kodenya sebanyak 100 baris.
# maka dari itu kita bisa menggunakan fungsi for loop (perulangan) ini

# for kondisi:
#   aksi

# contoh perulangan dengan list
angka_list = [0,1,2,3,4]
print(angka_list)

for i in angka_list: # maksudnya seperti ini -> untuk i yang ada di dalam variabel angka2
    print(f"i sekarang -> {i}") # untuk looping pertama adalah 0 dan teus mengulang sebanyak index dan data yang ada di dalam variabel angka2
print("Program 1 berakhir\n")

# contoh perulangann dengan range
angka_range = range(5)

for i in angka_range:
    print(f"i sekarang -> {i}") # hasilnya akan menampilan index ke-0 sampe index ke-4 walaupun kita memasukkan rangenya sebanyak 5, yang berarti index ke-0 juga dihitung
print("Program 2 berakhir\n")


angka_range = range(1,10) # inputnya hampir sama seperti perulangan kode program ke-2, hanya saja kali ini kita memasukkan angka 1, 10.
# artinya kita akan membuat perulangan dari 1 sampai 9 dan index ke-0 juga dihitung yang berarti jika kita menggunakan for i maka ia hanya akan memberikan output sampai 9 saja dan bukan 10

for i in angka_range:
    print(f"i sekarang -> {i}")
    
print("Program 3 berakhir\n")

# contoh perulangan dengan menggunakan string

data_str = "Saya ganteng abis"

for huruf in data_str: # setiap i (data) atau huruf yang ada di dalam variabel data_str
    print(huruf) # maka kode akan mem-print setiap huruf tersebut
print("Program 4 berakhir")