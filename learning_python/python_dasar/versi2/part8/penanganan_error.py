'''penanganan error'''
# bagaimana cara untuk menangani error agar program tidak berhenti?
# penanganan error memungkinkan program untuk menangani error dengan baik tanpa berhenti secara tiba-tiba


'''try-except'''
# try dan except digunakan untuk menangani error yang mungkin terjadi
# kita membuat blok kode try: dan error:
# di dalam try masukkan kode yang kira-kiranya akan terjadi error
# maka nantinya ketika terjadi error -> blok kode except akan tereksekusi

# contoh
print("=== Kalkulator sederhana ===")
try:
    angka1 = int(input("Masukkan angka pertama: "))
    angka2 = int(input("Masukkan angka kedua: "))
    hasil = angka1 / angka2
    print("Hasil:", hasil)
    # ketika baris kode di dalam 'try' ini mengalami error
    # entah apapun itu alasannya
    # maka baris except akan langsung tereksekusi dan menjalankan perintah di dalamnya daripada menampilan kode error yang membuat programnya berhenti sendiri
    
except:
    print("Terjadi error dalam perhitungan!")
    
print("Program selesai!")   # ketika kita menggunakan try-except, maka program akan berjalan lancar sampai semua baris kode tereksekusi meskipun ada beberapa baris kode yang mengalami error


'''menangani error spesifik'''
# try-except digunakan untuk menangani error yang umum seperti contoh di atas
# namun, sebenarnya ketika kita mengalami error, kita juga melakukan penanganan yang berbeda untuk error yang berbeda juga
# kita bisa menyebutkan tipe error secara spesifik setelah kata kunci 'except'
# sehingga ketika terjadi error secara spesifik, maka bagian except spesifik tersebut akan tereksekusi
# kita juga bisa membuat lebih dari 1 except dalam blok try-except agar bisa menangani banyak kode error sekaligus

try:
    a = int(input("Masukkan angka pertama: "))
    b = int(input("Masukkan angka kedua: "))
    hasil = a / b
    print(f"Hasil pembagian: {hasil}")
except ValueError:
    # baris ini akan tereksekusi ketika user memasukkan input selain integer
    print("Mohon masukkan angka yang valid!")
except ZeroDivisionError:
    # baris ini akan tereksekusi ketika user memasukkan angka 0 untuk pembagiannya
    print("Tidak bisa membagi dengan angka 0")
except:
    # baris ini akan tereksekusi ketika user melakukan kesalahan yang lain selain 2 spesifik di atas
    print("Terjadi kesalahan lain!")

print("Program selesai!")


'''try-except-else'''
# try-except juga memiliki bagian else sama seperti if dan for
# bagian else akan dieksekusi jika tidak ada error pada try-except
# jika terjadi error, maka bagian else tidak akan tereksekusi

try:
    angka = int(input("Masukkan angka: "))
except ValueError:
    # jika mengalami error, maka sistem hanya akan menjalankan baris kode except tanpa menjalankan else
    print("Input tidak valid")
else:
    print("Angka yang anda masukkan:", angka)
    if angka > 0:
        print("Angka positif")
    elif angka < 0:
        print("Angka negatif")
    else:
        print("Angka nol")


'''try-except finally'''
# else pada try-except hanya akan dijalankan jika kode tidak mengalami error
# bagaimana jika kita ingin tetap melakukan sesuatu, baik itu setelah terjadi error atau tidak?
# maka kita bisa menggunakan 'finally'
# finally akan selalu dijalankan, baik itu setelah mengalami error atau tidak

try:
    angka = int(input('Masukkan angka: '))
    print("Angka anda:", angka)
except ValueError:
    print("Input tidak valid")
finally:
    print("Program selesai dieksekusi")