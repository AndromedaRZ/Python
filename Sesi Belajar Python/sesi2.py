# Belajar python sesi 2
import random
import sys

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
print(f"\nHalo! {nama_anda}, coba perhatikan goa di bawah ini\n")

bentuk_goa = "|_|"
goa = [bentuk_goa] * 4

goa[posisi_cuypy - 1] = "|0_0|"

print(goa)

print("\nMenurut kamu, di goa nomor berapakah CUYPY berada? [1 / 2 / 3 / 4 ]\n")

jawaban = int(input("Masukkan jawabanmu: "))

konfirmasi = input(f"Apakah kamu yakin bahwa CUYPY ada di goa nomor {jawaban}? [y/n]:")

if konfirmasi == "n":
    print("Silahkan mulai ulang programnya")
    sys.exit()
elif konfirmasi == "y":
    if jawaban == posisi_cuypy:
        print(f"Selamat {nama_anda}, kamu menemukan CUYPY di goa nomor {posisi_cuypy} dan pilihanmu adalah goa nomor {jawaban}")
    else:
        print(f"Maaf {nama_anda}, CUYPY tidak berada di goa yang kamu pilih, tapi ada di goa nomor {posisi_cuypy}, sementara kamu memilih goa nomor {jawaban}")

else:
    print("Silahkan mulai ulang programnya")
    sys.exit()