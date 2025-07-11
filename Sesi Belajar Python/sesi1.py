# Belajar python sesi 1
import random

welcome_message = "Selamat datang di CUYPY GAMES"
posisi_cuypy = random.randint(1, 4)

print("***********************************")
print(f"** {welcome_message} **")
print("***********************************")

# nomor_saya = input("Masukkan angka yang telah ditentukan :")

# if nomor_saya == 4:
#     print(f"Yes, benar nomor saya adalah {nomor_saya}")
# else:
#     print(f"Yah, nomor saya bukan {nomor_saya}")

nama_anda = input("Masukkan nama anda: ")
print(f'''Halo! {nama_anda}, coba perhatikan goa di bawah ini
      
      |_|  |_|  |_|  |_|
      ''')

while True:
    print("Menurut kamu, di goa nomor berapakah CUYPY berada? [1 / 2 / 3 / 4 ]")
    jawaban = int(input("Masukkan jawabanmu: "))
    print()
    konfirmasi = input(f"Apakah kamu yakin bahwa CUYPY ada di goa nomor {jawaban} [y/n]")
    print()
    if konfirmasi == "y":
        break
    elif konfirmasi == "n":
        print("Tidak yakin!, coba lagi")
    else:
        print("Silahkan masukkan jawaban yang benar! y/n")

if jawaban == posisi_cuypy:
    print(f"Selamat {nama_anda}, kamu menemukan CUYPY di goa nomor {posisi_cuypy} dan pilihanmu adalah goa nomor {jawaban}")
else:
    print(f"Maaf {nama_anda}, CUYPY tidak berada di goa yang kamu pilih, tapi ada di goa nomor {posisi_cuypy}, sementara kamu memilih goa nomor {jawaban}")