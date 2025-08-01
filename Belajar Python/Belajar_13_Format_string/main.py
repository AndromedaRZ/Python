# Format string

# contoh generic
# string
nama = "ucup"
no_format_str = "hello " + nama # menggunakan operator + untuk menggabungkan string
format_str = f"hello {nama}" # menggunakan f-string untuk memasukkan variabel ke dalam string

# dari kedua cara di atas, memakai f-string lebih mudah dibaca dan ditulis

print(no_format_str)
print(format_str) 

# boolean
boolean = True
format_str = f"boolean = {boolean}"
print(format_str)

# angka
angka = 2005.4
format_str = f"angka = {angka}"
print(format_str)

# bilangan bulat
angka = 15
format_str = f"bilangan bulat = {angka:d}" # fungsi ':d' adalah untuk menampilkan bahwa variabel angka berisi bilangan bulat
print(format_str)

# bilangan ribuan
angka = 2000000
format_str = f"ribuan = {angka:,}" # fungsi ':,' adalah untuk memasukkan koma secara otomatis pada nilai di dalam variabel angka, agar setiap nilai angka seperti ribuan, ratusan, bahkan jutaan akan secara otomatis menempatkan koma sebagai pemisah digit nya
print(format_str)

# bilangan desimal
angka = 2005.5
format_str = f"desimal = {angka}"
print(format_str)