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
    
print("Nice!")
    