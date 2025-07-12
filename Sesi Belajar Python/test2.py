hobi = "membaca, bermain game, ngoding"
# kita tidak bisa mengambil hanya satu nilai dari variabel di atas, maka dari itu kita perlu mengubah data nya menjadi array seperti di bawah ini.
hobi2 = ["membaca", "bermain game", "ngoding"]
# jika data nya kita ubah menjadi array seperti di atas, maka kita bisa hanya mengambil satu data saja untuk ditampilkan atau diprint
print(hobi)
print(hobi2[0])
# dalam bahasa komputer atau lebih tepatnya penghitungan index dalam python, angka awal dimulai dari angka 0 sementara hitungan manusia dimulai dari angka 1
# jika masih belum terbiasa dengan index dalam python, kalian dapat menggunakan trik berikut
start_form = 1 # digunakan untuk membuat variabel dengan nilai 1
print(hobi2[2 - start_form]) # kalian bisa kurangi angka 3 (ibarat penghitungan pada manusia) dengan angka 1 (yang nantinya dapat sesuai dengan bahasa komputer)
# seperti contoh perintah di atas, kita ingin memunculkan hobi yang ke 2 pada variabel hobi2, tetapi dalam bahasa komputer atau index, hitungannya bukan ke 2 melainkan menjadi ke 1.
print()

buah = ["jeruk", "apel", "mangga", "pisang", "sirsak", " semangka", "delima", "durian"]
remaster_buah = buah 

print("panjang data dari variabel buah dalam index: ",len(buah) - 1)
print(f"ini buah ----------> {buah}")

print(buah[len(buah) - 1])

remaster_buah[1] = "jambu" # variabel ini menimpa isi dari variabel buah dengan nilai yang baru
print(f"ini remaster_buah -> {remaster_buah}")

