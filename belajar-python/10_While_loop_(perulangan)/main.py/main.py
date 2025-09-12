# while loop (perulangan)

# while kondisi:  --> ketika kondisinya
#   aksi ini
#   aksi itu

# angka = 10

# while angka > 5: # ketika kondisi (while) True, maka sistem akan terus mengeksekusinya tanpa henti sehingga menybebakan infinity loop (perulangan tanpa batas)
#     print("ucup kece!!")
# print("cukup!!")

# bisa kita buat alternatifnya seperti di bawah ini
angka = 0
while angka < 5: # perintah ini akan terus dieksekusi ketika True, tapi akan berhenti ketika kita membuatnya menjadi False
    angka = angka + 1 # setiap perulangan akan menambahkan angka sebanyak 1 ke dalam variabel angka
    print(f"angka sekarang adalah {angka}") # setiap perulangan akan menampilkan berapa jumlah dari variabel angka sekarang dan akan berhenti ketika kondisinya menjadi False tepatnya ketika nilainya melebihi kondisi yaitu melebihi 5
    
print("Program selesai")