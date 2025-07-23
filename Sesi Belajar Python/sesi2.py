# Belajar python sesi 2
import random
from libs import welcome_message # from (nama file nya tanpa py) lalu import (pilih function yang manan yang ingin kita ambil dari file libs.py tersebut)

welcome_message("WELCOME TO CUYPY")


nama_anda = input("Masukkan nama anda: ")

while nama_anda == "":
    nama_anda = input("Masukkan nama anda terlebih dahulu: ")
    
while True:
    print(f"\nHalo! {nama_anda}, coba perhatikan goa di bawah ini\n")

    posisi_cuypy = random.randint(1, 4)
    bentuk_goa = "|_|"
    goa_kosong = [bentuk_goa] * 4 # goa ini akan tetap kosong
    goa = goa_kosong.copy() # goa ini akan menentukan dimana cuypy berada
    goa[posisi_cuypy - 1] = "|0_0|"

    goa_kosong = ' '.join(goa_kosong) # perintah 'join' akan memasukkan spasi (yang diantara tanda kutip sebelumnya) ke dalam nilai atau array nya pada variabel goa_kosong dan otomatis akan menghapus sisa bentuk array seperti siku-siku dan tanda kutip pada output goa kosongnya
    goa = ' '.join(goa)

    print(goa_kosong)
    print("\nMenurut kamu, di goa nomor berapakah CUYPY berada? [1 / 2 / 3 / 4 ]\n")

    jawaban = int(input("Masukkan jawabanmu: "))

    konfirmasi = input(f"Apakah kamu yakin bahwa CUYPY ada di goa nomor {jawaban}? [y/n]: ")

    if konfirmasi == "n":
        print("Silahkan mulai ulang programnya")
        exit()
    elif konfirmasi == "y":
        if jawaban == posisi_cuypy:
            print(f" \n {goa} \n\n Selamat kamu menang!")
        else:
            print(f"\n {goa} \n\n Maaf kamu kalah")
    else:
        print("Silahkan mulai ulang programnya")
        exit()
        
    play_again = input("\nApakah kamu ingin mengulangi permainannya? [y/n]: ")
    if play_again == "n":
        break
    while play_again != "y": 
        play_again = input("\nApakah kamu ingin mengulangi permainannya? [y/n]: ")
        if play_again == "n":
            print("Program selesai!")
            exit()

print("Program selesai!")
    