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
angka = 2005.54321
format_str = f"desimal = {angka:.2f}" # tanda titik '.' menandakan desimalnya, lalu fungsi '2f' adalah mengambil sejauh mana angka floatnya, dalam kasus ini karena angkanya '2' maka jumlah angka float (yang dibelakang koma) yang diambil hanya 2 digit 
print(format_str)

# menampilkan leading zero
angka = 2005.54321
format_str = f"desimal = {angka:9.3f}" # angka '9' berfungsi untuk menambahkan sesuatu didalam variabel 'angka'
print(format_str)

# contoh lain leading zero
angka = 2005.54321
format_str = f"desimal = {angka:09.3f}" # angka '9' berfungsi untuk menambahkan sesuatu didalam variabel 'angka', dan yang ditambahkan adalah angka '0' disebelah angka '9' tersebut
print(format_str)

# menampilkan tanda + atau -
angka_minus = -10
angka_plus = 10
format_minus = f"minus = {angka_minus}" # jika diprint, simbol mines (-) akan terlihat
format_plus = f"plus = {angka_plus}" # jika diprint, simbol plus (+) tidak akan terlihat
format_minus2 = f"minus = {angka_minus:+d}" # jika diprint, simbol mines (-) akan tetap terlihat
format_plus2 = f"plus = {angka_plus:+d}" # jika diprint, simbol plus (+) akan terlihat

print(format_minus)
print(format_plus)
print(format_minus2)
print(format_plus2)

# memformat persen
persentase = 0.045
format_persen = f"persen = {persentase:.2%}" # fungsi dari ':' adalah untuk memulai bagian format, diikuti dengan '.2' yang berarti dua angka di belakang koma, dan simbol persen (%) untuk mengubah angka desimal menjadi persentase (dikalikan 100 dan ditambah dengan tanda %)
print(format_persen) 

# melakukan operasi aritmatika di dalam placeholder
harga = 10000
jumlah = 5

format_string = f"harga total = {harga*jumlah:,}" # kita bisa melakukan operasi aritmatika didalam kurung kurawal yang berisi variabel harga dan jumlah
print(format_string)

# format angka lain (binary, octal, hexadecimal)

angka = 255
format_binary = f"binary = {bin(angka)}" # konversi nilai dari variabel angka ke bilangan biner
format_octal = f"octal = {oct(angka)}" # konversi nilai dari variabel angka ke bilangan octal
format_hex = f"hex = {hex(angka)}" # konversi nilai dari variabel angka ke bilang hexadesimal

print(format_binary)
print(format_octal)
print(format_hex)