print("BANK OF RIZKY")

percobaan = 5

pin = int(input("Masukkan sandi untuk membuka brankas anda: "))

while pin != 1234 and percobaan > 0:
    pin = int(input("sandi salah, silahkan masukkan sandi kembali: "))
    percobaan -= 1
    print(f"sisa percobaan anda: {percobaan}")
    
if percobaan == 0:
    print("Percobaan anda sudah habis") 
    exit()
else:
    print("sandi berhasil, Selamat datang kembali Rizky :)")