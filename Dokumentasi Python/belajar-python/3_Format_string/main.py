## Format string

# contoh generic

# string
nama = "ucup"
format_str = f"Hello, {nama}" # kita bisa menambahkan huruf f di depan string agar nantinya di dalam string tersebut bisa kita sisipkan variabel secara langsung dengan menggunakan kurung kurawal dan nama variabelnya
# cara ini bisa disebut dengan f-string atau format string
# f-string ini sangat berguna untuk mempersingkat kode, dan kita bisa menghindari penggunaan simbol tambah (+) dan koma (,) yang berlebih
print(format_str)

# contoh penggunaannya pada boolean
boolean = True
format_str = f"boolean = {boolean}"
print(format_str)

# angka
angka = 2005.5
format_str = f"angka = {angka}"
print(format_str)

# bilangan bulat
angka = 15
format_str = f"bilangan bulat = {angka:d}" # (:d) ini berguna untuk menandakan bahwa variabel ini adalah bilangan bulat, tetapi akan menjadi error ketika data yang ada di variabel terebut bukan bilangan bulat/integer
print(format_str)

# bilangan dengan ordo ribuan
angka = 2000000
format_str = f"ribuan = {angka:,}" # fungsi (:,) akan memisahkan angka sama halnya seperti angka ribuan, ratusan ribuan, dan jutaan
print(format_str)

# bilangan desimal
angka = 2005.54321
format_str = f"desimal = {angka:.2f}" # fungsi .2f adalah untuk menandakan bahwa kita akan menggunakan 2 angka ke belakang dari koma atau titik sehingga menjadikannya angka desimal, angka sebelum huruf f juga bisa kita ubah sesuai dengan berapa banyak angka yang ingin kita pakai di belakang koma (atau titik)
print(format_str)

# menampilkan leading zero (atau angka di depan koma)
angka = 2005.54321
format_str = f"desimal = {angka:010.2f}"
print(format_str)

# menampilkan tanda + atau -
angka_minus = -10
angka_plus = 10
angka_plus2 = 15.29342
format_minus = f"minus = {angka_minus:+d}" # fungsi +d ini untuk memunculkan keterangan plus atau minus pada nilai atau angkanya, jika nilainya negatif maka akan muncul tanda minus (-)
format_plus = f"plus = {angka_plus:+.2f}" # jika nilainya positif, maka akan muncul tanda plus (+)
format_plus2 = f"plus2 = {angka_plus2:+.2f}" # kita juga bisa mengkombinasikannya dengan format yang sebelumnya

print(format_minus)
print(format_plus)
print(format_plus2)

# memformat persen
persentase = 0.045
format_persen = f"persen = {persentase:%}" # (:%) berfungsi untuk menambahkan simbol persentase ke dalam angkanya
print(format_persen)

format_persen = f"persen = {persentase:.2%}" # kita bisa mengetiknya menjadi (:.2%) untuk membuat agar hanya 2 angka saja yang ditampilkan di belakang titik
print(format_persen)


# melakukan operasi aritmatika di dalam placeholder
harga = 10000
jumlah = 5

format_string = f"harga total = Rp. {harga*jumlah:,}" # variabel harga dan jumlah bisa melakukan operasi aritmatika di dalam f-string, kita juga bisa menambahkan format dengan menggunakan (:,) untuk hasil penjumlahannya
print(format_string)

# format angka lain (binary, octal, hexadecimal)

angka = 255
format_binary = f"binary = {bin(angka)}"
format_octal = f"octal = {oct(angka)}"
format_hex = f"hex = {hex(angka)}"

print(format_binary)
print(format_octal)
print(format_hex)