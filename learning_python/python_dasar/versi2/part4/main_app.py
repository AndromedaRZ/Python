# kontrol alur program

# cara untuk mengatur jalannya program berdasarkan kondisi tertentu
# dengan kontro alur, program bisa mengambil tindakan berdasarkan situasi dan kondisi tertentu

'''pernyataan if'''
# pernyataan if digunakan untuk menjalankan kode hanya jika kondisi bernilai True
# setelah membuat if harus ada titik dua (:)
# kode yang akan dijalankan ketika kondisi if menjadi True harus diberi indentasi (diberi spasi di awal)
# spasi yang diberikan bisa 2 spasi atau 4 spasi, tapi direkomendasikan menggunakan 4 spasi dengan menggunakan tombol 'tab'

angka = int(input("Masukkan angka: "))

if angka > 0: # jika angka yang diinput di atas lebih dari 0, maka baris if ini akan tereksekusi
    print("Angka positif")
# spasi di depan ini adalah indentasi    

if angka < 0: # jika angka yang diinput di atas kurang dari 0, maka baris if ini akan tereksekusi
    print("Angka negatif")
    
    
if angka == 0: # jika angka yang diinput di atas adalah 0, maka baris if ini akan tereksekusi
    print("Angka nol")

'''pernyataan if else'''
# fungisnya hampir mirip dengan if, hanya saja ada tambahan statement else
# if-else digunakan ketika kita ingin menjalankan kode dengan kondisi yang berbeda untuk 2 kondisi yaitu True dan False

nilai = int(input("Masukkan nilai: "))

if nilai > 75: # jika nilai yang dimasukkan lebih besar dari 75, maka baris if ini akan tereksekusi
    print("Anda lulus!")
else: # jika nilai yang dimasukkan lebih kecil dari 75, maka baris else ini akan tereksekusi
    print("Anda tidak lulus!")

'''pernyataan else if (elif)'''
# else if (elif) digunakan untuk mengecek beberapa kondisi secara berurutan

nilai = int(input("Masukkan nilai: "))

if nilai >= 90:
    print("Grade A")
elif nilai >= 80:
    print("Grade B")
elif nilai >= 70:
    print("Grade C")
elif nilai >= 60:
    print("Grade D")
else:
    print("Grade E")
    
# jika kita membuatnya hanya dengan menggunakan if-else (tanpa elif), maka semua kondisi (4 kondisi di atas) akan tereksekusi
# maka dari itu kita perlu menggunakan elif agar program hanya menjalankan 1 kondisi yang terpenuhi
# jika salah satu kondisi terpenuhi, maka program tidak akan menjalankan kondisi lain yang tidak terpenuhi

'''kondisi dengan operator logika'''
# karena kondisi harus bernilai boolean, artinya kita bisa menggunakan operator, misalnya operator logika: and, or, not

umur = int(input("Masukkan umur: "))
punya_sim = input("Punya SIM? (ya/tidak): ")

if umur >= 17 and punya_sim == 'ya':
    print("Boleh mengendarai motor")
else:
    print("Tidak boleh mengendarai motor")
    
'''nested if (if bersarang)'''
# kita bisa menempatkan if di dalam if lagi

user = input('Username: ')
pw = input('Password: ')

if user == 'admin':
    if pw == '123':
        print('Login berhasil!')
        print('Selamat datang admin')
    else:
        print("Password salah!")
else:
    print('Username tidak ditemukan!')
# posisi if dan else diperhatikan apakah sejajar atau tidak


'''pernyataan match case'''
# match-case adalah fitur alternatif yang lebih bersih untuk elif yang banyak

hari = input("Masukkan nama hari: ").lower()

match hari:
    case 'senin' | 'selasa' | 'rabu' | 'kamis' | 'jumat': # kita bisa menggunakan | untuk membuat banyak kondisi
        print("Hari kerja")
    case 'sabtu' | 'minggu':
        print("Hari libur")
    case _:
        print("Nama hari tidak valid!")

# perbandingan ketika menggunakan if-elif-else
if hari == 'senin' or hari == 'selasa' or hari == 'rabu' or hari == 'kamis' or hari == 'jumat':
    print("Hari kerja")
elif hari == 'sabtu' or hari == 'minggu':
    print("Hari libur")
else:
    print("Nama hari tidak valid!")

# dengan menggunakan if-else, maka baris kodenya kelihatan berantakan
# maka dari itu pada kasus seperti itu kita bisa menggunakan match case

'''conditional expression (ternary operator)'''
# conditional expression memungkinkan kita menulis kode sederhana dalam satu baris

angka = int(input("Masukkan angka: "))
# dengan if-else biasa
if angka > 0:
    hasil = 'Positif'
else:
    hasil = 'Non-positif'
    
# dengan ternary operator (lebih singkat)
hasil = 'Positif' if angka > 0 else 'Non-positif'
print(f"Angka tersebut: {hasil}")