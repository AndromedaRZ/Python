# Materi pembahasan string untuk modul python lanjutan

data = "Ini adalah string"
print(data, "tipe datanya adalah:",type(data))

# 1. Cara membuat string
'''
1. Menggunakan single quote (kutip satu) '...'
2. Menggunakan double quote (kutip dua) "..."

'''

print('Menggunakan single quote atau kutip satu')

print("Menggunakan double quote atau kutip dua")

print('"Halo, apa kabar?"') # kedua tanda kutip yang tadi juga bisa digunakan di dalam string, nantinya tanda kutip yang ada di dalam akan dianggap sebagai string sehingga akan muncul sebagai output juga, pada kasus ini bisa digunakan sebagai sebuah percakapan

print("'Halo, apa kabar?'") # hal yang sama akan terjadi begitupun ketika kutipnya diletakkan sebaliknya, asal posisi di antara kutip tersebut saling terhubung untuk membungkus sebuah teks atau kalimat, dan nantinya kutip yang ada di dalam yang akan muncul sebagai output

print("Hari ini adalah hari jum'at") # salah satu dari dua jenis kutip tersebut bisa kita jadikan sebagai penutup string ketika kita harus memasukkan kutip ke dalam teks string untuk melengkapi sebuah kalimat, contohnya ketika ingin memasukkan kata jum'at

# 2. Menggunakan tanda \ (back slash)

# membuat tanda ' menjadi string
print('Mari sholat jum\'at')
print('g\'day, isn\'t it?') # back slash ini juga bisa menjadi alternatif ketika kita tidak menggunakan kutip dua sebagai bungkus string "..."

# backslash
# biasanya kita tidak bisa memasukkan single back slash sebagai kalimat string
# untuk itu kita buat menjadi double back slash agar bisa masuk ke dalam string, seperti contoh penulisan PATH di bawah ini:
print("C:\\user\\ucup")

# tab
# fungsi tab ini sama seperti pada tab umumnya, hanya saja cara memasukkannya ke dalam string kita perlu mengetetik back slash dan huruf t secara berdekatan seperti \t
print("Andi\tdan beni")
# tab \t ini juga bisa kita gunakan sebagai awal paragraf
print("\tLorem ipsum dolor sit amet, consectetur adipiscing elit. Pellentesque suscipit mollis luctus. Ut in tristique libero. Sed ante sapien, vestibulum in hendrerit eu, ultricies vitae justo. Suspendisse id justo sed enim finibus facilisis a nec neque. Mauris eget magna nulla. In condimentum iaculis dictum. Vestibulum a eleifend tortor, et sollicitudin enim. Donec vestibulum pretium scelerisque.")

# backspace
# menggunakan black slash dan huruf b \b, seperti namanya yaitu berfungsi sebagai backslash
print("Andi \bBeni") # karena tanda \b ditempatkan setelah spasi, maka spasinya akan terhapus

# newline
# bisa dikatakan sebagai garis baru, paragraf baru atau nge-enter kalimat menggunakan tanda back slash dan huruf n \n atau r \r
print("Baris pertama.\nBaris kedua.") # LF -> Line Feed -> Biasanya dipakai di UNIX system seperti Linux, MacOS
print("Baris pertama.\rBaris kedua.") # CR -> Carriage Return -> Biasanya dipakai di system lama seperti Commodore, Acorn, lisp
print("Baris pertama.\r\nBaris kedua.")# CRLF -> Line Feed Cariage Return -> Biasanya dipakai oleh Windows
# Itu sebabnya setiap system sering mendeteksi 'Enter' ini dengan cara yang berbeda-beda

# 3. String literal atau raw

# hati-hati
print("C:\new folder") # pathnya akan menjadi salah dan membuat outputnya berantakan

# alternatifnya kita bisa menggunakan raw string, dengan cara menambahkan huruf r sebelum kalimat stringnya
print(r"C:\new folder")

# multiline literal string
print("""
Nama: Ryan  
Kelas: 3 SMP
""")

# multiline literal string raw, dengan cara menambahkan huruf r sebelum kalimat stringnya
print(r"""
Nama: Ryan
Kelas: 3 SMK\new normal
divisi: IT Support
""")