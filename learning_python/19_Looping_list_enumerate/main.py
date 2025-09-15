# looping dari list

# for loop
print("\nMenggunakan for loop")
kumpulan_angka = [4,3,2,5,1,9]

for i in kumpulan_angka:  # untuk setiap index (dilambangkan dengan i) atau isinya di dalam variabel data list kumpulan_angka
    print(f"Angka = {i}")  # maka print dari index ke-0 sampai index terakhir (tergantung banyaknya data di dalam list)

nama = ["Zidane","Luna","Ryan","Joko"]

for nama in nama:  # kita juga bisa melakukan hal yang serupa pada data list string
    print(f"Nama: {nama}")  # outputnya adalah isi dari data list stringnya yang dimulai dari index ke-0 sampai index ke terakhir

# for loop dan range
print(f"\nmenggunakan for loop dan range")
kumpulan_angka = [3,6,2,9,7,1]

panjang = len(kumpulan_angka) # isi atau data dari variabel panjang adalah jumlah banyaknya data yang ada di list kumpulan_angka karena kita menggunakan fungsi len()

for i in range(panjang):  # untuk setiap index di dalam range banyaknya jumlah data pada list kumpulan_angka
    print(f"Angka = {kumpulan_angka[i]}")  # outputnya adalah nilai dari index ke-0 sampai index ke terakhir secara berurutan yang ada di dalam data list kumpulan_angka

# while
print(f"\nMenggunakan while loop")
kumpulan_angka = [3,6,2,9,7,1]

panjang = len(kumpulan_angka)
i = 0 # karena while loop bisa mengakibatkan infinity loop, maka kita tambahkan satu dummy variabel yang memiliki jumlah awal agar kita bisa mengaturnya

while i < panjang: # maka perulangan akan berhenti ketika nilai dari dummy variabel melebihi panjang(banyaknya data di dalam list)
    print(f"Angka = {kumpulan_angka[i]}") # outputnya akan sama seperti pada for loop dan range
    i += 1 # setiap perulangan akan menambah nilai dummmy variabel sebanyak 1

# list comprehension
print(f"\nList comprehension")
data = ["Ryan",8,10,4,"Joko"]

[print(f"Data = {i}") for i in data] # print (...) untuk setiap i di dalam variabel data
# fungsinya hampir sama seperti for pada biasanya hanya saja perintahnya dibuat lebih singkat

angka = [4,3,2,5,1,9]
angka_kuadrat = [i**2 for i in angka] # fungsi ini bisa kita gunakan untuk membuat perpangkatan di dalam list
print(angka_kuadrat) # sehingga kita tidak perlu membuat list yang baru


# enumerate
print(f"\nEnumerate")
data_list = ["Ryan",8,10,4,"Joko"]

for index,data in enumerate(data_list): # kita tambahkan index dan menggunakan enumerate() dan masukkan data list yang kika ingingkan
    print(f"index ke-{index}, data = {data}") # outputnya akan menunjukkan index ke berapa dan isinya apa saja yang ada di dalam data listnya
    # enumerate ini bisa mempermudah kita karena tidak perlu menggunakan for loop ataupun while loop