# Operator dalam bentuk methods

# *note: setiap method akan menyatu dengan variabel ataupun data yang ada di depannya, biasanya dipisahkan dengan tanda titik dan diakhiri dengan buka dan tutup kurung seperti contoh:
# salam.upper()
# salam.lower()
# salam.islower()
# untuk contoh yang lainnya bisa dilihat pada kode yang ditulis di bawah ini
 
## merubah case dari string

# merubah semua huruf menjadi uppercase (besar semua)
salam = 'bro!'
print("normal =", salam)

salam = salam.upper() # .upper ini adalah method yang digunakan untuk variabel salam yang biasanya ditandai dengan titik atau dot
# method .upper ini akan mengubah semua huruf atau string yang ada di dalam variabel salam menjadi kapital atau besar semua (uppercase)
print("uppercase =", salam)

# merubah semua huruf menjadi lowercase (kecil semua)
alay = "aKu KecEE bAdaiIi!!"
print("normal =", alay) # outputnya sama seperti data aslinya yaitu semua huruf uppercase dan lowercasenya berantakan

alay = alay.lower() # dengan menggunakan method .lower yang disandingkan dengan variabel alay, maka data yang ada di variabel alay akan menjadi huruf kecil semua (lowercase)
print("lowercase =", alay)

## pengecekan dengan isX method

# contoh pengecekkan lowercase dan uppercase
salam = "sist"
apakah_lower = salam.islower() # method .islower ini berfungsi untuk mengecek apakah variabel salam berisikan data yang lowercase atau tidak, jika tidak hasilnya akan True dan menjadi False ketika berlaku sebaliknya
print(salam, "is lower =", apakah_lower)

apakah_upper = salam.isupper() # hampir sama seperti .islower, hanya saja method ini akan menjadi True ketika data yang ada dalam variabel berisi huruf uppercase dan menjadi False ketika berlaku sebalilknya
print(salam, "is upper =", apakah_upper)

# method .islower dan .isupper ini akan menghasilkan tipe data boolean (True atau False)

# isalpha() -> untuk mengecek semuanya huruf
# isalnum() -> untuk mengecek semuanya angka dan huruf (alphanumeric)
# isdecimal() -> untuk mengecek angka saja
# isspace() -> mengecek misalnya ada kekosongan dalam string sepert spasi, tab, newline(\n)
# istitle() -> untuk mengecek semua kata dimulai dengan huruf besar

judul = "It Is Ok Not To Be Orkay"
cek_judul = judul.istitle() # hasilnya boolean (True/False)
# jika semua katanya diawali dengan huruf besar, maka akan menjadi True
# tetapi jika ada kata yang tidak diawali dengan huruf besar bahkan walaupun hanya satu kata, maka akan menjadi False
print(judul, "is title =" , cek_judul)

## mengecek komponen .startswith() dan .endswith() --> keren katanya

cek_start = "Sangjangnim Oppa".startswith("Sangjangnim") # kode ini ditulis sedikit berbeda, karena kita langsung memasukkan isi dari datanya ke dalam method, jadi tidak menggunakan variabel terlebih dahulu seperti baris kode yang ada di atas
# .startswith() akan mengecek apakah input yang ada di methodnya sesuai dengan data yang ada di depan method tersebut
# jika benar akan menjadi True dan jika salah akan menjadi False, method ini juga bersifat Case Sensitive jadi pastikan input methodnya sesuai dengan data yang diinginkan
print("start =", cek_start)

cek_end = "Sangjangnim Oppak".endswith("Oppak") # hampir sama seperti .startswith(), hanya saja .endswith() berfungsi untuk mengecek data yang ada di belakang apakah sesuai dengan inputnya atau tidak
#  jika benar akan menjadi True dan jika salah akan menjadi False, method ini juga bersifat Case Sensitive
print("end =", cek_end)

## penggabungkan komponen .join() dan pemisahan .split()

pisah = ['melon', 'semangka', 'jeruk']
print(pisah)

gabungan = ', '.join(pisah) # berfungsi untuk memasukkan data yang ada di depan .join() yaitu ", " ke dalam list variabel pisah
print(gabungan) # hasilnya akan berbeda ketika kita nge-print variaebl pisah langsung, kurung buka dan tutup [] dan petik satu yang memisahkannya akan ditiadakan dan diganti dengan nilai yang kita masukkan di method .join()

gabungan = ' '.join(pisah) # kita juga bisa mengisi method .join() ini dengan nilai yang lain dan tidak terbatas pada koma saja
print(gabungan)

gabungan = ' ehm '.join(pisah)
print(gabungan)

print(gabungan.split('ehm')) # fungsi method .split() ini berkebalikan dari .join() yaitu untuk memisahkan suatu data yang ada di variabel, pada bagian kurung splitnya kita isi dengan nilai yang ingin kita pisahka
# nantinya kumpulan data tersebut akan kembali ke bentuk list

## alokasi karakter menggunakan method .rjust(), .ljust() dan .center()

kanan = "kanan".rjust(20) # berarti right justify (rata kanan) dan methodnya kita isi seberapa jauh ingin menjadi rata ke kanan
# pada contoh diatas kita membuatnya menjadi 20, tetapi hal ini juga berpengaruh ketika kita membuat kata yang jumlahnya semakin panjang
print(f"'{kanan}'")

kiri = "kiri".ljust(20) # fungsinya untuk membuat semua teksnya left justify (rata kiri) dan ketentuannya serupa dengan .rjust()
print(f"'{kiri}'")

tengah = "tengah".center(20, "-") # di sebelah parameternya kita bisa memasukkan karakter yang kita inginkan sebagai pengganti spasi saat melakukan rata kiri kanan
# .center() berfungsi sebagai rata kiri kanan (hampir mirip justify) dan memiliki ketentuan yang serupa dengan .ljust() dan r.kust()
print(f"'{tengah}'")

# kebalikannya -> .strip()

tengah = tengah.strip('-') # mengilangkan karakter yang kita inginkan sekaligus rata kiri kanan sehingga menjadi default
print(f"'{tengah}'")