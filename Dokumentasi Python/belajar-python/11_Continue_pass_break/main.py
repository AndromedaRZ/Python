# continue, pass, break

# pass -> dia berfungsi sebagai dummy, artinya tidak akan dieksekusi

# angka = 0

# while angka < 5:
#     angka += 1
    
#     if angka == 3:
#         pass # pass di sini tidak akan dieksekusi 
    
#     print(angka)
    
# print("\n")


# continue

angka = 0

print(f"Angka sekarang -> {angka}")

while angka < 5:
    angka += 1
    print(f"Angka sekarang -> {angka}")
    
    if angka == 3:
        print("Bagus!")
        continue # continue di sini akan membuat loop langsung melanjutkan ke perulangan berikutnya
        # bisa dikatakan kalo fungsinya nge-skip perintah di bawah dan langsung balik lagi untuk mengulang perulangan yang berikutnya
    
    print("Whassapp!!!")
    
print("Nice!\n")

# break

angka = 0

while angka < 5:
    angka += 1
    print(f"Angka sekarang -> {angka}")
    
    
    if angka == 3:
        print("Nice!")
        break # break ini berfungsi untuk menghentikan looping dari perintah while
    
    print("Wassup!!")
    
print("Program selesai\n")

data_int = int(input("Hitung sampai = "))
angka = 0

while True:
    angka += 1
    print(f"Hitung = {angka}") # terminal akan menjalankan perintah print "Hitung = "dari 1 sampai tak terhingga
    
    if angka == data_int: # sebagai contoh ketika kita menginput 10, maka ketika loopingnya terjadi selama 10 kali, baris ini akan tereksekusi karena nilai loopingnya sama seperti input yang kita masukkan tadi
        print("Nice!")
        break # dan pada perulangan ke 10 perintah break ini akan aktif sehingga memberhentikan looping yang tak terhingga
    print("Wassup!") # saat perintah break tereksekusi, maka perintah print di sini akan dilewatkan
    
print("Program selesai") # lalu langsung mengarah ke perintah di luar looping (di luar while)