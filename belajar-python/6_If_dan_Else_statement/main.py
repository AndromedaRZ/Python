# if dan else statement

# singkatnya, if dan else bisa kita gunakan untuk membuat percabangan dari alur program yang kita buat dengan kondisi yang berbeda-beda

# 1. if (kondisinya)
#       aksinya ketika kondisi if terpenuhi
# 2. else (else akan tereksekusi jika kondisi di if tidak terpenuhi)
#       aksinya

nama = input("Siapa nama anda? ")

# 1. program if inline/satu baris
# if nama=="ucup" : print("Kamu ganteng abieezzz!!!")
# print(f"terima kasih {nama}")


# 2. program if indentation
if nama == 'ucup': # kita tambahkan new line atau garis baru untuk melanjutkan penngetikkan program agar berjalan di atas aksi if
    print("Kamu ganteng abiezz!")
    print("Kamu keren banget!!")
print(f"Terima kasih {nama}") # kita bisa setarakan indentasinya ke awal jika ingin keluar dari indentasi if sebelumnya

if nama == "otong":
    print("Hai otooongg, si keren!!!")
else: # else ini berfungsi untuk menambahkan kondisi lain ketika perintah dari if tidak terpenuhi (False)
    print("Ahh kamu bukan otong, kamu gak keren!")
print("Akhir dari program")

# jika kondisi di if benar (True) maka jalankan perintah setelah indentasinnya
# namun jika kondisi di if salah (False) maka jalankan perintah setelah baris else